from connexion import NoContent

import ga4gh.vr


def search():
    rv = {
        "ga4gh.vr": {
            "version": ga4gh.vr.__version__
        },
    }

    return rv, 200
