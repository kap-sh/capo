"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.attachment_body
    import capo_endusermessaging.types.brand_profile_attribute_category
    import capo_endusermessaging.types.brand_profile_attribute_description
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_type
    import capo_endusermessaging.types.brand_profile_attribute_value


class BrandProfileAttributeInput(TypedDict, closed=True):
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""
    attribute_type: "capo_endusermessaging.types.brand_profile_attribute_type.BrandProfileAttributeType"
    """<p>The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.</p>"""
    attribute_value: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_value.BrandProfileAttributeValue"
    ]
    """<p>The text value for the attribute. This value applies to attributes of type TEXT. For attributes of type IMAGE or DOCUMENT, provide the media through the attachment body instead.</p>"""
    attachment_body: NotRequired[
        "capo_endusermessaging.types.attachment_body.AttachmentBody"
    ]
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
def serialize_json(value: BrandProfileAttributeInput) -> dict:
    out: dict = {}
    out["attributeName"] = value["attribute_name"]
    import capo_endusermessaging.types.brand_profile_attribute_type

    out["attributeType"] = (
        capo_endusermessaging.types.brand_profile_attribute_type.serialize_json(
            value["attribute_type"]
        )
    )
    if "attribute_value" in value:
        out["attributeValue"] = value["attribute_value"]
    if "attachment_body" in value:
        import capo_endusermessaging.types.attachment_body

        out["attachmentBody"] = (
            capo_endusermessaging.types.attachment_body.serialize_json(
                value["attachment_body"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    return out


def deserialize_json(data: dict) -> BrandProfileAttributeInput:
    out: BrandProfileAttributeInput = {}  # type: ignore[typeddict-item]
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    else:
        raise DeserializationError("BrandProfileAttributeInput.attribute_name required")
    if data.get("attributeType") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_type

        out["attribute_type"] = (
            capo_endusermessaging.types.brand_profile_attribute_type.deserialize_json(
                data["attributeType"]
            )
        )
    else:
        raise DeserializationError("BrandProfileAttributeInput.attribute_type required")
    if data.get("attributeValue") is not None:
        out["attribute_value"] = data["attributeValue"]
    if data.get("attachmentBody") is not None:
        import capo_endusermessaging.types.attachment_body

        out["attachment_body"] = (
            capo_endusermessaging.types.attachment_body.deserialize_json(
                data["attachmentBody"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    return out
