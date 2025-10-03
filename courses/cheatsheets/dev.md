# Development

## Virtual Environments

Sandbox, Isolated bubble
Dependency conflicts, Polluting Global Space, Permission Issues, Reproducability

```bash
# Built-in venv module 
python -m venv .venv # .venv is directory
source .venv/bin/activate # Linux
.venv\Scripts\Activate.ps1 # Powershell
.venv\Scripts\activate.bat # Command Prompt

pip list

deactivate

pip freeze > requirements.txt

pip install -r requirements.txt
pip install package-name
pip uninstall package-name

python -m venv --without-pip .venv
python -m venv --system-site-packages .venv # allows access to global site-packages
```


```bash
# Conda -- package & env manager -- distribution and env management system

conda create --name <environment_name> <packages_to_install>
conda create -n <environment_name> <packages_to_install>
conda create -n data-analysis-env python=3.9 numpy pandas matplotlib

conda create -n ml-gpu-env python=3.8 cudatoolkit=11.3 cudnn -c conda-forge -c nvidia

conda init <your_shell_name> # bash, zsh, powershell
conda activate <environment_name>
conda deactivate

conda install <package_name> <another_package_name>
conda install --name <environment_name> <package_name> # Install without activating

conda list
conda list -n <env_name>

conda info --envs # list envs
conda env list # list envs

conda remove <package_name>

conda env export --name <environment_name> > environment.yml
conda env export > environment.yml # export active env

conda env create -f environment.yml

conda remove --name <environment_name> --all # remove env
conda env remove --name <environment_name> # remove env
```


```bash
# Channels -- locations where packages can be found

defaults
-c conda-forge
-c pytorch
-c nvidia

conda config --add channels <channel_name> # order matters
```


<br/><br/>

`sdist` -- source distribution is essentially an archive, like `.tar.gz` `.zip` -- source code, metadata, setup .py
- download source code, run setup .py, compile extensions(requires compilers if any), generate metadata, copy .pyc files, compiled extensions, data files into site-packages dir

Wheel (PEP 427)
- `.whl` built distribution format
- zip archive with a specific file naming convention
- contains .pyc, compiled extension modules - binaries for specific python and platform, package data, metadata in .dist-info dir, RECORD file - list of all files and their hashes
- `<distribution>-<version>-<build_tag>-<python_tag>-<abi_tag>-<platform_tag>.whl`
- ABI - Application Binary Interface

```bash
pip install setuptools wheel
python setup.py bdist_wheel

pip install build # modern approach
python -m build # generates sdist and whl

pip install twine # needed for uploading distributions 

pip download -r requirements.txt -d <download_directory> # ex: ./offline_packages dir

pip install --no-index --find-links ./offline_packages -r requirements.txt # only looks in specified dir; --no-index = not to connect to PyPi or online index
```

