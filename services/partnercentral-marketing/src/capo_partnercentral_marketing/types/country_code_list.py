"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CountryCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.country_code

CountryCodeList: TypeAlias = list[
    "capo_partnercentral_marketing.types.country_code.CountryCode"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CountryCodeList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CountryCodeList:
    return [item for item in data if item is not None]
