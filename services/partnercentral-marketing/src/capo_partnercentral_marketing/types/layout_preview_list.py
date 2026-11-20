"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#LayoutPreviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.layout_preview

LayoutPreviewList: TypeAlias = list[
    "capo_partnercentral_marketing.types.layout_preview.LayoutPreview"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LayoutPreviewList) -> list:
    import capo_partnercentral_marketing.types.layout_preview

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.layout_preview.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> LayoutPreviewList:
    import capo_partnercentral_marketing.types.layout_preview

    out: LayoutPreviewList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.layout_preview.deserialize_cbor(item)
        )
    return out
