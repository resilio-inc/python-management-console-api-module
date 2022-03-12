Resilio Connect API python module
=================================


Examples
--------

Create group

.. code-block:: python

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

    api = ConnectApi('https://localhost:8443', '<API-token>')
    jobs = api.get_jobs()

    for j in jobs:
        if j.name == 'Backup job':
            j.start()
            break

Get all agents and print errors:

.. code-block:: python

    api = ConnectApi('https://localhost:8443', '<API-token>')
    for a in api.get_agents():
        if len(a.errors):
            print(a.name)

            for e in a.errors:
                print(f'    {e["code_str"]}: {e["message"]}')
