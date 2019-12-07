__version_info__ = (1, 3, 0, 'final', 0)


def get_version():
    version = '{}.{}'.format(__version_info__[0], __version_info__[1])
    if __version_info__[2]:
        version = '{}.{}'.format(version, __version_info__[2])
    if __version_info__[3] != 'final':
        version = '{}{}'.format(version, __version_info__[3])
        if __version_info__[4]:
            version = '{}{}'.format(version, __version_info__[4])
    return version


__version__ = get_version()
