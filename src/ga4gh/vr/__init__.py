# flake8: noqa
"""Public interface to the GA4GH Variation Representation reference
implementation

"""


__all__ = """ga4gh_identify ga4gh_serialize models normalize   schema_path""".split()


import warnings
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:    # pragma: nocover
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


from bioutils.normalize import normalize
from ga4gh.core import ga4gh_digest, ga4gh_identify, ga4gh_serialize
from ._internal.models import models, schema_path
