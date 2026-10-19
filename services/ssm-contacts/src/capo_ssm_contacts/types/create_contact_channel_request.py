"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateContactChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.channel_name
    import capo_ssm_contacts.types.channel_type
    import capo_ssm_contacts.types.contact_channel_address
    import capo_ssm_contacts.types.defer_activation
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.ssm_contacts_arn


class CreateContactChannelRequest(TypedDict, closed=True):
    contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.</p>"""
    name: "capo_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel.</p>"""
    type: "capo_ssm_contacts.types.channel_type.ChannelType"
    """<p>Incident Manager supports three types of contact channels:</p> <ul> <li> <p> <code>SMS</code> </p> </li> <li> <p> <code>VOICE</code> </p> </li> <li> <p> <code>EMAIL</code> </p> </li> </ul>"""
    delivery_address: (
        "capo_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel. The format is dependent on the type of the contact channel. The following are the expected formats:</p> <ul> <li> <p>SMS - '+' followed by the country code and phone number</p> </li> <li> <p>VOICE - '+' followed by the country code and phone number</p> </li> <li> <p>EMAIL - any standard email format</p> </li> </ul>"""
    defer_activation: NotRequired[
        "capo_ssm_contacts.types.defer_activation.DeferActivation"
    ]
    """<p>If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.</p>"""
    idempotency_token: NotRequired[
        "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
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
    if "defer_activation" in value:
        out["DeferActivation"] = value["defer_activation"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactChannelRequest:
    out: CreateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
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
        raise DeserializationError(
            "CreateContactChannelRequest.delivery_address required"
        )
    if data.get("DeferActivation") is not None:
        out["defer_activation"] = data["DeferActivation"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
