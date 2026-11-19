"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_target_event_context
    import capo_codepipeline.types.string
    import capo_codepipeline.types.timestamp


class DeployTargetEvent(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The name of the event for the deploy action.</p>"""
    status: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The status of the event for the deploy action.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time for the event for the deploy action.</p>"""
    end_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The end time for the event for the deploy action.</p>"""
    context: NotRequired[
        "capo_codepipeline.types.deploy_target_event_context.DeployTargetEventContext"
    ]
    """<p>The context for the event for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEvent) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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
    if "context" in value:
        import capo_codepipeline.types.deploy_target_event_context

        out["context"] = (
            capo_codepipeline.types.deploy_target_event_context.serialize_aws_json_1_1(
                value["context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployTargetEvent:
    out: DeployTargetEvent = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("context") is not None:
        import capo_codepipeline.types.deploy_target_event_context

        out["context"] = (
            capo_codepipeline.types.deploy_target_event_context.deserialize_aws_json_1_1(
                data["context"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployTargetEvent) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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
    if "context" in value:
        import capo_codepipeline.types.deploy_target_event_context

        out["context"] = (
            capo_codepipeline.types.deploy_target_event_context.serialize_cbor(
                value["context"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeployTargetEvent:
    out: DeployTargetEvent = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
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
    if data.get("context") is not None:
        import capo_codepipeline.types.deploy_target_event_context

        out["context"] = (
            capo_codepipeline.types.deploy_target_event_context.deserialize_cbor(
                data["context"]
            )
        )
    return out
