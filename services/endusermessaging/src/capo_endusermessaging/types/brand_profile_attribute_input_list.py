"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_input

BrandProfileAttributeInputList: TypeAlias = list[
    "capo_endusermessaging.types.brand_profile_attribute_input.BrandProfileAttributeInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeInputList) -> list:
    import capo_endusermessaging.types.brand_profile_attribute_input

    out: list = []
    for item in value:
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrandProfileAttributeInputList:
    import capo_endusermessaging.types.brand_profile_attribute_input

    out: BrandProfileAttributeInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_input.deserialize_json(
                item
            )
        )
    return out
