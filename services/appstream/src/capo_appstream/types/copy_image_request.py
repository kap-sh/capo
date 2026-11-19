"""Generated from Smithy shape ``com.amazonaws.appstream#CopyImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.description
    import capo_appstream.types.name
    import capo_appstream.types.region_name


class CopyImageRequest(TypedDict, closed=True):
    source_image_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the image to copy.</p>"""
    destination_image_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name that the image will have when it is copied to the destination.</p>"""
    destination_region: NotRequired["capo_appstream.types.region_name.RegionName"]
    """<p>The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.</p>"""
    destination_image_description: NotRequired[
        "capo_appstream.types.description.Description"
    ]
    """<p>The description that the image will have when it is copied to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyImageRequest) -> dict:
    out: dict = {}
    if "source_image_name" in value:
        out["SourceImageName"] = value["source_image_name"]
    if "destination_image_name" in value:
        out["DestinationImageName"] = value["destination_image_name"]
    if "destination_region" in value:
        out["DestinationRegion"] = value["destination_region"]
    if "destination_image_description" in value:
        out["DestinationImageDescription"] = value["destination_image_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyImageRequest:
    out: CopyImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceImageName") is not None:
        out["source_image_name"] = data["SourceImageName"]
    if data.get("DestinationImageName") is not None:
        out["destination_image_name"] = data["DestinationImageName"]
    if data.get("DestinationRegion") is not None:
        out["destination_region"] = data["DestinationRegion"]
    if data.get("DestinationImageDescription") is not None:
        out["destination_image_description"] = data["DestinationImageDescription"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopyImageRequest) -> dict:
    out: dict = {}
    if "source_image_name" in value:
        out["SourceImageName"] = value["source_image_name"]
    if "destination_image_name" in value:
        out["DestinationImageName"] = value["destination_image_name"]
    if "destination_region" in value:
        out["DestinationRegion"] = value["destination_region"]
    if "destination_image_description" in value:
        out["DestinationImageDescription"] = value["destination_image_description"]
    return out


def deserialize_cbor(data: dict) -> CopyImageRequest:
    out: CopyImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceImageName") is not None:
        out["source_image_name"] = data["SourceImageName"]
    if data.get("DestinationImageName") is not None:
        out["destination_image_name"] = data["DestinationImageName"]
    if data.get("DestinationRegion") is not None:
        out["destination_region"] = data["DestinationRegion"]
    if data.get("DestinationImageDescription") is not None:
        out["destination_image_description"] = data["DestinationImageDescription"]
    return out
