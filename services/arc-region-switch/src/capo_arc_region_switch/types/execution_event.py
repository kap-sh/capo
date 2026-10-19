"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.execution_block_type
    import capo_arc_region_switch.types.execution_event_type
    import capo_arc_region_switch.types.resources
    import capo_arc_region_switch.types.step_name


class ExecutionEvent(TypedDict, closed=True):
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp for an execution event.</p>"""
    type: NotRequired[
        "capo_arc_region_switch.types.execution_event_type.ExecutionEventType"
    ]
    """<p>The type of an execution event.</p>"""
    step_name: NotRequired["capo_arc_region_switch.types.step_name.StepName"]
    """<p>The step name for an execution event.</p>"""
    execution_block_type: NotRequired[
        "capo_arc_region_switch.types.execution_block_type.ExecutionBlockType"
    ]
    """<p>The execution block type for an execution event.</p>"""
    resources: NotRequired["capo_arc_region_switch.types.resources.Resources"]
    """<p>The resources for an execution event.</p>"""
    error: NotRequired["str"]
    """<p>Errors for an execution event.</p>"""
    description: NotRequired["str"]
    """<p>The description for an execution event.</p>"""
    event_id: "str"
    """<p>The event ID for an execution event.</p>"""
    previous_event_id: NotRequired["str"]
    """<p>The event ID of the previous execution event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionEvent) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["timestamp"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["timestamp"]
            )
        )
    if "type" in value:
        import capo_arc_region_switch.types.execution_event_type

        out["type"] = (
            capo_arc_region_switch.types.execution_event_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    if "execution_block_type" in value:
        import capo_arc_region_switch.types.execution_block_type

        out["executionBlockType"] = (
            capo_arc_region_switch.types.execution_block_type.serialize_aws_json_1_0(
                value["execution_block_type"]
            )
        )
    if "resources" in value:
        import capo_arc_region_switch.types.resources

        out["resources"] = (
            capo_arc_region_switch.types.resources.serialize_aws_json_1_0(
                value["resources"]
            )
        )
    if "error" in value:
        out["error"] = value["error"]
    if "description" in value:
        out["description"] = value["description"]
    out["eventId"] = value["event_id"]
    if "previous_event_id" in value:
        out["previousEventId"] = value["previous_event_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionEvent:
    out: ExecutionEvent = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["timestamp"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timestamp"]
            )
        )
    if data.get("type") is not None:
        import capo_arc_region_switch.types.execution_event_type

        out["type"] = (
            capo_arc_region_switch.types.execution_event_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    if data.get("executionBlockType") is not None:
        import capo_arc_region_switch.types.execution_block_type

        out["execution_block_type"] = (
            capo_arc_region_switch.types.execution_block_type.deserialize_aws_json_1_0(
                data["executionBlockType"]
            )
        )
    if data.get("resources") is not None:
        import capo_arc_region_switch.types.resources

        out["resources"] = (
            capo_arc_region_switch.types.resources.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("previousEventId") is not None:
        out["previous_event_id"] = data["previousEventId"]
    return out
