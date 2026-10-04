"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function. Possible values: <code>Pending</code> (function is being created), <code>Active</code> (function is ready to use), <code>Failed</code> (function creation or update failed), <code>Deleting</code> (function is being deleted).</p>"""
FunctionState: TypeAlias = Literal[
    "Pending",
    "Active",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionState) -> str:
    return value


def deserialize_json(data: str) -> FunctionState:
    return cast(FunctionState, data)
