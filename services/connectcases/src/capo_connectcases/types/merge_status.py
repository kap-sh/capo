"""Generated from Smithy shape ``com.amazonaws.connectcases#MergeStatus``."""

from typing import TypeAlias

"""<p>The merge status of a case.</p> <ul> <li> <p> <code>IN_PROGRESS</code> - The merge is running. You can't modify the secondary case or its related items. You can modify the primary case, but you can't delete it.</p> </li> <li> <p> <code>COMPLETED</code> - The merge finished, and this case was the secondary case. The case was closed by the merge. You can reopen, update, and delete it, but you can't include it in another merge.</p> </li> </ul>"""
MergeStatus: TypeAlias = str
