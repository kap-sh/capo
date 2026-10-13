"""Generated from Smithy shape ``com.amazonaws.invoicing#Contacts``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.contact

Contacts: TypeAlias = list["capo_invoicing.types.contact.Contact"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contacts) -> list:
    import capo_invoicing.types.contact

    out: list = []
    for item in value:
        out.append(capo_invoicing.types.contact.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Contacts:
    import capo_invoicing.types.contact

    out: Contacts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_invoicing.types.contact.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: Contacts) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
