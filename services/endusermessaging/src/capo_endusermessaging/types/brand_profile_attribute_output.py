"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileAttributeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_type
    import capo_endusermessaging.types.media_download_url


class BrandProfileAttributeOutput(TypedDict, closed=True):
    attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName"
    """<p>The name of the brand profile attribute. The name is unique within a brand profile.</p>"""
    attribute_type: "capo_endusermessaging.types.brand_profile_attribute_type.BrandProfileAttributeType"
    """<p>The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.</p>"""
    media_download_url: NotRequired[
        "capo_endusermessaging.types.media_download_url.MediaDownloadUrl"
    ]
    """<p>A presigned Amazon S3 URL that you can use to download the attribute media. The URL is valid for one hour and is present only for attributes of type IMAGE or DOCUMENT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandProfileAttributeOutput) -> dict:
    out: dict = {}
    out["attributeName"] = value["attribute_name"]
    import capo_endusermessaging.types.brand_profile_attribute_type

    out["attributeType"] = (
        capo_endusermessaging.types.brand_profile_attribute_type.serialize_json(
            value["attribute_type"]
        )
    )
    if "media_download_url" in value:
        out["mediaDownloadUrl"] = value["media_download_url"]
    return out


def deserialize_json(data: dict) -> BrandProfileAttributeOutput:
    out: BrandProfileAttributeOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("attributeType") is not None:
        import capo_endusermessaging.types.brand_profile_attribute_type

        out["attribute_type"] = (
            capo_endusermessaging.types.brand_profile_attribute_type.deserialize_json(
                data["attributeType"]
            )
        )
    else:
        import typing

        out["attribute_type"] = typing.cast(
            "capo_endusermessaging.types.brand_profile_attribute_type.BrandProfileAttributeType",
            "",
        )
    if data.get("mediaDownloadUrl") is not None:
        out["media_download_url"] = data["mediaDownloadUrl"]
    return out


def redact_sensitive(value: BrandProfileAttributeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attribute_name" in value:
        out["attribute_name"] = "*** Sensitive Data Redacted ***"
    if "media_download_url" in value:
        out["media_download_url"] = "*** Sensitive Data Redacted ***"
    return out
