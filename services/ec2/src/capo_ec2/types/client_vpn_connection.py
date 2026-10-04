"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_connection_status
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class ClientVpnConnection(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint to which the client is connected.</p>"""
    timestamp: NotRequired["capo_ec2.types.string.String"]
    """<p>The current date and time.</p>"""
    connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the client connection.</p>"""
    username: NotRequired["capo_ec2.types.string.String"]
    """<p>The username of the client who established the client connection. This information is only provided if Active Directory client authentication is used.</p>"""
    connection_established_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the client connection was established.</p>"""
    ingress_bytes: NotRequired["capo_ec2.types.string.String"]
    """<p>The number of bytes sent by the client.</p>"""
    egress_bytes: NotRequired["capo_ec2.types.string.String"]
    """<p>The number of bytes received by the client.</p>"""
    ingress_packets: NotRequired["capo_ec2.types.string.String"]
    """<p>The number of packets sent by the client.</p>"""
    egress_packets: NotRequired["capo_ec2.types.string.String"]
    """<p>The number of packets received by the client.</p>"""
    client_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address of the client.</p>"""
    client_ipv6_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 address assigned to the client connection when using a dual-stack Client VPN endpoint. This field is only populated when the endpoint is configured for dual-stack addressing, and the client is using IPv6 for connectivity.</p>"""
    common_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The common name associated with the client. This is either the name of the client certificate, or the Active Directory user name.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>The current state of the client connection.</p>"""
    connection_end_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the client connection was terminated.</p>"""
    posture_compliance_statuses: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The statuses returned by the client connect handler for posture compliance, if applicable.</p>"""
    authorization_policy_last_evaluated_time: NotRequired[
        "capo_ec2.types.string.String"
    ]
    """<p>The date and time the authorization policy was last evaluated for the client connection, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "timestamp" in value:
        pairs.append((f"{key_prefix}Timestamp", str(value["timestamp"])))
    if "connection_id" in value:
        pairs.append((f"{key_prefix}ConnectionId", str(value["connection_id"])))
    if "username" in value:
        pairs.append((f"{key_prefix}Username", str(value["username"])))
    if "connection_established_time" in value:
        pairs.append(
            (
                f"{key_prefix}ConnectionEstablishedTime",
                str(value["connection_established_time"]),
            )
        )
    if "ingress_bytes" in value:
        pairs.append((f"{key_prefix}IngressBytes", str(value["ingress_bytes"])))
    if "egress_bytes" in value:
        pairs.append((f"{key_prefix}EgressBytes", str(value["egress_bytes"])))
    if "ingress_packets" in value:
        pairs.append((f"{key_prefix}IngressPackets", str(value["ingress_packets"])))
    if "egress_packets" in value:
        pairs.append((f"{key_prefix}EgressPackets", str(value["egress_packets"])))
    if "client_ip" in value:
        pairs.append((f"{key_prefix}ClientIp", str(value["client_ip"])))
    if "client_ipv6_address" in value:
        pairs.append(
            (f"{key_prefix}ClientIpv6Address", str(value["client_ipv6_address"]))
        )
    if "common_name" in value:
        pairs.append((f"{key_prefix}CommonName", str(value["common_name"])))
    if "status" in value:
        import capo_ec2.types.client_vpn_connection_status

        capo_ec2.types.client_vpn_connection_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "connection_end_time" in value:
        pairs.append(
            (f"{key_prefix}ConnectionEndTime", str(value["connection_end_time"]))
        )
    if "posture_compliance_statuses" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["posture_compliance_statuses"],
            pairs,
            f"{key_prefix}PostureComplianceStatusSet",
        )
    if "authorization_policy_last_evaluated_time" in value:
        pairs.append(
            (
                f"{key_prefix}AuthorizationPolicyLastEvaluatedTime",
                str(value["authorization_policy_last_evaluated_time"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ClientVpnConnection:
    out: ClientVpnConnection = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("clientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_timestamp = el.find("timestamp")
    if child_timestamp is not None:
        out["timestamp"] = str(child_timestamp.text or "")
    child_connection_id = el.find("connectionId")
    if child_connection_id is not None:
        out["connection_id"] = str(child_connection_id.text or "")
    child_username = el.find("username")
    if child_username is not None:
        out["username"] = str(child_username.text or "")
    child_connection_established_time = el.find("connectionEstablishedTime")
    if child_connection_established_time is not None:
        out["connection_established_time"] = str(
            child_connection_established_time.text or ""
        )
    child_ingress_bytes = el.find("ingressBytes")
    if child_ingress_bytes is not None:
        out["ingress_bytes"] = str(child_ingress_bytes.text or "")
    child_egress_bytes = el.find("egressBytes")
    if child_egress_bytes is not None:
        out["egress_bytes"] = str(child_egress_bytes.text or "")
    child_ingress_packets = el.find("ingressPackets")
    if child_ingress_packets is not None:
        out["ingress_packets"] = str(child_ingress_packets.text or "")
    child_egress_packets = el.find("egressPackets")
    if child_egress_packets is not None:
        out["egress_packets"] = str(child_egress_packets.text or "")
    child_client_ip = el.find("clientIp")
    if child_client_ip is not None:
        out["client_ip"] = str(child_client_ip.text or "")
    child_client_ipv6_address = el.find("clientIpv6Address")
    if child_client_ipv6_address is not None:
        out["client_ipv6_address"] = str(child_client_ipv6_address.text or "")
    child_common_name = el.find("commonName")
    if child_common_name is not None:
        out["common_name"] = str(child_common_name.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_connection_status

        out["status"] = (
            capo_ec2.types.client_vpn_connection_status.deserialize_ec2_query(
                child_status
            )
        )
    child_connection_end_time = el.find("connectionEndTime")
    if child_connection_end_time is not None:
        out["connection_end_time"] = str(child_connection_end_time.text or "")
    child_posture_compliance_statuses = el.find("postureComplianceStatusSet")
    if child_posture_compliance_statuses is not None:
        import capo_ec2.types.value_string_list

        out["posture_compliance_statuses"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_posture_compliance_statuses
            )
        )
    child_authorization_policy_last_evaluated_time = el.find(
        "authorizationPolicyLastEvaluatedTime"
    )
    if child_authorization_policy_last_evaluated_time is not None:
        out["authorization_policy_last_evaluated_time"] = str(
            child_authorization_policy_last_evaluated_time.text or ""
        )
    return out
