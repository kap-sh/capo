"""Generated from Smithy shape ``com.amazonaws.elementalinference#FunctionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a function.</p> <ul> <li> <p>CREATING – CreateFunction returns this status. The function is ready to use as soon as the request succeeds. </p> </li> <li> <p>AVAILABLE – No feed references the function. Every property can be changed, and the function can be deleted. </p> </li> <li> <p>REFERENCED – At least one feed references the function, so the function can't be deleted. Only the expressions and the description can be changed, and eventBridgeDelivery can be set to DISABLED but not to ENABLED. The request expression must keep referencing the same media context. </p> </li> <li> <p>DELETING – DeleteFunction returns this status. The function is removed as soon as the request succeeds. </p> </li> <li> <p>DELETED – Not currently returned.</p> </li> </ul>"""
FunctionStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "REFERENCED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionStatus) -> str:
    return value


def deserialize_json(data: str) -> FunctionStatus:
    return cast(FunctionStatus, data)
