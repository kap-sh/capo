"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ImageGenerationDestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.destination_region
    import capo_kinesis_video.types.destination_uri


class ImageGenerationDestinationConfig(TypedDict, closed=True):
    uri: "capo_kinesis_video.types.destination_uri.DestinationUri"
    """<p>The Uniform Resource Identifier (URI) that identifies where the images will be delivered.</p>"""
    destination_region: "capo_kinesis_video.types.destination_region.DestinationRegion"
    """<p>The Amazon Web Services Region of the S3 bucket where images will be delivered. This <code>DestinationRegion</code> must match the Region where the stream is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageGenerationDestinationConfig) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    out["DestinationRegion"] = value["destination_region"]
    return out


def deserialize_json(data: dict) -> ImageGenerationDestinationConfig:
    out: ImageGenerationDestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    if data.get("DestinationRegion") is not None:
        out["destination_region"] = data["DestinationRegion"]
    else:
        out["destination_region"] = ""
    return out
