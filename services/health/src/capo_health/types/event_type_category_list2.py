"""Generated from Smithy shape ``com.amazonaws.health#eventTypeCategoryList2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type_category

eventTypeCategoryList2: TypeAlias = list[
    "capo_health.types.event_type_category.eventTypeCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeCategoryList2) -> list:
    import capo_health.types.event_type_category

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> eventTypeCategoryList2:
    import capo_health.types.event_type_category

    out: eventTypeCategoryList2 = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_type_category.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventTypeCategoryList2) -> list:
    import capo_health.types.event_type_category

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type_category.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> eventTypeCategoryList2:
    import capo_health.types.event_type_category

    out: eventTypeCategoryList2 = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_type_category.deserialize_cbor(item))
    return out
