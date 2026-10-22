"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionVersionSelector``."""

from typing import TypeAlias

"""<p>A version selector for a retrieval instruction: a version number, or DRAFT for the retrieval instruction's current reviewed content. Version numbers are 1 to 999,999,999 (at most nine digits, no leading zeros) — the same number space as RetrievalInstructionNumericalVersion.</p>"""
RetrievalInstructionVersionSelector: TypeAlias = str
