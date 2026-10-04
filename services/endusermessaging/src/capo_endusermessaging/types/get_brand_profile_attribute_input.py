"""Generated from Smithy shape ``com.amazonaws.endusermessaging#GetBrandProfileAttributeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_id_or_arn


class GetBrandProfileAttributeInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrandProfileAttributeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrandProfileAttributeInput:
    out: GetBrandProfileAttributeInput = {}  # type: ignore[typeddict-item]
    return out
