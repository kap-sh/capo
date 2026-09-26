"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_arn


class AssociatedScope(TypedDict, closed=True):
    scope_arn: "capo_network_security_manager.types.scope_arn.ScopeArn"
    """<p>The ARN of the associated scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedScope) -> dict:
    out: dict = {}
    out["scopeArn"] = value["scope_arn"]
    return out


def deserialize_json(data: dict) -> AssociatedScope:
    out: AssociatedScope = {}  # type: ignore[typeddict-item]
    if data.get("scopeArn") is not None:
        out["scope_arn"] = data["scopeArn"]
    else:
        raise DeserializationError("AssociatedScope.scope_arn required")
    return out
