"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_summary

BrandProfileAttributeSummaryList: TypeAlias = list[
    "capo_endusermessaging.types.brand_profile_attribute_summary.BrandProfileAttributeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeSummaryList) -> list:
    import capo_endusermessaging.types.brand_profile_attribute_summary

    out: list = []
    for item in value:
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrandProfileAttributeSummaryList:
    import capo_endusermessaging.types.brand_profile_attribute_summary

    out: BrandProfileAttributeSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.brand_profile_attribute_summary.deserialize_json(
                item
            )
        )
    return out
