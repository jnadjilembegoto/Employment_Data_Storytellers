import os# utiliser pour le chemin d'accès

def data_dir(script_path):
    main=os.path.dirname(__file__)
    return  os.path.join(main, script_path)
