"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function revision. Possible values: <code>Pending</code> (revision is being built), <code>Active</code> (revision is ready to serve traffic), <code>Failed</code> (revision build failed).</p>"""
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
