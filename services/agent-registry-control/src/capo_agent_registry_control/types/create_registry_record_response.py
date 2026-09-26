"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CreateRegistryRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_record_arn
    import capo_agent_registry_control.types.registry_record_status


class CreateRegistryRecordResponse(TypedDict, closed=True):
    record_arn: (
        "capo_agent_registry_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The ARN of the created registry record</p>"""
    status: (
        "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus"
    )
    """<p>The status of the registry record, set to CREATING while the asynchronous workflow is in progress</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRecordResponse) -> dict:
    out: dict = {}
    out["recordArn"] = value["record_arn"]
    import capo_agent_registry_control.types.registry_record_status

    out["status"] = (
        capo_agent_registry_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateRegistryRecordResponse:
    out: CreateRegistryRecordResponse = {}  # type: ignore[typeddict-item]
    if data.get("recordArn") is not None:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("CreateRegistryRecordResponse.record_arn required")
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_record_status

        out["status"] = (
            capo_agent_registry_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateRegistryRecordResponse.status required")
    return out
