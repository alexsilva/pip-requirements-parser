import pip

_pip_version = pip.__version__

if _pip_version < "10.0.0":
    from pip.req import parse_requirements
    from pip.download import PipSession
elif _pip_version < "20.0.0":
    from pip._internal.req import parse_requirements
    from pip._internal.req import PipSession
else:
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession


def parse(filepath, links=False):
    """Returns a list of strings with the requirments registered in the file"""
    requirements = []
    for lib in parse_requirements(filepath, session=PipSession()):
        if links and hasattr(lib.link, 'url'):
            requirements.append(lib.link.url)
        elif lib.req is not None:
            requirements.append(str(lib.req))
    return requirements
