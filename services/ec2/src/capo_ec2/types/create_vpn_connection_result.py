"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConnectionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_connection


class CreateVpnConnectionResult(TypedDict, closed=True):
    vpn_connection: NotRequired["capo_ec2.types.vpn_connection.VpnConnection"]
    """<p>Information about the VPN connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnConnectionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection" in value:
        import capo_ec2.types.vpn_connection

        capo_ec2.types.vpn_connection.serialize_ec2_query(
            value["vpn_connection"], pairs, f"{key_prefix}VpnConnection"
        )


def deserialize_ec2_query(el: Element) -> CreateVpnConnectionResult:
    out: CreateVpnConnectionResult = {}  # type: ignore[typeddict-item]
    child_vpn_connection = el.find("vpnConnection")
    if child_vpn_connection is not None:
        import capo_ec2.types.vpn_connection

        out["vpn_connection"] = capo_ec2.types.vpn_connection.deserialize_ec2_query(
            child_vpn_connection
        )
    return out


def redact_sensitive(value: CreateVpnConnectionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vpn_connection" in value:
        import capo_ec2.types.vpn_connection

        out["vpn_connection"] = capo_ec2.types.vpn_connection.redact_sensitive(
            value["vpn_connection"]
        )
    return out
