"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.activation_status
    import capo_ssm_contacts.types.channel_name
    import capo_ssm_contacts.types.channel_type
    import capo_ssm_contacts.types.contact_channel_address
    import capo_ssm_contacts.types.ssm_contacts_arn


class ContactChannel(TypedDict, closed=True):
    contact_channel_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that contains the contact channel.</p>"""
    name: "capo_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel.</p>"""
    type: NotRequired["capo_ssm_contacts.types.channel_type.ChannelType"]
    """<p>The type of the contact channel. Incident Manager supports three contact methods:</p> <ul> <li> <p>SMS</p> </li> <li> <p>VOICE</p> </li> <li> <p>EMAIL</p> </li> </ul>"""
    delivery_address: (
        "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""
    activation_status: "capo_ssm_contacts.types.activation_status.ActivationStatus"
    """<p>A Boolean value describing if the contact channel has been activated or not. If the contact channel isn't activated, Incident Manager can't engage the contact through it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactChannel) -> dict:
    out: dict = {}
    out["ContactChannelArn"] = value["contact_channel_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Name"] = value["name"]
    if "type" in value:
        import capo_ssm_contacts.types.channel_type

        out["Type"] = capo_ssm_contacts.types.channel_type.serialize_aws_json_1_1(
            value["type"]
        )
    import capo_ssm_contacts.types.contact_channel_address

    out["DeliveryAddress"] = (
        capo_ssm_contacts.types.contact_channel_address.serialize_aws_json_1_1(
            value["delivery_address"]
        )
    )
    import capo_ssm_contacts.types.activation_status

    out["ActivationStatus"] = (
        capo_ssm_contacts.types.activation_status.serialize_aws_json_1_1(
            value["activation_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactChannel:
    out: ContactChannel = {}  # type: ignore[typeddict-item]
    if data.get("ContactChannelArn") is not None:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    else:
        out["contact_channel_arn"] = ""
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_ssm_contacts.types.channel_type

        out["type"] = capo_ssm_contacts.types.channel_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("DeliveryAddress") is not None:
        import capo_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            capo_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    else:
        raise DeserializationError("ContactChannel.delivery_address required")
    if data.get("ActivationStatus") is not None:
        import capo_ssm_contacts.types.activation_status

        out["activation_status"] = (
            capo_ssm_contacts.types.activation_status.deserialize_aws_json_1_1(
                data["ActivationStatus"]
            )
        )
    else:
        import typing

        out["activation_status"] = typing.cast(
            "capo_ssm_contacts.types.activation_status.ActivationStatus", ""
        )
    return out
