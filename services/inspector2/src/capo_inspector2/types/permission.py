"""Generated from Smithy shape ``com.amazonaws.inspector2#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.operation
    import capo_inspector2.types.service


class Permission(TypedDict, closed=True):
    service: "capo_inspector2.types.service.Service"
    """<p>The services that the permissions allow an account to perform the given operations for.</p>"""
    operation: "capo_inspector2.types.operation.Operation"
    """<p>The operations that can be performed with the given permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> dict:
    out: dict = {}
    out["service"] = value["service"]
    out["operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    else:
        out["operation"] = ""
    return out
