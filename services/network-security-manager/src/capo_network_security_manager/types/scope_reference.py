"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ScopeReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_identifier


class ScopeReference(TypedDict, closed=True):
    scope_identifier: (
        "capo_network_security_manager.types.scope_identifier.ScopeIdentifier"
    )
    """<p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeReference) -> dict:
    out: dict = {}
    out["scopeIdentifier"] = value["scope_identifier"]
    return out


def deserialize_json(data: dict) -> ScopeReference:
    out: ScopeReference = {}  # type: ignore[typeddict-item]
    if data.get("scopeIdentifier") is not None:
        out["scope_identifier"] = data["scopeIdentifier"]
    else:
        raise DeserializationError("ScopeReference.scope_identifier required")
    return out
