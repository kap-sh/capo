"""Generated from Smithy shape ``com.amazonaws.invoicing#ProfileList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_profile

ProfileList: TypeAlias = list["capo_invoicing.types.invoice_profile.InvoiceProfile"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileList) -> list:
    import capo_invoicing.types.invoice_profile

    out: list = []
    for item in value:
        out.append(capo_invoicing.types.invoice_profile.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ProfileList:
    import capo_invoicing.types.invoice_profile

    out: ProfileList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_invoicing.types.invoice_profile.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: ProfileList) -> list[Any]:
    import capo_invoicing.types.invoice_profile

    return [
        capo_invoicing.types.invoice_profile.redact_sensitive(item) for item in value
    ]
