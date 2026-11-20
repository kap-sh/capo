"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FieldValueInputList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.field_value_input

FieldValueInputList: TypeAlias = list[
    "capo_partnercentral_marketing.types.field_value_input.FieldValueInput"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FieldValueInputList) -> list:
    import capo_partnercentral_marketing.types.field_value_input

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.field_value_input.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> FieldValueInputList:
    import capo_partnercentral_marketing.types.field_value_input

    out: FieldValueInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.field_value_input.deserialize_cbor(item)
        )
    return out


def redact_sensitive(value: FieldValueInputList) -> list[Any]:
    import capo_partnercentral_marketing.types.field_value_input

    return [
        capo_partnercentral_marketing.types.field_value_input.redact_sensitive(item)
        for item in value
    ]
