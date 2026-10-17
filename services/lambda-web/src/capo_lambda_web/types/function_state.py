"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a web function. Possible values:</p> <ul> <li> <p> <code>Pending</code> – The function is being created.</p> </li> <li> <p> <code>Active</code> – The function is ready to use.</p> </li> <li> <p> <code>Failed</code> – Function creation or update failed.</p> </li> <li> <p> <code>Deleting</code> – The function is being deleted.</p> </li> </ul>"""
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
