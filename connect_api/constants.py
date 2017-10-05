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


class AgentOS:
    WIN32 = 'win32'
    WIN64 = 'win64'
    MAC = 'mac'
    LINUX = 'linux'
    ANDROID = 'android'
    IOS = 'iOS'
    WINDOWS_PHONE = 'Wp8'

    @classmethod
    def is_windows(cls, os):
        return os in [cls.WIN64, cls.WIN32]

    @classmethod
    def is_linux(cls, os):
        return os == cls.LINUX

    @classmethod
    def is_mac(cls, os):
        return os == cls.MAC

    @classmethod
    def is_mobile(cls, os):
        return os in [cls.ANDROID, cls.IOS, cls.WINDOWS_PHONE]
