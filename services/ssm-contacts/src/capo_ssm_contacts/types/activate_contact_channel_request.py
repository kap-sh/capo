"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ActivateContactChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.activation_code
    import capo_ssm_contacts.types.ssm_contacts_arn


class ActivateContactChannelRequest(TypedDict, closed=True):
    contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""
    activation_code: "capo_ssm_contacts.types.activation_code.ActivationCode"
    """<p>The code sent to the contact channel when it was created in the contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    out["ActivationCode"] = value["activation_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivateContactChannelRequest:
    out: ActivateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelId") is not None:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        out["contact_channel_id"] = ""
    if data.get("ActivationCode") is not None:
        out["activation_code"] = data["ActivationCode"]
    else:
        out["activation_code"] = ""
    return out
