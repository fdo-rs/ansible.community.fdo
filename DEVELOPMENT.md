# Prepare development environment

Create python venv and clone code.

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install ansible-core  # 2.13.3

mkdir -p ansible_collections/community/
cd ansible_collections/community/
git clone git@github.com:xlab-si/community.fdo.git fdo
cd fdo

# Install community.general collection, since we like to have stdout_callback=community.general.yaml in ansible.cfg
ansible-galaxy collection install community.general
# Install dependencies needed by the collection (TODO - can be listed in galaxy.yml?)
ansible-galaxy collection install -r meta/requirements.yml
# Optional, if you want to run "ansible-test --venv ..."
# pip install -r test.requirements.txt -r sanity.requirements
```

Included `Makefile` contains shortcuts for common development tasks,
running tests, linter, code formatting, source directory cleanup etc.
To list all available commands, run just `make`, and you will get something like:

```
(.venv) [me@mypc fdo]$ make
Available targets:
clean:  ## Remove all auto-generated files
format:  ## Format python code with black
integration:  ## Run integration tests
sanity:  ## Run sanity tests
units:  ## Run unit tests
```

If you want to run tests with a single python version (e.g. not with whole test matrix), use:

```
ansible-test sanity --venv
ansible-test units --venv
ansible-test integration --venv
```

Build collection.

```yaml
ansible-galaxy collection build
```

Run sample playbook.
Sample ansible.cfg is there to ensure collection does not need to be installed.

```yaml
ansible-playbook -i localhost, sample-playbook.yml -v
```

# CI infrastructure

The CI integration tests require a preconfigured infrastructure -
VMs that already run FDO services.
We have a dedicated github actions runner that has access to those VMs.

In [DEV-github-runner.md](DEV-github-runner.md) are described steps used to setup the CI runner.

In (TODO) are described steps to setup VMs with FDO services.
