from connexion import NoContent

from ..globals import get_manager


def put(body):
    pass

#    request = body
#    defn = request.pop("definition")
#    fmt = request.pop("format")
#
#    messages = []
#
#    m = get_manager()
#    a = m.translate_allele(defn=defn, fmt=fmt)
#    m.add_allele(a)
#    
#    result = {
#        "messages": messages,
#        "data": a.as_dict(),
#    }
#    
#    return result, 200
