"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#GetResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.amazon_resource_name
    import capo_pinpoint_sms_voice_v2.types.resource_policy


class GetResourcePolicyResult(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the End User Messaging SMS resource attached to the resource-based policy.</p>"""
    policy: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.resource_policy.ResourcePolicy"
    ]
    """<p>The JSON formatted string that contains the resource-based policy attached to the End User Messaging SMS resource. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time when the resource-based policy was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyResult) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "created_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyResult:
    out: GetResourcePolicyResult = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
