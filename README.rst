Resilio Connect API python module
=================================


Examples
--------

Create distribution job:

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
