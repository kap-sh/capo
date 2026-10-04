"""Generated from Smithy shape ``com.amazonaws.endusermessaging#GetBrandProfileAttributeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.brand_profile_attribute_category
    import capo_endusermessaging.types.brand_profile_attribute_description
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_type
    import capo_endusermessaging.types.brand_profile_attribute_value
    import capo_endusermessaging.types.media_download_url


class GetBrandProfileAttributeOutput(TypedDict, closed=True):
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""
    attribute_type: "capo_endusermessaging.types.brand_profile_attribute_type.BrandProfileAttributeType"
    """<p>The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.</p>"""
    attribute_value: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_value.BrandProfileAttributeValue"
    ]
    """<p>The text value of the attribute. This value applies to attributes of type TEXT.</p>"""
    description: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_description.BrandProfileAttributeDescription"
    ]
    """<p>A description of the attribute.</p>"""
    category: NotRequired[
        "capo_endusermessaging.types.brand_profile_attribute_category.BrandProfileAttributeCategory"
    ]
    """<p>The category of the attribute.</p>"""
    media_content_type: NotRequired["str"]
    """<p>The MIME content type of the attribute media.</p>"""
    media_size_bytes: NotRequired["int"]
    """<p>The size of the attribute media, in bytes.</p>"""
    media_download_url: NotRequired[
        "capo_endusermessaging.types.media_download_url.MediaDownloadUrl"
    ]
    """<p>A presigned Amazon S3 URL that you can use to download the attribute media. The URL is valid for one hour and is present only for attributes of type IMAGE or DOCUMENT.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time when the resource was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrandProfileAttributeOutput) -> dict:
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
    if "description" in value:
        out["description"] = value["description"]
    if "category" in value:
        out["category"] = value["category"]
    if "media_content_type" in value:
        out["mediaContentType"] = value["media_content_type"]
    if "media_size_bytes" in value:
        out["mediaSizeBytes"] = value["media_size_bytes"]
    if "media_download_url" in value:
        out["mediaDownloadUrl"] = value["media_download_url"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_endusermessaging.types._prelude.timestamp

    out["updatedAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetBrandProfileAttributeOutput:
    out: GetBrandProfileAttributeOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    else:
        raise DeserializationError(
            "GetBrandProfileAttributeOutput.attribute_name required"
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
            "GetBrandProfileAttributeOutput.attribute_type required"
        )
    if data.get("attributeValue") is not None:
        out["attribute_value"] = data["attributeValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("mediaContentType") is not None:
        out["media_content_type"] = data["mediaContentType"]
    if data.get("mediaSizeBytes") is not None:
        out["media_size_bytes"] = data["mediaSizeBytes"]
    if data.get("mediaDownloadUrl") is not None:
        out["media_download_url"] = data["mediaDownloadUrl"]
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetBrandProfileAttributeOutput.created_at required")
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetBrandProfileAttributeOutput.updated_at required")
    return out
