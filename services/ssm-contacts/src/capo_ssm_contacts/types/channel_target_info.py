"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ChannelTargetInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.retry_interval_in_minutes
    import capo_ssm_contacts.types.ssm_contacts_arn


class ChannelTargetInfo(TypedDict, closed=True):
    contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""
    retry_interval_in_minutes: NotRequired[
        "capo_ssm_contacts.types.retry_interval_in_minutes.RetryIntervalInMinutes"
    ]
    """<p>The number of minutes to wait before retrying to send engagement if the engagement initially failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelTargetInfo) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    if "retry_interval_in_minutes" in value:
        out["RetryIntervalInMinutes"] = value["retry_interval_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelTargetInfo:
    out: ChannelTargetInfo = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelId") is not None:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        out["contact_channel_id"] = ""
    if data.get("RetryIntervalInMinutes") is not None:
        out["retry_interval_in_minutes"] = data["RetryIntervalInMinutes"]
    return out
