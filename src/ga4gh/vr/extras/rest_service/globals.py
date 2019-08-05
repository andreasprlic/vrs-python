"""Runtime globals (really, thread locals)

Items created here are singletons within the thread

"""

import logging
import os

from flask import current_app

import ga4gh.vr
from ga4gh.vr.extras.translator import Translator
from ga4gh.vr.extras.dataproxy import SeqRepoRESTDataProxy


_logger = logging.getLogger(__name__)

seqrepo_rest_service_url = "http://localhost:5000/seqrepo"



def _get_g(k, fn):
    """fetch a global singleton, creating with `fn` on first invocation"""
    v = getattr(current_app, k, None)
    if not v:
        v = fn()
        setattr(current_app, k, v)
    return v


def _create_Translator():
    dp = SeqRepoRESTDataProxy(base_url=seqrepo_rest_service_url)
    return Translator(data_proxy=dp)

def get_translator():
    return _get_g("_vr_translator", _create_Translator)





    
