"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionNumericalVersion``."""

from typing import TypeAlias

"""<p>A retrieval instruction version number: at most nine digits (1 to 999,999,999). Numbers are allocated monotonically from 1 and never reused, even after the version is deleted, so the shape also bounds the lifetime number of versions an instruction can ever allocate.</p>"""
RetrievalInstructionNumericalVersion: TypeAlias = str
