from warnings import WarningMessage


try:
    import torch
except ModuleNotFoundError:
    WarningMessage("pytorch not installed, skip")