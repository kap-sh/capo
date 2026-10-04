"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateBrandProfileAttributeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_category
    import capo_endusermessaging.types.brand_profile_attribute_description
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_value
    import capo_endusermessaging.types.brand_profile_id_or_arn


class UpdateBrandProfileAttributeInput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""
    attribute_value: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_value.BrandProfileAttributeValue"
    ]
    """<p>The text value of the attribute. This value applies to attributes of type TEXT.</p>"""
    attachment_body: NotRequired["bytes"]
    """<p>The binary content for an attribute of type IMAGE or DOCUMENT. The content is base64-encoded when it is sent over the wire.</p>"""
    description: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_description.BrandProfileAttributeDescription"
    ]
    """<p>A description of the attribute.</p>"""
    category: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_category.BrandProfileAttributeCategory"
    ]
    """<p>The category of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandProfileAttributeInput) -> dict:
    out: dict = {}
    if "attribute_value" in value:
        out["attributeValue"] = value["attribute_value"]
    if "attachment_body" in value:
        import capo_endusermessaging.types._prelude.blob

        out["attachmentBody"] = (
            capo_endusermessaging.types._prelude.blob.serialize_json(
                value["attachment_body"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> UpdateBrandProfileAttributeInput:
    out: UpdateBrandProfileAttributeInput = {}  # type: ignore[typeddict-item]
    if data.get("attributeValue") is not None:
        out["attribute_value"] = data["attributeValue"]
    if data.get("attachmentBody") is not None:
        import capo_endusermessaging.types._prelude.blob

        out["attachment_body"] = (
            capo_endusermessaging.types._prelude.blob.deserialize_json(
                data["attachmentBody"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    return out
