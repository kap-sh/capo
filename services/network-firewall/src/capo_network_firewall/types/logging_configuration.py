"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.log_destination_configs


class LoggingConfiguration(TypedDict, closed=True):
    log_destination_configs: (
        "capo_network_firewall.types.log_destination_configs.LogDestinationConfigs"
    )
    """<p>Defines the logging destinations for the logs for a firewall. Network Firewall generates logs for stateful rule groups. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LoggingConfiguration) -> dict:
    out: dict = {}
    import capo_network_firewall.types.log_destination_configs

    out["LogDestinationConfigs"] = (
        capo_network_firewall.types.log_destination_configs.serialize_aws_json_1_0(
            value["log_destination_configs"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogDestinationConfigs") is not None:
        import capo_network_firewall.types.log_destination_configs

        out["log_destination_configs"] = (
            capo_network_firewall.types.log_destination_configs.deserialize_aws_json_1_0(
                data["LogDestinationConfigs"]
            )
        )
    else:
        out["log_destination_configs"] = []
    return out
