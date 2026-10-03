"""Generated from Smithy shape ``com.amazonaws.snowball#Notification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.boolean
    import capo_snowball.types.job_state_list
    import capo_snowball.types.sns_topic_arn


class Notification(TypedDict, closed=True):
    sns_topic_arn: NotRequired["capo_snowball.types.sns_topic_arn.SnsTopicARN"]
    """<p>The new SNS <code>TopicArn</code> that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html">CreateTopic</a> Amazon SNS API action.</p> <p>You can subscribe email addresses to an Amazon SNS topic through the Amazon Web Services Management Console, or by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html">Subscribe</a> Amazon Simple Notification Service (Amazon SNS) API action.</p>"""
    job_states_to_notify: NotRequired["capo_snowball.types.job_state_list.JobStateList"]
    """<p>The list of job states that will trigger a notification for this job.</p>"""
    notify_all: "capo_snowball.types.boolean.Boolean"
    """<p>Any change in job state will trigger a notification for this job.</p>"""
    device_pickup_sns_topic_arn: NotRequired[
        "capo_snowball.types.sns_topic_arn.SnsTopicARN"
    ]
    """<p>Used to send SNS notifications for the person picking up the device (identified during job creation).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Notification) -> dict:
    out: dict = {}
    if "sns_topic_arn" in value:
        out["SnsTopicARN"] = value["sns_topic_arn"]
    if "job_states_to_notify" in value:
        import capo_snowball.types.job_state_list

        out["JobStatesToNotify"] = (
            capo_snowball.types.job_state_list.serialize_aws_json_1_1(
                value["job_states_to_notify"]
            )
        )
    out["NotifyAll"] = value.get("notify_all", False)
    if "device_pickup_sns_topic_arn" in value:
        out["DevicePickupSnsTopicARN"] = value["device_pickup_sns_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Notification:
    out: Notification = {}  # type: ignore[typeddict-item]
    if data.get("SnsTopicARN") is not None:
        out["sns_topic_arn"] = data["SnsTopicARN"]
    if data.get("JobStatesToNotify") is not None:
        import capo_snowball.types.job_state_list

        out["job_states_to_notify"] = (
            capo_snowball.types.job_state_list.deserialize_aws_json_1_1(
                data["JobStatesToNotify"]
            )
        )
    if data.get("NotifyAll") is not None:
        out["notify_all"] = data["NotifyAll"]
    else:
        out["notify_all"] = False
    if data.get("DevicePickupSnsTopicARN") is not None:
        out["device_pickup_sns_topic_arn"] = data["DevicePickupSnsTopicARN"]
    return out
