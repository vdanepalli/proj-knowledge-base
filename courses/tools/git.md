# [Git](../../courses.md)


- [Git](#git)
  - [LinkedIn: Practical Github Actions](#linkedin-practical-github-actions)
  - [LinkedIn: Practical GitHub Project Management and Collaboration](#linkedin-practical-github-project-management-and-collaboration)
  - [LinkedIn: Practical GitHub Copilot](#linkedin-practical-github-copilot)
  - [LinkedIn: Practical GitHuub Code Search](#linkedin-practical-githuub-code-search)
  - [LLM](#llm)
    - [Adding SSH Keys](#adding-ssh-keys)


## LinkedIn: Practical Github Actions

- Podcast Feed Generator : Problem  
  - XML -- Markup; RSS Feeds -- flavor of XML for Syndicating Content
- create rep
- copy [images audio feed readme](https://github.com/LinkedInLearning/github-practical-actions-4412872/tree/01_02b)
- setup github pages
  - deploy from a branch : main - root
- create codespace 
  - PyYAML module installed
  ```py
  # feed.yaml

  import yaml
  import xml.etree.ElementTree as xml_tree

  with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {
        'version':'2.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    }) 

    channel_element = xml_tree.SubElement(rss_element, 'channel')

    link_prefix = yaml_data['link']

    xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
    xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
    xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
    xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
    xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
    xml_tree.SubElement(channel_element, 'link').text = link_prefix

    xml_tree.SubElement(channel_element, 'category', {'text': yaml_data['category']})


    for item in yaml_data['item']:
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item['title']
        xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
        xml_tree.SubElement(item_element, 'description').text = item['description']
        xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
        xml_tree.SubElement(item_element, 'pubDate')pubDate.text = item['published']
        xml_tree.SubElement(item_element, 'title').text = item['title']

        enclosure = xml_tree.SubElement(item_element, 'enclosure', {
            'url': link_prefix + item['file'], 
            'type': 'audio/mpeg', 
            'length': item['length']
        })


    output_tree = xml_tree.ElementTree(rss_element)

    output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
  ```

- `git checkout main`
- `git merge 01_04e`
- `git push`
- actions > new workflow > setup workflow yourself 
  - creates .github/workflows
  - main.yml
    ```YAML
    name: Generate Podcast Feeds
    on: [push]
    jobs:
        build:
            runs-on: ubuntu-latest
            steps:
                - name: Checkout Repo
                    uses: actions/checkout@v3
                - name: Setup Python
                    uses: actions/setup-python@v4
                    with: 
                        python-version: '3.10'
                - name: Install Dependencies
                    run: |
                        python -m pip install --upgrade pip
                        pip install python
                - name: Run Feed Generator
                    run: python feed.py
                - name: Push Repo
                    run: |
                        git config user.name vdanepalli
                        git config user.email vdanepalli@gmail.com
                        git add .
                        git commit -m "Modified Feed"
                        git push
    ```
- commit changes
- setti ngs/actions -- workflow permissions -- provide read and write permissions


<br/><br/>

- create repo podcast-generator
- copy feed.py to this repo 

```Dockerfile
# Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git

RUN pip3 install PyYAML

COPY feed.py /usr/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```

```sh
#!/bin/bash

# Shebang specifies the interpreter that's going to execute this script

echo "=================" # prints to command line

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add -A && git commit -m "Update Feed"

git push --set-upstream origin main


echo "=================" 
```

```YAML
# action.yml

name: "Podcast generator"
author: "Vinay Danepalli"
description: "Generates a feed for a podcast from a YAML File"
runs:
    using: "docker"
    image: "Dockerfile"
branding:
    icon: "git-branch"
    color: "red"
inputs:
    email:
        description: The commiter's email address
        required: true
        default: ${{ github.actor }}@localhost
    name:
        description: The commiter's name
        required: true
        default: ${{ github.actor }}
```

```YAML
name: Generate Podcast Feeds
on: [push]
jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout Repo
                uses: actions/checkout@v3
            - name: Run Feed Generator
                uses: username/pdocast-generator_repo_name@main_branch_or_release_tag
            
```

- make sure entrypoint.sh has write permissions `chmod -R 775 entrypoint.sh`


<br/><br/>

- draft a release
- choose primary category: Utilities     
- choose another category: Deployment
- Add tags: v1.0
- Target: main 
- Generate release notes
- Set as a pre-release -- optional
- Publish release
- Update About
  - Description
  - Website 
  - Topics: Podcast Python Feed XML RSS GithubActions Actions
- Updaet Readme.md File  

## LinkedIn: Practical GitHub Project Management and Collaboration

- Classic Projects (board experiecne) vs Projects (new experience)
- Projects > Create New Project
- Table > Project Name = Github projects > Create
- Rename View1 to Table

## LinkedIn: Practical GitHub Copilot


## LinkedIn: Practical GitHuub Code Search 


## LLM

### Adding SSH Keys

```bash
# Create a key just for ~/Desktop/github work (ed25519 is modern & recommended)
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_githubdir -C "githubdir (Vinay’s Mac)"

# Start the agent (if not already)
eval "$(ssh-agent -s)"

# macOS keychain integration (Ventura+ syntax; works on Catalina too)
ssh-add --apple-use-keychain ~/.ssh/id_ed25519_githubdir 
# ssh-add -K ~/.ssh/id_ed25519_githubdir

pbcopy < ~/.ssh/id_ed25519_githubdir.pub # Copy to clipboard
```

```bash
nano ~/.ssh/config

# Default GitHub behavior (outside of ~/Desktop/github/)
# If you already have a default IdentityFile for other hosts, keep it here.
Host github.com
  User git
  AddKeysToAgent yes
  UseKeychain yes
  # If you have a "main" key you want outside this folder, list it here:
  # IdentityFile ~/.ssh/id_ed25519
  # IdentitiesOnly no

# SPECIAL RULE: only when you're *in* ~/Desktop/github/ (or subfolders)
# we force the dedicated key for GitHub.
Match host github.com exec "pwd | grep -q '^$HOME/Desktop/github/'"
  Hostname github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_githubdir
  IdentitiesOnly yes
```

```bash
mkdir -p ~/Desktop/github/test
cd ~/Desktop/github/test

# This should authenticate with the *githubdir* key you just added to GitHub:
ssh -T git@github.com
```