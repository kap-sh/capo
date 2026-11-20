"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UseCaseFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.use_case_filter

UseCaseFilterList: TypeAlias = list[
    "capo_partnercentral_marketing.types.use_case_filter.UseCaseFilter"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UseCaseFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> UseCaseFilterList:
    return [item for item in data if item is not None]
