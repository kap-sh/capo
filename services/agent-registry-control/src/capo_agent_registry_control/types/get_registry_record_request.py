"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#GetRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.registry_identifier


class GetRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record (ARN or ID)</p>"""
    record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to retrieve (ARN or ID)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegistryRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRegistryRecordRequest:
    out: GetRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    return out
