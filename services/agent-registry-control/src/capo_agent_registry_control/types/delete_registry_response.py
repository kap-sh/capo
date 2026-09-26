"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#DeleteRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_status


class DeleteRegistryResponse(TypedDict, closed=True):
    status: "capo_agent_registry_control.types.registry_status.RegistryStatus"
    """<p>Current status of the registry, set to DELETING when deletion is initiated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryResponse) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_status

    out["status"] = capo_agent_registry_control.types.registry_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteRegistryResponse:
    out: DeleteRegistryResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_status

        out["status"] = (
            capo_agent_registry_control.types.registry_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteRegistryResponse.status required")
    return out
