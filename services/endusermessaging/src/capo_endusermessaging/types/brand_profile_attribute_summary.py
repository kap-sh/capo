"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.brand_profile_attribute_category
    import capo_endusermessaging.types.brand_profile_attribute_description
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_type


class BrandProfileAttributeSummary(TypedDict, closed=True):
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""
    attribute_type: "capo_endusermessaging.types.brand_profile_attribute_type.BrandProfileAttributeType"
    """<p>The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.</p>"""
    description: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_description.BrandProfileAttributeDescription"
    ]
    """<p>A description of the attribute.</p>"""
    category: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_category.BrandProfileAttributeCategory"
    ]
    """<p>The category of the attribute.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time when the resource was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeSummary) -> dict:
    out: dict = {}
    out["attributeName"] = value["attribute_name"]
    import capo_endusermessaging.types.brand_profile_attribute_type

    out["attributeType"] = (
        capo_endusermessaging.types.brand_profile_attribute_type.serialize_json(
            value["attribute_type"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_endusermessaging.types._prelude.timestamp

    out["updatedAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> BrandProfileAttributeSummary:
    out: BrandProfileAttributeSummary = {}  # type: ignore[typeddict-item]
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    else:
        raise DeserializationError(
            "BrandProfileAttributeSummary.attribute_name required"
        )
    if data.get("attributeType") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_type

        out["attribute_type"] = (
            capo_endusermessaging.types.brand_profile_attribute_type.deserialize_json(
                data["attributeType"]
            )
        )
    else:
        raise DeserializationError(
            "BrandProfileAttributeSummary.attribute_type required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BrandProfileAttributeSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("BrandProfileAttributeSummary.updated_at required")
    return out
