"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.scope_identifier


class GetScopeInput(TypedDict, closed=True):
    scope_identifier: (
        "capo_network_security_manager.types.scope_identifier.ScopeIdentifier"
    )
    """<p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScopeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetScopeInput:
    out: GetScopeInput = {}  # type: ignore[typeddict-item]
    return out
