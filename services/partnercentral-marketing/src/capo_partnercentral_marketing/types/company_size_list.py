"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CompanySizeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.company_size

CompanySizeList: TypeAlias = list[
    "capo_partnercentral_marketing.types.company_size.CompanySize"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CompanySizeList) -> list:
    import capo_partnercentral_marketing.types.company_size

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.company_size.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CompanySizeList:
    import capo_partnercentral_marketing.types.company_size

    out: CompanySizeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.company_size.deserialize_cbor(item)
        )
    return out
