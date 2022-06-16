##
# @brief try import package, install if not found
# @param package       package name, str
# @param install_name  (optional) name of package when installed with pip
def import_install(package, install_name=None):
    if install_name is None:
        install_name = package
    global pkg__
    pkg__ = None
    exec(f"try: \n"
         f"    import {package}\n"
         f"    global pkg__\n"
         f"    pkg__ = {package}\n"
         f"except: pass")
    if pkg__ is not None:
        return pkg__
    print(f"[INFO] {package} is not installed - installing it")
    from pip._internal import main as pipmain
    pipmain(['install', install_name])
    exec(f"try: \n"
         f"    import {package}\n"
         f"    global pkg__\n"
         f"    pkg__ = {package}\n"
         f"except: pass")
    if pkg__ is None:
        raise(RuntimeError(f"[ERROR] {install_name} could not be installed"))
    return pkg__
