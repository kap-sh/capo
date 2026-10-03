"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.operation_event_status
    import capo_ssm_sap.types.resource


class OperationEvent(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the operation event. For example, "Stop the EC2 instance i-abcdefgh987654321".</p>"""
    resource: NotRequired["capo_ssm_sap.types.resource.Resource"]
    """<p>The resource involved in the operations event.</p> <p>Contains <code>ResourceArn</code> ARN and <code>ResourceType</code>.</p>"""
    status: NotRequired[
        "capo_ssm_sap.types.operation_event_status.OperationEventStatus"
    ]
    """<p>The status of the operation event. The possible statuses are: <code>IN_PROGRESS</code>, <code>COMPLETED</code>, and <code>FAILED</code>.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message relating to a specific operation event.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of the specified operation event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OperationEvent) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "resource" in value:
        import capo_ssm_sap.types.resource

        out["Resource"] = capo_ssm_sap.types.resource.serialize_json(value["resource"])
    if "status" in value:
        import capo_ssm_sap.types.operation_event_status

        out["Status"] = capo_ssm_sap.types.operation_event_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "timestamp" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["Timestamp"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> OperationEvent:
    out: OperationEvent = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Resource") is not None:
        import capo_ssm_sap.types.resource

        out["resource"] = capo_ssm_sap.types.resource.deserialize_json(data["Resource"])
    if data.get("Status") is not None:
        import capo_ssm_sap.types.operation_event_status

        out["status"] = capo_ssm_sap.types.operation_event_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Timestamp") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["timestamp"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["Timestamp"]
        )
    return out
