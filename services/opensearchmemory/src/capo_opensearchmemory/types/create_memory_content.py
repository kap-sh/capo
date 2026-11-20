"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateMemoryContent``."""

from typing import TypeAlias

"""<p>The memory text for <code>CreateMemory</code>: 1 to 16,000 characters and at most about 6,000 tokens, not blank, and well-formed Unicode. Longer text fails with <code>ValidationException</code>.</p>"""
CreateMemoryContent: TypeAlias = str
