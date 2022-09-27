# About

Just notes about how we setup self-hosted github runner.

Main thing - ensure runner will have network access to hosts running
FDO services required for integration tests. 

# Runner setup

Start with empty VM, 2 CPU, 4 GB RAM, 20 GB disk, CentOS 8-stream or CentOS 9.

Follow https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners.
It sends you to https://github.com/<username>/community.fdo/settings/actions/runners/new.
Copy-paste commands, with small modification - start with
```
cd /opt
GHUSER=github_username
sudo mkdir actions-runner-$GHUSER && sudo chown $USER actions-runner-$GHUSER && cd actions-runner-$GHUSER

curl -o actions-runner-linux-x64-2.297.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.297.0/actions-runner-linux-x64-2.297.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.297.0.tar.gz
sudo ./bin/installdependencies.sh
./config.sh --url https://github.com/$GHUSER/community.fdo --token CHANGEME
./run.sh
```

Configure runner as service - https://docs.github.com/en/actions/hosting-your-own-runners/configuring-the-self-hosted-runner-application-as-a-service

```bash
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status
```
