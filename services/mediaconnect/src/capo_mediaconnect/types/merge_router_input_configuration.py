"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.merge_router_input_protocol_configuration_list
    import capo_mediaconnect.types.router_network_interface_arn


class MergeRouterInputConfiguration(TypedDict, closed=True):
    network_interface_arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The ARN of the network interface to use for this merge router input.</p>"""
    protocol_configurations: "capo_mediaconnect.types.merge_router_input_protocol_configuration_list.MergeRouterInputProtocolConfigurationList"
    """<p>A list of exactly two protocol configurations for the merge input sources. Both must use the same protocol type.</p>"""
    merge_recovery_window_milliseconds: "int"
    """<p>The time window in milliseconds for merging the two input sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputConfiguration) -> dict:
    out: dict = {}
    out["networkInterfaceArn"] = value["network_interface_arn"]
    import capo_mediaconnect.types.merge_router_input_protocol_configuration_list

    out["protocolConfigurations"] = (
        capo_mediaconnect.types.merge_router_input_protocol_configuration_list.serialize_json(
            value["protocol_configurations"]
        )
    )
    out["mergeRecoveryWindowMilliseconds"] = value["merge_recovery_window_milliseconds"]
    return out


def deserialize_json(data: dict) -> MergeRouterInputConfiguration:
    out: MergeRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkInterfaceArn") is not None:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    else:
        out["network_interface_arn"] = ""
    if data.get("protocolConfigurations") is not None:
        import capo_mediaconnect.types.merge_router_input_protocol_configuration_list

        out["protocol_configurations"] = (
            capo_mediaconnect.types.merge_router_input_protocol_configuration_list.deserialize_json(
                data["protocolConfigurations"]
            )
        )
    else:
        out["protocol_configurations"] = []
    if data.get("mergeRecoveryWindowMilliseconds") is not None:
        out["merge_recovery_window_milliseconds"] = data[
            "mergeRecoveryWindowMilliseconds"
        ]
    else:
        out["merge_recovery_window_milliseconds"] = 0
    return out
