"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ReferenceMaterialList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.reference_material

ReferenceMaterialList: TypeAlias = list[
    "capo_partnercentral_marketing.types.reference_material.ReferenceMaterial"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReferenceMaterialList) -> list:
    import capo_partnercentral_marketing.types.reference_material

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.reference_material.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ReferenceMaterialList:
    import capo_partnercentral_marketing.types.reference_material

    out: ReferenceMaterialList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.reference_material.deserialize_cbor(
                item
            )
        )
    return out
