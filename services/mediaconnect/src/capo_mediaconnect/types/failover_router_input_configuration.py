"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.failover_input_source_priority_mode
    import capo_mediaconnect.types.failover_router_input_protocol_configuration_list
    import capo_mediaconnect.types.router_network_interface_arn


class FailoverRouterInputConfiguration(TypedDict, closed=True):
    network_interface_arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The ARN of the network interface to use for this failover router input.</p>"""
    protocol_configurations: "capo_mediaconnect.types.failover_router_input_protocol_configuration_list.FailoverRouterInputProtocolConfigurationList"
    """<p>A list of exactly two protocol configurations for the failover input sources. Both must use the same protocol type.</p>"""
    source_priority_mode: "capo_mediaconnect.types.failover_input_source_priority_mode.FailoverInputSourcePriorityMode"
    """<p>The mode for determining source priority in failover configurations.</p>"""
    primary_source_index: NotRequired["int"]
    """<p>The index (0 or 1) that specifies which source in the protocol configurations list is currently active. Used to control which of the two failover sources is currently selected. This field is ignored when sourcePriorityMode is set to NO_PRIORITY</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputConfiguration) -> dict:
    out: dict = {}
    out["networkInterfaceArn"] = value["network_interface_arn"]
    import capo_mediaconnect.types.failover_router_input_protocol_configuration_list

    out["protocolConfigurations"] = (
        capo_mediaconnect.types.failover_router_input_protocol_configuration_list.serialize_json(
            value["protocol_configurations"]
        )
    )
    import capo_mediaconnect.types.failover_input_source_priority_mode

    out["sourcePriorityMode"] = (
        capo_mediaconnect.types.failover_input_source_priority_mode.serialize_json(
            value["source_priority_mode"]
        )
    )
    if "primary_source_index" in value:
        out["primarySourceIndex"] = value["primary_source_index"]
    return out


def deserialize_json(data: dict) -> FailoverRouterInputConfiguration:
    out: FailoverRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkInterfaceArn") is not None:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    else:
        out["network_interface_arn"] = ""
    if data.get("protocolConfigurations") is not None:
        import capo_mediaconnect.types.failover_router_input_protocol_configuration_list

        out["protocol_configurations"] = (
            capo_mediaconnect.types.failover_router_input_protocol_configuration_list.deserialize_json(
                data["protocolConfigurations"]
            )
        )
    else:
        out["protocol_configurations"] = []
    if data.get("sourcePriorityMode") is not None:
        import capo_mediaconnect.types.failover_input_source_priority_mode

        out["source_priority_mode"] = (
            capo_mediaconnect.types.failover_input_source_priority_mode.deserialize_json(
                data["sourcePriorityMode"]
            )
        )
    else:
        import typing

        out["source_priority_mode"] = typing.cast(
            "capo_mediaconnect.types.failover_input_source_priority_mode.FailoverInputSourcePriorityMode",
            "",
        )
    if data.get("primarySourceIndex") is not None:
        out["primary_source_index"] = data["primarySourceIndex"]
    return out
