"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnTunnelOptionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.modify_vpn_tunnel_options_specification
    import capo_ec2.types.string
    import capo_ec2.types.vpn_connection_id


class ModifyVpnTunnelOptionsRequest(TypedDict, closed=True):
    vpn_connection_id: NotRequired["capo_ec2.types.vpn_connection_id.VpnConnectionId"]
    """<p>The ID of the Amazon Web Services Site-to-Site VPN connection.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    tunnel_options: NotRequired[
        "capo_ec2.types.modify_vpn_tunnel_options_specification.ModifyVpnTunnelOptionsSpecification"
    ]
    """<p>The tunnel options to modify.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    skip_tunnel_replacement: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off <code>EnableTunnelLifecycleControl</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    pre_shared_key_storage: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies the storage mode for the pre-shared key (PSK). Valid values are <code>Standard</code> (stored in Site-to-Site VPN service) or <code>SecretsManager</code> (stored in Amazon Web Services Secrets Manager).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpnTunnelOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection_id" in value:
        pairs.append((f"{key_prefix}VpnConnectionId", str(value["vpn_connection_id"])))
    if "vpn_tunnel_outside_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}VpnTunnelOutsideIpAddress",
                str(value["vpn_tunnel_outside_ip_address"]),
            )
        )
    if "tunnel_options" in value:
        import capo_ec2.types.modify_vpn_tunnel_options_specification

        capo_ec2.types.modify_vpn_tunnel_options_specification.serialize_ec2_query(
            value["tunnel_options"], pairs, f"{key_prefix}TunnelOptions"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "skip_tunnel_replacement" in value:
        pairs.append(
            (
                f"{key_prefix}SkipTunnelReplacement",
                "true" if value["skip_tunnel_replacement"] else "false",
            )
        )
    if "pre_shared_key_storage" in value:
        pairs.append(
            (f"{key_prefix}PreSharedKeyStorage", str(value["pre_shared_key_storage"]))
        )


def deserialize_ec2_query(el: Element) -> ModifyVpnTunnelOptionsRequest:
    out: ModifyVpnTunnelOptionsRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_vpn_tunnel_outside_ip_address = el.find("VpnTunnelOutsideIpAddress")
    if child_vpn_tunnel_outside_ip_address is not None:
        out["vpn_tunnel_outside_ip_address"] = str(
            child_vpn_tunnel_outside_ip_address.text or ""
        )
    child_tunnel_options = el.find("TunnelOptions")
    if child_tunnel_options is not None:
        import capo_ec2.types.modify_vpn_tunnel_options_specification

        out["tunnel_options"] = (
            capo_ec2.types.modify_vpn_tunnel_options_specification.deserialize_ec2_query(
                child_tunnel_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_skip_tunnel_replacement = el.find("SkipTunnelReplacement")
    if child_skip_tunnel_replacement is not None:
        out["skip_tunnel_replacement"] = (
            child_skip_tunnel_replacement.text or ""
        ).lower() == "true"
    child_pre_shared_key_storage = el.find("PreSharedKeyStorage")
    if child_pre_shared_key_storage is not None:
        out["pre_shared_key_storage"] = str(child_pre_shared_key_storage.text or "")
    return out


def redact_sensitive(value: ModifyVpnTunnelOptionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tunnel_options" in value:
        out["tunnel_options"] = "*** Sensitive Data Redacted ***"
    return out
