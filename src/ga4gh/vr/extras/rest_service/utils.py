def filter_dict(d):
    try:
        return {k: filter_dict(d[k])
                for k in d
                if not k.startswith("_")}
    except:
        return d
    
