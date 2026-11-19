"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ContactTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.contact_type

ContactTypeList: TypeAlias = list[
    "capo_marketplace_agreement.types.contact_type.ContactType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContactTypeList) -> list:
    import capo_marketplace_agreement.types.contact_type

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.contact_type.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContactTypeList:
    import capo_marketplace_agreement.types.contact_type

    out: ContactTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.contact_type.deserialize_aws_json_1_0(item)
        )
    return out
