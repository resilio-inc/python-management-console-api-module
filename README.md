# Resilio Connect API python module


## Installation

1. Clone the repository
```
git clone git@github.com:bt-sync/connect-api.git
```

2. Install the module
```
sudo pip install ./connect-api
```

## Examples

Create distribution job

```python
api = ConnectApi('https://localhost:8443', '<API-token>')
agents = api.get_agents()

src_group = api.create_group('src.group', [agents[0]])
dst_group = api.create_group('dst.group', agents[1:])

job = api.new_job(JobType.DISTRIBUTION, 'Job %d' % len(jobs))

job.add_source_group(src_group, Path('source'))
job.add_destination_group(dst_group, Path('dest'))

job.add_trigger('post_download', {
    'linux': 'Linux command',
    'win': 'Windows command',
    'osx': 'OS X command'
})

job.save()
```