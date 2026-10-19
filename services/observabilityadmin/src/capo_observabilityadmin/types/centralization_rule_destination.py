"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.account_identifier
    import capo_observabilityadmin.types.destination_logs_configuration
    import capo_observabilityadmin.types.destination_metrics_configuration
    import capo_observabilityadmin.types.region


class CentralizationRuleDestination(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.region.Region"
    """<p>The primary destination region to which telemetry data should be centralized.</p>"""
    account: NotRequired[
        "capo_observabilityadmin.types.account_identifier.AccountIdentifier"
    ]
    """<p>The destination account (within the organization) to which the telemetry data should be centralized.</p>"""
    destination_logs_configuration: NotRequired[
        "capo_observabilityadmin.types.destination_logs_configuration.DestinationLogsConfiguration"
    ]
    """<p>Log specific configuration for centralization destination log groups.</p>"""
    destination_metrics_configuration: NotRequired[
        "capo_observabilityadmin.types.destination_metrics_configuration.DestinationMetricsConfiguration"
    ]
    """<p>Metric specific configuration for centralization destination metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleDestination) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "account" in value:
        out["Account"] = value["account"]
    if "destination_logs_configuration" in value:
        import capo_observabilityadmin.types.destination_logs_configuration

        out["DestinationLogsConfiguration"] = (
            capo_observabilityadmin.types.destination_logs_configuration.serialize_json(
                value["destination_logs_configuration"]
            )
        )
    if "destination_metrics_configuration" in value:
        import capo_observabilityadmin.types.destination_metrics_configuration

        out["DestinationMetricsConfiguration"] = (
            capo_observabilityadmin.types.destination_metrics_configuration.serialize_json(
                value["destination_metrics_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CentralizationRuleDestination:
    out: CentralizationRuleDestination = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    if data.get("DestinationLogsConfiguration") is not None:
        import capo_observabilityadmin.types.destination_logs_configuration

        out["destination_logs_configuration"] = (
            capo_observabilityadmin.types.destination_logs_configuration.deserialize_json(
                data["DestinationLogsConfiguration"]
            )
        )
    if data.get("DestinationMetricsConfiguration") is not None:
        import capo_observabilityadmin.types.destination_metrics_configuration

        out["destination_metrics_configuration"] = (
            capo_observabilityadmin.types.destination_metrics_configuration.deserialize_json(
                data["DestinationMetricsConfiguration"]
            )
        )
    return out
