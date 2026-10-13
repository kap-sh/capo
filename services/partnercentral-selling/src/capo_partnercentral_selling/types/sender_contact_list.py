"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SenderContactList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.sender_contact

SenderContactList: TypeAlias = list[
    "capo_partnercentral_selling.types.sender_contact.SenderContact"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderContactList) -> list:
    import capo_partnercentral_selling.types.sender_contact

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.sender_contact.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SenderContactList:
    import capo_partnercentral_selling.types.sender_contact

    out: SenderContactList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.sender_contact.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: SenderContactList) -> list[Any]:
    import capo_partnercentral_selling.types.sender_contact

    return [
        capo_partnercentral_selling.types.sender_contact.redact_sensitive(item)
        for item in value
    ]
