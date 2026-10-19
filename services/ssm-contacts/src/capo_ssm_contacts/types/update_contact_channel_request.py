"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#UpdateContactChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.channel_name
    import capo_ssm_contacts.types.contact_channel_address
    import capo_ssm_contacts.types.ssm_contacts_arn


class UpdateContactChannelRequest(TypedDict, closed=True):
    contact_channel_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel you want to update.</p>"""
    name: NotRequired["capo_ssm_contacts.types.channel_name.ChannelName"]
    """<p>The name of the contact channel.</p>"""
    delivery_address: NotRequired[
        "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    ]
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "delivery_address" in value:
        import capo_ssm_contacts.types.contact_channel_address

        out["DeliveryAddress"] = (
            capo_ssm_contacts.types.contact_channel_address.serialize_aws_json_1_1(
                value["delivery_address"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContactChannelRequest:
    out: UpdateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelId") is not None:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        out["contact_channel_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DeliveryAddress") is not None:
        import capo_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            capo_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    return out
