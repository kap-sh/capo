"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.association_sync_state
    import capo_network_firewall.types.firewall_status_value


class VpcEndpointAssociationStatus(TypedDict, closed=True):
    status: "capo_network_firewall.types.firewall_status_value.FirewallStatusValue"
    """<p>The readiness of the configured firewall endpoint to handle network traffic. </p>"""
    association_sync_state: NotRequired[
        "capo_network_firewall.types.association_sync_state.AssociationSyncState"
    ]
    """<p>The list of the Availability Zone sync states for all subnets that are defined by the firewall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociationStatus) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_status_value

    out["Status"] = (
        capo_network_firewall.types.firewall_status_value.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "association_sync_state" in value:
        import capo_network_firewall.types.association_sync_state

        out["AssociationSyncState"] = (
            capo_network_firewall.types.association_sync_state.serialize_aws_json_1_0(
                value["association_sync_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointAssociationStatus:
    out: VpcEndpointAssociationStatus = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_network_firewall.types.firewall_status_value

        out["status"] = (
            capo_network_firewall.types.firewall_status_value.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_network_firewall.types.firewall_status_value.FirewallStatusValue", ""
        )
    if data.get("AssociationSyncState") is not None:
        import capo_network_firewall.types.association_sync_state

        out["association_sync_state"] = (
            capo_network_firewall.types.association_sync_state.deserialize_aws_json_1_0(
                data["AssociationSyncState"]
            )
        )
    return out
