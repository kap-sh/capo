"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetRouterInputThumbnailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_thumbnail_details


class GetRouterInputThumbnailResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the router input.</p>"""
    name: "str"
    """<p>The name of the router input.</p>"""
    thumbnail_details: "capo_mediaconnect.types.router_input_thumbnail_details.RouterInputThumbnailDetails"
    """<p>The details of the thumbnail associated with the router input, including the thumbnail image, timecode, timestamp, and any associated error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouterInputThumbnailResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_input_thumbnail_details

    out["thumbnailDetails"] = (
        capo_mediaconnect.types.router_input_thumbnail_details.serialize_json(
            value["thumbnail_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRouterInputThumbnailResponse:
    out: GetRouterInputThumbnailResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("thumbnailDetails") is not None:
        import capo_mediaconnect.types.router_input_thumbnail_details

        out["thumbnail_details"] = (
            capo_mediaconnect.types.router_input_thumbnail_details.deserialize_json(
                data["thumbnailDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetRouterInputThumbnailResponse.thumbnail_details required"
        )
    return out
