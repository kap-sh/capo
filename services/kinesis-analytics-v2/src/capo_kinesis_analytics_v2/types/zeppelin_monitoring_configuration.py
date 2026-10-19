"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.log_level


class ZeppelinMonitoringConfiguration(TypedDict, closed=True):
    log_level: "capo_kinesis_analytics_v2.types.log_level.LogLevel"
    """<p>The verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinMonitoringConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.log_level

    out["LogLevel"] = capo_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
        value["log_level"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinMonitoringConfiguration:
    out: ZeppelinMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogLevel") is not None:
        import capo_kinesis_analytics_v2.types.log_level

        out["log_level"] = (
            capo_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    else:
        import typing

        out["log_level"] = typing.cast(
            "capo_kinesis_analytics_v2.types.log_level.LogLevel", ""
        )
    return out
