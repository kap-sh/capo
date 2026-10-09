"""Generated from Smithy shape ``com.amazonaws.medialive#CloudWatchAlarmTemplateTargetResourceType``."""

from typing import Literal, TypeAlias, cast

"""The resource type this template should dynamically generate cloudwatch metric alarms for."""
CloudWatchAlarmTemplateTargetResourceType: TypeAlias = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "MEDIALIVE_MULTIPLEX",
    "MEDIALIVE_CHANNEL",
    "MEDIALIVE_INPUT_DEVICE",
    "MEDIAPACKAGE_CHANNEL",
    "MEDIAPACKAGE_ORIGIN_ENDPOINT",
    "MEDIACONNECT_FLOW",
    "S3_BUCKET",
    "MEDIATAILOR_PLAYBACK_CONFIGURATION",
    "ELEMENTAL_INFERENCE_FEED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchAlarmTemplateTargetResourceType) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchAlarmTemplateTargetResourceType:
    return cast(CloudWatchAlarmTemplateTargetResourceType, data)
