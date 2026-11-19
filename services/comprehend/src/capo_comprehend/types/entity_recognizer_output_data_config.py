"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerOutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.s3_uri


class EntityRecognizerOutputDataConfig(TypedDict, closed=True):
    flywheel_stats_s3_prefix: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 prefix for the data lake location of the flywheel statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerOutputDataConfig) -> dict:
    out: dict = {}
    if "flywheel_stats_s3_prefix" in value:
        out["FlywheelStatsS3Prefix"] = value["flywheel_stats_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerOutputDataConfig:
    out: EntityRecognizerOutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelStatsS3Prefix") is not None:
        out["flywheel_stats_s3_prefix"] = data["FlywheelStatsS3Prefix"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerOutputDataConfig) -> dict:
    out: dict = {}
    if "flywheel_stats_s3_prefix" in value:
        out["FlywheelStatsS3Prefix"] = value["flywheel_stats_s3_prefix"]
    return out


def deserialize_cbor(data: dict) -> EntityRecognizerOutputDataConfig:
    out: EntityRecognizerOutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelStatsS3Prefix") is not None:
        out["flywheel_stats_s3_prefix"] = data["FlywheelStatsS3Prefix"]
    return out
