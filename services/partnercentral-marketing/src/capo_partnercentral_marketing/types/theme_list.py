"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ThemeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.theme

ThemeList: TypeAlias = list["capo_partnercentral_marketing.types.theme.Theme"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeList) -> list:
    import capo_partnercentral_marketing.types.theme

    out: list = []
    for item in value:
        out.append(capo_partnercentral_marketing.types.theme.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ThemeList:
    import capo_partnercentral_marketing.types.theme

    out: ThemeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_partnercentral_marketing.types.theme.deserialize_cbor(item))
    return out
