"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdateRegistryRecordStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.date_timestamp
    import capo_agent_registry_control.types.registry_arn
    import capo_agent_registry_control.types.registry_record_arn
    import capo_agent_registry_control.types.registry_record_id
    import capo_agent_registry_control.types.registry_record_status


class UpdateRegistryRecordStatusResponse(TypedDict, closed=True):
    registry_arn: "capo_agent_registry_control.types.registry_arn.RegistryArn"
    """<p>The ARN of the registry</p>"""
    record_arn: (
        "capo_agent_registry_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The ARN of the registry record</p>"""
    record_id: "capo_agent_registry_control.types.registry_record_id.RegistryRecordId"
    """<p>The ID of the registry record</p>"""
    status: (
        "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus"
    )
    """<p>The resulting status of the registry record</p>"""
    status_reason: "str"
    """<p>The reason for the status change</p>"""
    updated_at: "capo_agent_registry_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the record was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordStatusResponse) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    import capo_agent_registry_control.types.registry_record_status

    out["status"] = (
        capo_agent_registry_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    out["statusReason"] = value["status_reason"]
    import capo_agent_registry_control.types.date_timestamp

    out["updatedAt"] = capo_agent_registry_control.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordStatusResponse:
    out: UpdateRegistryRecordStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusResponse.registry_arn required"
        )
    if data.get("recordArn") is not None:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusResponse.record_arn required"
        )
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusResponse.record_id required"
        )
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_record_status

        out["status"] = (
            capo_agent_registry_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordStatusResponse.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusResponse.status_reason required"
        )
    if data.get("updatedAt") is not None:
        import capo_agent_registry_control.types.date_timestamp

        out["updated_at"] = (
            capo_agent_registry_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRegistryRecordStatusResponse.updated_at required"
        )
    return out
