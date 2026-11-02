"""Generated from Smithy shape ``com.amazonaws.omics#RunOutputUriPrefixMode``."""

from typing import TypeAlias

"""<p>The mode controls the path prefixes that the service adds beneath <code>outputUri</code>. Valid values:</p> <ul> <li> <p> <code>SERVICE_DEFINED</code> – Adds a run-specific prefix</p> </li> <li> <p> <code>NONE_WITH_OVERWRITE</code> – Adds no prefix and overwrites existing objects at the run's output keys</p> </li> </ul>"""
RunOutputUriPrefixMode: TypeAlias = str
