"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowStep``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.flow_name
    import capo_customer_profiles.types.long
    import capo_customer_profiles.types.status
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.timestamp


class AppflowIntegrationWorkflowStep(TypedDict, closed=True):
    flow_name: "capo_customer_profiles.types.flow_name.FlowName"
    """<p>Name of the flow created during execution of workflow step. <code>APPFLOW_INTEGRATION</code> workflow type creates an appflow flow during workflow step execution on the customers behalf.</p>"""
    status: "capo_customer_profiles.types.status.Status"
    """<p>Workflow step status for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    execution_message: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Message indicating execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    records_processed: "capo_customer_profiles.types.long.long"
    """<p>Total number of records processed during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    batch_records_start_time: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Start datetime of records pulled in batch during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    batch_records_end_time: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>End datetime of records pulled in batch during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Creation timestamp of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Last updated timestamp for workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowStep) -> dict:
    out: dict = {}
    out["FlowName"] = value["flow_name"]
    import capo_customer_profiles.types.status

    out["Status"] = capo_customer_profiles.types.status.serialize_json(value["status"])
    out["ExecutionMessage"] = value["execution_message"]
    out["RecordsProcessed"] = value.get("records_processed", 0)
    out["BatchRecordsStartTime"] = value["batch_records_start_time"]
    out["BatchRecordsEndTime"] = value["batch_records_end_time"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowStep:
    out: AppflowIntegrationWorkflowStep = {}  # type: ignore[typeddict-item]
    if data.get("FlowName") is not None:
        out["flow_name"] = data["FlowName"]
    else:
        out["flow_name"] = ""
    if data.get("Status") is not None:
        import capo_customer_profiles.types.status

        out["status"] = capo_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_customer_profiles.types.status.Status", "")
    if data.get("ExecutionMessage") is not None:
        out["execution_message"] = data["ExecutionMessage"]
    else:
        out["execution_message"] = ""
    if data.get("RecordsProcessed") is not None:
        out["records_processed"] = data["RecordsProcessed"]
    else:
        out["records_processed"] = 0
    if data.get("BatchRecordsStartTime") is not None:
        out["batch_records_start_time"] = data["BatchRecordsStartTime"]
    else:
        out["batch_records_start_time"] = ""
    if data.get("BatchRecordsEndTime") is not None:
        out["batch_records_end_time"] = data["BatchRecordsEndTime"]
    else:
        out["batch_records_end_time"] = ""
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
