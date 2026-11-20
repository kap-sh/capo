"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.tag

TagList: TypeAlias = list["capo_partnercentral_marketing.types.tag.Tag"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagList) -> list:
    import capo_partnercentral_marketing.types.tag

    out: list = []
    for item in value:
        out.append(capo_partnercentral_marketing.types.tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TagList:
    import capo_partnercentral_marketing.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_partnercentral_marketing.types.tag.deserialize_cbor(item))
    return out
