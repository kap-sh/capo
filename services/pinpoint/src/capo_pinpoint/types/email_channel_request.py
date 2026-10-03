"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string


class EmailChannelRequest(TypedDict, closed=True):
    configuration_set: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The <a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html">Amazon SES configuration set</a> that you want to apply to messages that you send through the channel.</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the email channel for the application.</p>"""
    from_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The verified email address that you want to send email from when you send email through the channel.</p>"""
    identity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that you want to use when you send email through the channel.</p>"""
    role_arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The ARN of the AWS Identity and Access Management (IAM) role that you want Amazon Pinpoint to use when it submits email-related event data for the channel.</p>"""
    orchestration_sending_role_arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The ARN of an IAM role for Amazon Pinpoint to use to send email from your campaigns or journeys through Amazon SES.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailChannelRequest) -> dict:
    out: dict = {}
    if "configuration_set" in value:
        out["ConfigurationSet"] = value["configuration_set"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "orchestration_sending_role_arn" in value:
        out["OrchestrationSendingRoleArn"] = value["orchestration_sending_role_arn"]
    return out


def deserialize_json(data: dict) -> EmailChannelRequest:
    out: EmailChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSet") is not None:
        out["configuration_set"] = data["ConfigurationSet"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("OrchestrationSendingRoleArn") is not None:
        out["orchestration_sending_role_arn"] = data["OrchestrationSendingRoleArn"]
    return out
