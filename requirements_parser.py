import pip

if pip.__version__ < "10.0.0":
    from pip.req import parse_requirements
    from pip.download import PipSession
else:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession


def parse(filepath, links=False):
    """Returns a list of strings with the requirments registered in the file"""
    requirements = []
    for lib in parse_requirements(filepath, session=PipSession()):
        if links:
            if hasattr(lib.link, 'url'):
                requirements.append(lib.link.url)
        elif lib.req is not None:
            requirements.append(str(lib.req))
    return requirements
