"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CustomerSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.customer_segment

CustomerSegmentList: TypeAlias = list[
    "capo_partnercentral_marketing.types.customer_segment.CustomerSegment"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerSegmentList) -> list:
    import capo_partnercentral_marketing.types.customer_segment

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.customer_segment.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CustomerSegmentList:
    import capo_partnercentral_marketing.types.customer_segment

    out: CustomerSegmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.customer_segment.deserialize_cbor(item)
        )
    return out
