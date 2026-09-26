"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#GetRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_identifier


class GetRegistryRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to retrieve (ARN or ID)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRegistryRequest:
    out: GetRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
