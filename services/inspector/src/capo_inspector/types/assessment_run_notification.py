"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunNotification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_run_notification_sns_status_code
    import capo_inspector.types.bool
    import capo_inspector.types.inspector_event
    import capo_inspector.types.message
    import capo_inspector.types.timestamp


class AssessmentRunNotification(TypedDict, closed=True):
    date: "capo_inspector.types.timestamp.Timestamp"
    """<p>The date of the notification.</p>"""
    event: "capo_inspector.types.inspector_event.InspectorEvent"
    """<p>The event for which a notification is sent.</p>"""
    message: NotRequired["capo_inspector.types.message.Message"]
    """<p>The message included in the notification.</p>"""
    error: "capo_inspector.types.bool.Bool"
    """<p>The Boolean value that specifies whether the notification represents an error.</p>"""
    sns_topic_arn: NotRequired["capo_inspector.types.arn.Arn"]
    """<p>The SNS topic to which the SNS notification is sent.</p>"""
    sns_publish_status_code: NotRequired[
        "capo_inspector.types.assessment_run_notification_sns_status_code.AssessmentRunNotificationSnsStatusCode"
    ]
    """<p>The status code of the SNS notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunNotification) -> dict:
    out: dict = {}
    import capo_inspector.types.timestamp

    out["date"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(value["date"])
    import capo_inspector.types.inspector_event

    out["event"] = capo_inspector.types.inspector_event.serialize_aws_json_1_1(
        value["event"]
    )
    if "message" in value:
        out["message"] = value["message"]
    out["error"] = value["error"]
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    if "sns_publish_status_code" in value:
        import capo_inspector.types.assessment_run_notification_sns_status_code

        out["snsPublishStatusCode"] = (
            capo_inspector.types.assessment_run_notification_sns_status_code.serialize_aws_json_1_1(
                value["sns_publish_status_code"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunNotification:
    out: AssessmentRunNotification = {}  # type: ignore[typeddict-item]
    if data.get("date") is not None:
        import capo_inspector.types.timestamp

        out["date"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["date"]
        )
    else:
        import datetime

        out["date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    else:
        out["error"] = False
    if data.get("snsTopicArn") is not None:
        out["sns_topic_arn"] = data["snsTopicArn"]
    if data.get("snsPublishStatusCode") is not None:
        import capo_inspector.types.assessment_run_notification_sns_status_code

        out["sns_publish_status_code"] = (
            capo_inspector.types.assessment_run_notification_sns_status_code.deserialize_aws_json_1_1(
                data["snsPublishStatusCode"]
            )
        )
    return out
