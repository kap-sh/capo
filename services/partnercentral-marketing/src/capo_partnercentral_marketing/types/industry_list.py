"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#IndustryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.industry

IndustryList: TypeAlias = list["capo_partnercentral_marketing.types.industry.Industry"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IndustryList) -> list:
    import capo_partnercentral_marketing.types.industry

    out: list = []
    for item in value:
        out.append(capo_partnercentral_marketing.types.industry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IndustryList:
    import capo_partnercentral_marketing.types.industry

    out: IndustryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_partnercentral_marketing.types.industry.deserialize_cbor(item))
    return out
