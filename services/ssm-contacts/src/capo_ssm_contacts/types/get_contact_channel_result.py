"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactChannelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.activation_status
    import capo_ssm_contacts.types.channel_name
    import capo_ssm_contacts.types.channel_type
    import capo_ssm_contacts.types.contact_channel_address
    import capo_ssm_contacts.types.ssm_contacts_arn


class GetContactChannelResult(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that the channel belongs to.</p>"""
    contact_channel_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact channel.</p>"""
    name: "capo_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel</p>"""
    type: "capo_ssm_contacts.types.channel_type.ChannelType"
    """<p>The type of contact channel. The type is <code>SMS</code>, <code>VOICE</code>, or <code>EMAIL</code>.</p>"""
    delivery_address: (
        "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""
    activation_status: NotRequired[
        "capo_ssm_contacts.types.activation_status.ActivationStatus"
    ]
    """<p>A Boolean value indicating if the contact channel has been activated or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactChannelResult) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["ContactChannelArn"] = value["contact_channel_arn"]
    out["Name"] = value["name"]
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
    if "activation_status" in value:
        import capo_ssm_contacts.types.activation_status

        out["ActivationStatus"] = (
            capo_ssm_contacts.types.activation_status.serialize_aws_json_1_1(
                value["activation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactChannelResult:
    out: GetContactChannelResult = {}  # type: ignore[typeddict-item]
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("ContactChannelArn") is not None:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    else:
        out["contact_channel_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        import capo_ssm_contacts.types.channel_type

        out["type"] = capo_ssm_contacts.types.channel_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_ssm_contacts.types.channel_type.ChannelType", ""
        )
    if data.get("DeliveryAddress") is not None:
        import capo_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            capo_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    else:
        raise DeserializationError("GetContactChannelResult.delivery_address required")
    if data.get("ActivationStatus") is not None:
        import capo_ssm_contacts.types.activation_status

        out["activation_status"] = (
            capo_ssm_contacts.types.activation_status.deserialize_aws_json_1_1(
                data["ActivationStatus"]
            )
        )
    return out
