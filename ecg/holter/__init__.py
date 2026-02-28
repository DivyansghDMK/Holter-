"""
ecg/holter/__init__.py
Public API for the Holter recording subsystem.
"""

from .file_format import ECGHFileWriter, ECGHFileReader
from .stream_writer import HolterStreamWriter
from .analysis_worker import HolterAnalysisWorker
from .replay_engine import HolterReplayEngine
from .report_generator import generate_holter_report

# UI components — only importable when PyQt5 is available
try:
    from .holter_ui import (
        HolterStartDialog,
        HolterStatusBar,
        HolterMainWindow,
    )
    _UI_AVAILABLE = True
except ImportError:
    _UI_AVAILABLE = False

__all__ = [
    "ECGHFileWriter", "ECGHFileReader",
    "HolterStreamWriter", "HolterAnalysisWorker",
    "HolterReplayEngine", "generate_holter_report",
]
if _UI_AVAILABLE:
    __all__ += ["HolterStartDialog", "HolterStatusBar", "HolterMainWindow"]
