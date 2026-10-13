"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConnectionsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_connection_list


class DescribeVpnConnectionsResult(TypedDict, closed=True):
    vpn_connections: NotRequired["capo_ec2.types.vpn_connection_list.VpnConnectionList"]
    """<p>Information about one or more VPN connections.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connections" in value:
        import capo_ec2.types.vpn_connection_list

        capo_ec2.types.vpn_connection_list.serialize_ec2_query(
            value["vpn_connections"], pairs, f"{key_prefix}VpnConnectionSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpnConnectionsResult:
    out: DescribeVpnConnectionsResult = {}  # type: ignore[typeddict-item]
    child_vpn_connections = el.find("vpnConnectionSet")
    if child_vpn_connections is not None:
        import capo_ec2.types.vpn_connection_list

        out["vpn_connections"] = (
            capo_ec2.types.vpn_connection_list.deserialize_ec2_query(
                child_vpn_connections
            )
        )
    return out


def redact_sensitive(value: DescribeVpnConnectionsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vpn_connections" in value:
        import capo_ec2.types.vpn_connection_list

        out["vpn_connections"] = capo_ec2.types.vpn_connection_list.redact_sensitive(
            value["vpn_connections"]
        )
    return out
