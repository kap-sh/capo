"""Generated from Smithy shape ``com.amazonaws.mediatailor#ConfigureLogsForPlaybackConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__list_of_logging_strategies
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.ads_interaction_log
    import capo_mediatailor.types.manifest_service_interaction_log


class ConfigureLogsForPlaybackConfigurationRequest(TypedDict, closed=True):
    percent_enabled: "capo_mediatailor.types.__integer.__integer"
    """<p>The percentage of session logs that MediaTailor sends to your CloudWatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to <code>60</code>, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html">debug log mode</a>.</p> <p>Valid values: <code>0</code> - <code>100</code> </p>"""
    playback_configuration_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the playback configuration.</p>"""
    enabled_logging_strategies: NotRequired[
        "capo_mediatailor.types.__list_of_logging_strategies.__listOfLoggingStrategies"
    ]
    """<p>The method used for collecting logs from AWS Elemental MediaTailor. To configure MediaTailor to send logs directly to Amazon CloudWatch Logs, choose <code>LEGACY_CLOUDWATCH</code>. To configure MediaTailor to send logs to CloudWatch, which then vends the logs to your destination of choice, choose <code>VENDED_LOGS</code>. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.</p> <p>To use vended logs, you must configure the delivery destination in Amazon CloudWatch, as described in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2">Enable logging from AWS services, Logging that requires additional permissions [V2]</a>.</p>"""
    ads_interaction_log: NotRequired[
        "capo_mediatailor.types.ads_interaction_log.AdsInteractionLog"
    ]
    """<p>The event types that MediaTailor emits in logs for interactions with the ADS.</p>"""
    manifest_service_interaction_log: NotRequired[
        "capo_mediatailor.types.manifest_service_interaction_log.ManifestServiceInteractionLog"
    ]
    """<p>The event types that MediaTailor emits in logs for interactions with the origin server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsForPlaybackConfigurationRequest) -> dict:
    out: dict = {}
    out["PercentEnabled"] = value.get("percent_enabled", 0)
    out["PlaybackConfigurationName"] = value["playback_configuration_name"]
    if "enabled_logging_strategies" in value:
        import capo_mediatailor.types.__list_of_logging_strategies

        out["EnabledLoggingStrategies"] = (
            capo_mediatailor.types.__list_of_logging_strategies.serialize_json(
                value["enabled_logging_strategies"]
            )
        )
    if "ads_interaction_log" in value:
        import capo_mediatailor.types.ads_interaction_log

        out["AdsInteractionLog"] = (
            capo_mediatailor.types.ads_interaction_log.serialize_json(
                value["ads_interaction_log"]
            )
        )
    if "manifest_service_interaction_log" in value:
        import capo_mediatailor.types.manifest_service_interaction_log

        out["ManifestServiceInteractionLog"] = (
            capo_mediatailor.types.manifest_service_interaction_log.serialize_json(
                value["manifest_service_interaction_log"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsForPlaybackConfigurationRequest:
    out: ConfigureLogsForPlaybackConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PercentEnabled") is not None:
        out["percent_enabled"] = data["PercentEnabled"]
    else:
        out["percent_enabled"] = 0
    if data.get("PlaybackConfigurationName") is not None:
        out["playback_configuration_name"] = data["PlaybackConfigurationName"]
    else:
        raise DeserializationError(
            "ConfigureLogsForPlaybackConfigurationRequest.playback_configuration_name required"
        )
    if data.get("EnabledLoggingStrategies") is not None:
        import capo_mediatailor.types.__list_of_logging_strategies

        out["enabled_logging_strategies"] = (
            capo_mediatailor.types.__list_of_logging_strategies.deserialize_json(
                data["EnabledLoggingStrategies"]
            )
        )
    if data.get("AdsInteractionLog") is not None:
        import capo_mediatailor.types.ads_interaction_log

        out["ads_interaction_log"] = (
            capo_mediatailor.types.ads_interaction_log.deserialize_json(
                data["AdsInteractionLog"]
            )
        )
    if data.get("ManifestServiceInteractionLog") is not None:
        import capo_mediatailor.types.manifest_service_interaction_log

        out["manifest_service_interaction_log"] = (
            capo_mediatailor.types.manifest_service_interaction_log.deserialize_json(
                data["ManifestServiceInteractionLog"]
            )
        )
    return out
