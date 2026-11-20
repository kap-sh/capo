"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MessageText``."""

from typing import TypeAlias

"""<p>The text of a single turn. It must be well-formed Unicode: text that contains an unpaired UTF-16 surrogate fails with <code>ValidationException</code>.</p> <p>There is no separate limit for one turn. A single turn can use the whole event limit of 5 MiB of UTF-8 text across all turns, and the service splits long turns itself.</p>"""
MessageText: TypeAlias = str
