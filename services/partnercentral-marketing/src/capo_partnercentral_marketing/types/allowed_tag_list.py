"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AllowedTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.html_tag_name

AllowedTagList: TypeAlias = list[
    "capo_partnercentral_marketing.types.html_tag_name.HtmlTagName"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AllowedTagList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AllowedTagList:
    return [item for item in data if item is not None]
