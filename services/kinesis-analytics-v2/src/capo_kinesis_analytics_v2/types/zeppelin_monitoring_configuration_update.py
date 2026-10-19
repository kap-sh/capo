"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinMonitoringConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.log_level


class ZeppelinMonitoringConfigurationUpdate(TypedDict, closed=True):
    log_level_update: "capo_kinesis_analytics_v2.types.log_level.LogLevel"
    """<p>Updates to the logging level for Apache Zeppelin within a Managed Service for Apache Flink Studio notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinMonitoringConfigurationUpdate) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.log_level

    out["LogLevelUpdate"] = (
        capo_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
            value["log_level_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinMonitoringConfigurationUpdate:
    out: ZeppelinMonitoringConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("LogLevelUpdate") is not None:
        import capo_kinesis_analytics_v2.types.log_level

        out["log_level_update"] = (
            capo_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevelUpdate"]
            )
        )
    else:
        import typing

        out["log_level_update"] = typing.cast(
            "capo_kinesis_analytics_v2.types.log_level.LogLevel", ""
        )
    return out
