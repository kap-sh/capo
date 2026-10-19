"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.aws_region
    import capo_chime_sdk_media_pipelines.types.data_retention_in_hours


class KinesisVideoStreamConfiguration(TypedDict, closed=True):
    region: "capo_chime_sdk_media_pipelines.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region of the video stream.</p>"""
    data_retention_in_hours: NotRequired[
        "capo_chime_sdk_media_pipelines.types.data_retention_in_hours.DataRetentionInHours"
    ]
    """<p>The amount of time that data is retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "data_retention_in_hours" in value:
        out["DataRetentionInHours"] = value["data_retention_in_hours"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamConfiguration:
    out: KinesisVideoStreamConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("DataRetentionInHours") is not None:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    return out
