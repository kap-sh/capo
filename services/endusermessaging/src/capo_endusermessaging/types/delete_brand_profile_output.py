"""Generated from Smithy shape ``com.amazonaws.endusermessaging#DeleteBrandProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.brand_profile_id_or_arn


class DeleteBrandProfileOutput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile.</p>"""
    brand_profile_arn: (
        "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the brand profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandProfileOutput) -> dict:
    out: dict = {}
    out["brandProfileId"] = value["brand_profile_id"]
    out["brandProfileArn"] = value["brand_profile_arn"]
    return out


def deserialize_json(data: dict) -> DeleteBrandProfileOutput:
    out: DeleteBrandProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileId") is not None:
        out["brand_profile_id"] = data["brandProfileId"]
    else:
        raise DeserializationError("DeleteBrandProfileOutput.brand_profile_id required")
    if data.get("brandProfileArn") is not None:
        out["brand_profile_arn"] = data["brandProfileArn"]
    else:
        raise DeserializationError(
            "DeleteBrandProfileOutput.brand_profile_arn required"
        )
    return out
