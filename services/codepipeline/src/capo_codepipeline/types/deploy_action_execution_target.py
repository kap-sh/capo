"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployActionExecutionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_target_event_list
    import capo_codepipeline.types.string
    import capo_codepipeline.types.timestamp


class DeployActionExecutionTarget(TypedDict, closed=True):
    target_id: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The ID of the target for the deploy action.</p>"""
    target_type: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The type of target for the deploy action.</p>"""
    status: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The status of the deploy action.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time for the deploy action.</p>"""
    end_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The end time for the deploy action.</p>"""
    events: NotRequired[
        "capo_codepipeline.types.deploy_target_event_list.DeployTargetEventList"
    ]
    """<p>The lifecycle events for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployActionExecutionTarget) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_type" in value:
        out["targetType"] = value["target_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codepipeline.types.timestamp

        out["endTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "events" in value:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = (
            capo_codepipeline.types.deploy_target_event_list.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployActionExecutionTarget:
    out: DeployActionExecutionTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    if data.get("targetType") is not None:
        out["target_type"] = data["targetType"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("startTime") is not None:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codepipeline.types.timestamp

        out["end_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("events") is not None:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = (
            capo_codepipeline.types.deploy_target_event_list.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployActionExecutionTarget) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_type" in value:
        out["targetType"] = value["target_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codepipeline.types.timestamp

        out["endTime"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "events" in value:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = capo_codepipeline.types.deploy_target_event_list.serialize_cbor(
            value["events"]
        )
    return out


def deserialize_cbor(data: dict) -> DeployActionExecutionTarget:
    out: DeployActionExecutionTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    if data.get("targetType") is not None:
        out["target_type"] = data["targetType"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("startTime") is not None:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codepipeline.types.timestamp

        out["end_time"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["endTime"]
        )
    if data.get("events") is not None:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = (
            capo_codepipeline.types.deploy_target_event_list.deserialize_cbor(
                data["events"]
            )
        )
    return out
