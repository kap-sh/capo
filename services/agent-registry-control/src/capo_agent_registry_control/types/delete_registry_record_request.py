"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#DeleteRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.registry_identifier


class DeleteRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record (ARN or ID)</p>"""
    record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to delete (ARN or ID)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRegistryRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRegistryRecordRequest:
    out: DeleteRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    return out
