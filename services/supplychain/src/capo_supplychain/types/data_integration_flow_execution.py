"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.data_integration_flow_execution_output_metadata
    import capo_supplychain.types.data_integration_flow_execution_source_info
    import capo_supplychain.types.data_integration_flow_execution_status
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.uuid


class DataIntegrationFlowExecution(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The flow execution's instanceId.</p>"""
    flow_name: (
        "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    )
    """<p>The flow execution's flowName.</p>"""
    execution_id: "capo_supplychain.types.uuid.UUID"
    """<p>The flow executionId.</p>"""
    status: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_status.DataIntegrationFlowExecutionStatus"
    ]
    """<p>The status of flow execution.</p>"""
    source_info: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_source_info.DataIntegrationFlowExecutionSourceInfo"
    ]
    """<p>The source information for a flow execution.</p>"""
    message: NotRequired["str"]
    """<p>The failure message (if any) of failed flow execution.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The flow execution start timestamp.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The flow execution end timestamp.</p>"""
    output_metadata: NotRequired[
        "capo_supplychain.types.data_integration_flow_execution_output_metadata.DataIntegrationFlowExecutionOutputMetadata"
    ]
    """<p>The flow execution output metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecution) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["flowName"] = value["flow_name"]
    out["executionId"] = value["execution_id"]
    if "status" in value:
        import capo_supplychain.types.data_integration_flow_execution_status

        out["status"] = (
            capo_supplychain.types.data_integration_flow_execution_status.serialize_json(
                value["status"]
            )
        )
    if "source_info" in value:
        import capo_supplychain.types.data_integration_flow_execution_source_info

        out["sourceInfo"] = (
            capo_supplychain.types.data_integration_flow_execution_source_info.serialize_json(
                value["source_info"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "start_time" in value:
        import capo_supplychain.types._prelude.timestamp

        out["startTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_supplychain.types._prelude.timestamp

        out["endTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "output_metadata" in value:
        import capo_supplychain.types.data_integration_flow_execution_output_metadata

        out["outputMetadata"] = (
            capo_supplychain.types.data_integration_flow_execution_output_metadata.serialize_json(
                value["output_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowExecution:
    out: DataIntegrationFlowExecution = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("status") is not None:
        import capo_supplychain.types.data_integration_flow_execution_status

        out["status"] = (
            capo_supplychain.types.data_integration_flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("sourceInfo") is not None:
        import capo_supplychain.types.data_integration_flow_execution_source_info

        out["source_info"] = (
            capo_supplychain.types.data_integration_flow_execution_source_info.deserialize_json(
                data["sourceInfo"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("startTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["start_time"] = capo_supplychain.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["end_time"] = capo_supplychain.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("outputMetadata") is not None:
        import capo_supplychain.types.data_integration_flow_execution_output_metadata

        out["output_metadata"] = (
            capo_supplychain.types.data_integration_flow_execution_output_metadata.deserialize_json(
                data["outputMetadata"]
            )
        )
    return out
