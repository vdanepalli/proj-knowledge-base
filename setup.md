# Setup Instructions

Run below commands to setup pre-commit hook that is triggered by `git commit`  

```bash
git init
git remote add origin git@github.com:vdanepalli/vd_elearning.git
touch .git/hooks/pre-commit
code .git/hooks/pre-commit
```

<br/><br/>


Copy below commands to `pre-commit`

```bash
#!/bin/sh
# pre-commit hook

echo "Running update.py before commit..."
python3 src/update.py

# Check if the python script executed successfully
if [ $? -ne 0 ]; then
  echo "Error running update.py. Aborting commit."
  exit 1 # Exit with non-zero status to abort the commit
fi

echo "Staging changes..."
# Stage all changes (including those potentially made by update.py)
git add .

echo "Pre-commit hook finished successfully. Proceeding with commit..."
exit 0 # Exit with zero status to allow the commit
```


<br/><br/>

- Make the `pre-commit` executable
```bash
chmod +x .git/hooks/pre-commit
```


<br/><br/>

Run `git add .` as usual and then run `git commit -m "..."`

<br/><br/>

Git Alias 

- `git config --global alias.amendnoedit 'commit --amend --no-edit'`
- `git config --global alias.pushf 'push --force'`
- `git config --global alias.pullr 'pull --rebase'`
- `git config --global alias.amendpush '!git add . && git commit --amend --no-edit && git push --force'`
