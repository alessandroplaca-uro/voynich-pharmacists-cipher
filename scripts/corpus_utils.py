# Compatibility shim: re-export everything from 00_corpus_utils
from importlib.util import spec_from_file_location, module_from_spec
import pathlib, sys

_here = pathlib.Path(__file__).parent
_spec = spec_from_file_location("_corpus_utils_impl", _here / "00_corpus_utils.py")
_mod  = module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Expose all public names
for _name in dir(_mod):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_mod, _name)
