"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdateRegistryRecordStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_record_status


class UpdateRegistryRecordStatusRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record (ARN or ID)</p>"""
    record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to update the status of (ARN or ID)</p>"""
    status: (
        "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus"
    )
    """<p>The target status for the registry record</p>"""
    status_reason: "str"
    """<p>The reason for the status change, for example why the record was approved, rejected, or deprecated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordStatusRequest) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_record_status

    out["status"] = (
        capo_agent_registry_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordStatusRequest:
    out: UpdateRegistryRecordStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_record_status

        out["status"] = (
            capo_agent_registry_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordStatusRequest.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusRequest.status_reason required"
        )
    return out
