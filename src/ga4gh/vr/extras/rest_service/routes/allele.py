from connexion import NoContent

from ga4gh.core import ga4gh_identify

from ..globals import get_translator
from ..utils import filter_dict


def put(body):
    request = body
    defn = request.pop("definition")
    fmt = request.pop("format")

    messages = []

    tlr = get_translator()
    a = tlr.from_hgvs(defn)
    
    data = filter_dict(a.as_dict())
    data["id"] = ga4gh_identify(a)

    result = {
        "messages": messages,
        "data": data
    }
    
    return result, 200
