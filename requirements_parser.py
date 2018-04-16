import pip

if pip.__version__ < "10.0.0":
    from pip.req import parse_requirements
    from pip.download import PipSession
else:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession


def parse(filepath):
    """Returns a list of strings with the requirments registered in the file"""
    requirements = parse_requirements(filepath, session=PipSession())
    return [str(ir.req) for ir in requirements]
