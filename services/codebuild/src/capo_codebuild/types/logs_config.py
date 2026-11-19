"""Generated from Smithy shape ``com.amazonaws.codebuild#LogsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.cloud_watch_logs_config
    import capo_codebuild.types.s3_logs_config


class LogsConfig(TypedDict, closed=True):
    cloud_watch_logs: NotRequired[
        "capo_codebuild.types.cloud_watch_logs_config.CloudWatchLogsConfig"
    ]
    """<p> Information about CloudWatch Logs for a build project. CloudWatch Logs are enabled by default. </p>"""
    s3_logs: NotRequired["capo_codebuild.types.s3_logs_config.S3LogsConfig"]
    """<p> Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogsConfig) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_codebuild.types.cloud_watch_logs_config

        out["cloudWatchLogs"] = (
            capo_codebuild.types.cloud_watch_logs_config.serialize_aws_json_1_1(
                value["cloud_watch_logs"]
            )
        )
    if "s3_logs" in value:
        import capo_codebuild.types.s3_logs_config

        out["s3Logs"] = capo_codebuild.types.s3_logs_config.serialize_aws_json_1_1(
            value["s3_logs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogsConfig:
    out: LogsConfig = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogs") is not None:
        import capo_codebuild.types.cloud_watch_logs_config

        out["cloud_watch_logs"] = (
            capo_codebuild.types.cloud_watch_logs_config.deserialize_aws_json_1_1(
                data["cloudWatchLogs"]
            )
        )
    if data.get("s3Logs") is not None:
        import capo_codebuild.types.s3_logs_config

        out["s3_logs"] = capo_codebuild.types.s3_logs_config.deserialize_aws_json_1_1(
            data["s3Logs"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogsConfig) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_codebuild.types.cloud_watch_logs_config

        out["cloudWatchLogs"] = (
            capo_codebuild.types.cloud_watch_logs_config.serialize_cbor(
                value["cloud_watch_logs"]
            )
        )
    if "s3_logs" in value:
        import capo_codebuild.types.s3_logs_config

        out["s3Logs"] = capo_codebuild.types.s3_logs_config.serialize_cbor(
            value["s3_logs"]
        )
    return out


def deserialize_cbor(data: dict) -> LogsConfig:
    out: LogsConfig = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogs") is not None:
        import capo_codebuild.types.cloud_watch_logs_config

        out["cloud_watch_logs"] = (
            capo_codebuild.types.cloud_watch_logs_config.deserialize_cbor(
                data["cloudWatchLogs"]
            )
        )
    if data.get("s3Logs") is not None:
        import capo_codebuild.types.s3_logs_config

        out["s3_logs"] = capo_codebuild.types.s3_logs_config.deserialize_cbor(
            data["s3Logs"]
        )
    return out
