"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#LanguageFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_language

LanguageFilterList: TypeAlias = list[
    "capo_partnercentral_marketing.types.asset_language.AssetLanguage"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageFilterList) -> list:
    import capo_partnercentral_marketing.types.asset_language

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.asset_language.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> LanguageFilterList:
    import capo_partnercentral_marketing.types.asset_language

    out: LanguageFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.asset_language.deserialize_cbor(item)
        )
    return out
