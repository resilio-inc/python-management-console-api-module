class Permission:
    READ_ONLY = 'ro'
    DESTINATION = 'ro'
    READ_WRITE = 'rw'
    SOURCE = 'rw'
    SELECTIVE_RO = 'sro'
    SELECTIVE_RW = 'srw'


class JobType:
    SYNC = 'sync'
    DISTRIBUTION = 'distribution'
    CONSOLIDATION = 'consolidation'
    SCRIPT = 'script'


class SchedulerType:
    NOW = 'now'
    ONCE = 'once'
    MANUALLY = 'manually'
    HOURLY = 'hourly'
    DAILY = 'daily'
    WEEKLY = 'weekly'


class JobStatus:
    SYNCED = 'synced'
    IN_PROGRESS = 'in-progress'
    INDEXING = 'indexing'
    ERROR = 'error'