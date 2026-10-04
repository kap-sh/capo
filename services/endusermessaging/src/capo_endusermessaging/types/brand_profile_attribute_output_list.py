"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_output

BrandProfileAttributeOutputList: TypeAlias = list[
    "capo_endusermessaging.types.brand_profile_attribute_output.BrandProfileAttributeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeOutputList) -> list:
    import capo_endusermessaging.types.brand_profile_attribute_output

    out: list = []
    for item in value:
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrandProfileAttributeOutputList:
    import capo_endusermessaging.types.brand_profile_attribute_output

    out: BrandProfileAttributeOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_output.deserialize_json(
                item
            )
        )
    return out
