"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.capacity_usage_summary
    import capo_network_firewall.types.configuration_sync_state
    import capo_network_firewall.types.firewall_status_value
    import capo_network_firewall.types.sync_states
    import capo_network_firewall.types.transit_gateway_attachment_sync_state


class FirewallStatus(TypedDict, closed=True):
    status: "capo_network_firewall.types.firewall_status_value.FirewallStatusValue"
    """<p>The readiness of the configured firewall to handle network traffic across all of the Availability Zones where you have it configured. This setting is <code>READY</code> only when the <code>ConfigurationSyncStateSummary</code> value is <code>IN_SYNC</code> and the <code>Attachment</code> <code>Status</code> values for all of the configured subnets are <code>READY</code>. </p>"""
    configuration_sync_state_summary: (
        "capo_network_firewall.types.configuration_sync_state.ConfigurationSyncState"
    )
    """<p>The configuration sync state for the firewall. This summarizes the <code>Config</code> settings in the <code>SyncStates</code> for this firewall status object. </p> <p>When you create a firewall or update its configuration, for example by adding a rule group to its firewall policy, Network Firewall distributes the configuration changes to all Availability Zones that have subnets defined for the firewall. This summary indicates whether the configuration changes have been applied everywhere. </p> <p>This status must be <code>IN_SYNC</code> for the firewall to be ready for use, but it doesn't indicate that the firewall is ready. The <code>Status</code> setting indicates firewall readiness. It's based on this setting and the readiness of the firewall endpoints to take traffic. </p>"""
    sync_states: NotRequired["capo_network_firewall.types.sync_states.SyncStates"]
    """<p>Status for the subnets that you've configured in the firewall. This contains one array element per Availability Zone where you've configured a subnet in the firewall. </p> <p>These objects provide detailed information for the settings <code>ConfigurationSyncStateSummary</code> and <code>Status</code>. </p>"""
    capacity_usage_summary: NotRequired[
        "capo_network_firewall.types.capacity_usage_summary.CapacityUsageSummary"
    ]
    """<p>Describes the capacity usage of the resources contained in a firewall's reference sets. Network Firewall calculates the capacity usage by taking an aggregated count of all of the resources used by all of the reference sets in a firewall.</p>"""
    transit_gateway_attachment_sync_state: NotRequired[
        "capo_network_firewall.types.transit_gateway_attachment_sync_state.TransitGatewayAttachmentSyncState"
    ]
    """<p>The synchronization state of the transit gateway attachment. This indicates whether the firewall's transit gateway configuration is properly synchronized and operational. Use this to verify that your transit gateway configuration changes have been applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallStatus) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_status_value

    out["Status"] = (
        capo_network_firewall.types.firewall_status_value.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_network_firewall.types.configuration_sync_state

    out["ConfigurationSyncStateSummary"] = (
        capo_network_firewall.types.configuration_sync_state.serialize_aws_json_1_0(
            value["configuration_sync_state_summary"]
        )
    )
    if "sync_states" in value:
        import capo_network_firewall.types.sync_states

        out["SyncStates"] = (
            capo_network_firewall.types.sync_states.serialize_aws_json_1_0(
                value["sync_states"]
            )
        )
    if "capacity_usage_summary" in value:
        import capo_network_firewall.types.capacity_usage_summary

        out["CapacityUsageSummary"] = (
            capo_network_firewall.types.capacity_usage_summary.serialize_aws_json_1_0(
                value["capacity_usage_summary"]
            )
        )
    if "transit_gateway_attachment_sync_state" in value:
        import capo_network_firewall.types.transit_gateway_attachment_sync_state

        out["TransitGatewayAttachmentSyncState"] = (
            capo_network_firewall.types.transit_gateway_attachment_sync_state.serialize_aws_json_1_0(
                value["transit_gateway_attachment_sync_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallStatus:
    out: FirewallStatus = {}  # type: ignore[typeddict-item]
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
    if data.get("ConfigurationSyncStateSummary") is not None:
        import capo_network_firewall.types.configuration_sync_state

        out["configuration_sync_state_summary"] = (
            capo_network_firewall.types.configuration_sync_state.deserialize_aws_json_1_0(
                data["ConfigurationSyncStateSummary"]
            )
        )
    else:
        import typing

        out["configuration_sync_state_summary"] = typing.cast(
            "capo_network_firewall.types.configuration_sync_state.ConfigurationSyncState",
            "",
        )
    if data.get("SyncStates") is not None:
        import capo_network_firewall.types.sync_states

        out["sync_states"] = (
            capo_network_firewall.types.sync_states.deserialize_aws_json_1_0(
                data["SyncStates"]
            )
        )
    if data.get("CapacityUsageSummary") is not None:
        import capo_network_firewall.types.capacity_usage_summary

        out["capacity_usage_summary"] = (
            capo_network_firewall.types.capacity_usage_summary.deserialize_aws_json_1_0(
                data["CapacityUsageSummary"]
            )
        )
    if data.get("TransitGatewayAttachmentSyncState") is not None:
        import capo_network_firewall.types.transit_gateway_attachment_sync_state

        out["transit_gateway_attachment_sync_state"] = (
            capo_network_firewall.types.transit_gateway_attachment_sync_state.deserialize_aws_json_1_0(
                data["TransitGatewayAttachmentSyncState"]
            )
        )
    return out
