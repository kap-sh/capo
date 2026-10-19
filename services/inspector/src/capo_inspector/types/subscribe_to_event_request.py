"""Generated from Smithy shape ``com.amazonaws.inspector#SubscribeToEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.inspector_event


class SubscribeToEventRequest(TypedDict, closed=True):
    resource_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.</p>"""
    event: "capo_inspector.types.inspector_event.InspectorEvent"
    """<p>The event for which you want to receive SNS notifications.</p>"""
    topic_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the SNS topic to which the SNS notifications are sent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToEventRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_inspector.types.inspector_event

    out["event"] = capo_inspector.types.inspector_event.serialize_aws_json_1_1(
        value["event"]
    )
    out["topicArn"] = value["topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribeToEventRequest:
    out: SubscribeToEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("event") is not None:
        import capo_inspector.types.inspector_event

        out["event"] = capo_inspector.types.inspector_event.deserialize_aws_json_1_1(
            data["event"]
        )
    else:
        import typing

        out["event"] = typing.cast(
            "capo_inspector.types.inspector_event.InspectorEvent", ""
        )
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    else:
        out["topic_arn"] = ""
    return out
