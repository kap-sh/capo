"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_info

BrandProfileInfoList: TypeAlias = list[
    "capo_endusermessaging.types.brand_profile_info.BrandProfileInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileInfoList) -> list:
    import capo_endusermessaging.types.brand_profile_info

    out: list = []
    for item in value:
        out.append(capo_endusermessaging.types.brand_profile_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrandProfileInfoList:
    import capo_endusermessaging.types.brand_profile_info

    out: BrandProfileInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.brand_profile_info.deserialize_json(item)
        )
    return out
