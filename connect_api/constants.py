from enum import Enum


class Permission(Enum):
    READ_ONLY = 'ro'
    DESTINATION = 'ro'
    READ_WRITE = 'rw'
    SOURCE = 'rw'
    SELECTIVE_RO = 'sro'
    SELECTIVE_RW = 'srw'


class JobType(Enum):
    SYNC = 'sync'
    DISTRIBUTION = 'distribution'
    CONSOLIDATION = 'consolidation'
    SCRIPT = 'script'


class SchedulerType(Enum):
    NOW = 'now'
    ONCE = 'once'
    MANUALLY = 'manually'
    HOURLY = 'hourly'
    DAILY = 'daily'
    WEEKLY = 'weekly'


class JobStatus(Enum):
    SYNCED = 'synced'
    IN_PROGRESS = 'in-progress'
    INDEXING = 'indexing'