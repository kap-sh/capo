"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TemplateFieldIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.template_field_id

TemplateFieldIdList: TypeAlias = list[
    "capo_partnercentral_marketing.types.template_field_id.TemplateFieldId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TemplateFieldIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TemplateFieldIdList:
    return [item for item in data if item is not None]
