#!/usr/bin/env python3

import json
import time

import context
from connect_api import ConnectApi, Path


api = ConnectApi('http://localhost:8080', 'AAA')
agents = api.get_agents()


src_group = api.create_group('src.group', [agents[0]])
dst_group = api.create_group('dst.group', agents[1:])
print(src_group.attrs)

jobs = api.get_jobs()

job = api.new_job(JobType.DISTRIBUTION, 'Job %d' % len(jobs)) 
job.add_source_group(src_group, Path('source'))
job.add_destination_group(dst_group, Path('dest'))

job.add_trigger('post_download', {
    'linux': 'Linux',
    'win': 'Windows',
    'osx': 'OS X'
})

# job = jobs[0]
# print(job.attrs)
# job.add_trigger('post_download', None)

job.save()

print(job.attrs)
