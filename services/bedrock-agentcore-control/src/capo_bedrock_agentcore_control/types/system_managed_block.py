"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SystemManagedBlock``."""

from typing_extensions import TypedDict


class SystemManagedBlock(TypedDict, closed=True):
    managed_by: "str"
    """<p>The identifier of the system or process that manages this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemManagedBlock) -> dict:
    out: dict = {}
    out["managedBy"] = value["managed_by"]
    return out


def deserialize_json(data: dict) -> SystemManagedBlock:
    out: SystemManagedBlock = {}  # type: ignore[typeddict-item]
    if data.get("managedBy") is not None:
        out["managed_by"] = data["managedBy"]
    else:
        out["managed_by"] = ""
    return out
