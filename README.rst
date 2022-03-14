Resilio Connect API python module
=================================

Steps to install the module (Ubuntu 20.04)
--------

Install dependencies first

.. code-block:: bash

    sudo apt update
    sudo apt install python3 python3-pip git
    python3 -m pip install requests

Clone repo

.. code-block:: bash

    git clone https://github.com/resilio-inc/python-management-console-api-module.git

Build the module

.. code-block:: bash

    cd ./python-management-console-api-module
    python3 setup.py build

Install the module globally

.. code-block:: bash

    python3 setup.py install

Check if the module has installed successfully

.. code-block:: bash

    python3 -m pip freeze | grep connect-api


Usage examples
--------

Create group

.. code-block:: python

    from connect_api import ConnectApi

    api = ConnectApi('https://localhost:8443', '<API-token>')
    cloud_agents = []

    for a in api.get_agents():
        for t in a.tags:
            if t['name'] == 'CLOUD':
                cloud_agents.append(a)
                break

    api.create_group('Cloud agents', cloud_agents)

Create and start distribution job:

.. code-block:: python

    from connect_api import ConnectApi

    api = ConnectApi('https://localhost:8443', '<API-token>')
    agents = api.get_agents()
    jobs = api.get_jobs()

    src_group = api.create_group('src.group', [agents[0]])
    dst_group = api.create_group('dst.group', agents[1:])

    job = api.new_job(JobType.DISTRIBUTION, 'Job %d' % len(jobs))

    job.add_source_group(src_group, Path('source'))
    job.add_destination_group(dst_group, Path('dest'))

    job.add_trigger('post_download', Script({
        'linux': 'Linux command',
        'win': 'Windows command',
        'osx': 'OS X command'
    }))

    job.save()
    job_run = api.get_job_run(job.start())

Create consolidation job with scheduler:

.. code-block:: python

    from connect_api import ConnectApi

    api = ConnectApi('https://localhost:8443', '<API-token>')
    groups = api.get_groups()
    workstations = None
    backup_servers = None

    for g in groups:
        if g.name == 'Workstations':
            workstations = g
        elif g.name == 'Backup servers':
            backup_servers = g

    job = api.new_job(JobType.CONSOLIDATION, 'Backup job')

    source_path = Path('/var/work')
    source_path.win = 'C:\\work' # Set different path for Windows agents
    job.add_source_group(workstations, source_path)
    job.add_destination_group(backup_servers, Path('/mnt/storage'))

    job.schedule_daily(1, 0) # Run every day at 00:00

    job.save()

Start a job run from previously created job:

.. code-block:: python

    from connect_api import ConnectApi

    api = ConnectApi('https://localhost:8443', '<API-token>')
    jobs = api.get_jobs()

    for j in jobs:
        if j.name == 'Backup job':
            j.start()
            break

Get all agents and print errors:

.. code-block:: python

    from connect_api import ConnectApi

    api = ConnectApi('https://localhost:8443', '<API-token>')
    for a in api.get_agents():
        if len(a.errors):
            print(a.name)

            for e in a.errors:
                print(f'    {e["code_str"]}: {e["message"]}')
