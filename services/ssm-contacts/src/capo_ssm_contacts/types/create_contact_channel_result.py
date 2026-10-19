"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateContactChannelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class CreateContactChannelResult(TypedDict, closed=True):
    contact_channel_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactChannelResult) -> dict:
    out: dict = {}
    out["ContactChannelArn"] = value["contact_channel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactChannelResult:
    out: CreateContactChannelResult = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelArn") is not None:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    else:
        out["contact_channel_arn"] = ""
    return out
