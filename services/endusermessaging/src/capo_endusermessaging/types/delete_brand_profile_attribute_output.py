"""Generated from Smithy shape ``com.amazonaws.endusermessaging#DeleteBrandProfileAttributeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_id_or_arn


class DeleteBrandProfileAttributeOutput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile.</p>"""
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandProfileAttributeOutput) -> dict:
    out: dict = {}
    out["brandProfileId"] = value["brand_profile_id"]
    out["attributeName"] = value["attribute_name"]
    return out


def deserialize_json(data: dict) -> DeleteBrandProfileAttributeOutput:
    out: DeleteBrandProfileAttributeOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileId") is not None:
        out["brand_profile_id"] = data["brandProfileId"]
    else:
        raise DeserializationError(
            "DeleteBrandProfileAttributeOutput.brand_profile_id required"
        )
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    else:
        raise DeserializationError(
            "DeleteBrandProfileAttributeOutput.attribute_name required"
        )
    return out
