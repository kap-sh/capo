"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ThemeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.theme

ThemeFilterList: TypeAlias = list["capo_partnercentral_marketing.types.theme.Theme"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeFilterList) -> list:
    import capo_partnercentral_marketing.types.theme

    out: list = []
    for item in value:
        out.append(capo_partnercentral_marketing.types.theme.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ThemeFilterList:
    import capo_partnercentral_marketing.types.theme

    out: ThemeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_partnercentral_marketing.types.theme.deserialize_cbor(item))
    return out
