import os

curpath = os.path.realpath(__file__)
basepath = curpath
while os.path.split(basepath)[1] != 'source':
    newpath = os.path.split(basepath)[0]
    if newpath == basepath:
        print("ERROR: unable to find source from path "+curpath)
        break
    basepath = os.path.split(basepath)[0]
RESPATH = os.path.join(os.path.split(basepath)[0], "resources")


def res_path(path):
        return os.path.join(RESPATH, path)


def list_files(basedir):
    """
    Provide a list of all paths of all files recursively included in some of the
    base directories provided in basedir
    :param basedir: An arbitrarily nested list of files and folders to consider
    :return: a list of paths of files included in some directory in the input list
    """
    rets = []
    if not isinstance(basedir, str):
        for d in basedir:
            rets.extend(list_files(d))
        return rets

    if not os.path.isdir(basedir):
        return [basedir]

    subelems = [os.path.join(basedir, f) for f in os.listdir(basedir)]
    for f in subelems:
        rets.extend(list_files(f))
    return rets
