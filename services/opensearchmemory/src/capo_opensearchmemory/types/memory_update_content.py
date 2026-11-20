"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MemoryUpdateContent``."""

from typing import TypeAlias

"""<p>Replacement text for a memory, at most about 6,000 tokens. It must not be blank and must be well-formed Unicode. Longer text fails with <code>ValidationException</code>.</p>"""
MemoryUpdateContent: TypeAlias = str
