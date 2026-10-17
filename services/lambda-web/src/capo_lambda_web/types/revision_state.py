"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function revision. Possible values:</p> <ul> <li> <p> <code>Pending</code> – The revision is being built.</p> </li> <li> <p> <code>Active</code> – The revision is ready to serve traffic.</p> </li> <li> <p> <code>Failed</code> – The revision build failed.</p> </li> </ul>"""
RevisionState: TypeAlias = Literal[
    "Pending",
    "Active",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: RevisionState) -> str:
    return value


def deserialize_json(data: str) -> RevisionState:
    return cast(RevisionState, data)
