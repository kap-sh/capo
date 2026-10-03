"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeClientVpnIngressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.string


class AuthorizeClientVpnIngressRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    target_network_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the network for which access is being authorized.</p>"""
    access_group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the group to grant access to, for example, the Active Directory group or identity provider (IdP) group. Required if <code>AuthorizeAllGroups</code> is <code>false</code> or not specified.</p>"""
    authorize_all_groups: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to grant access to all clients. Specify <code>true</code> to grant all clients who successfully establish a VPN connection access to the network. Must be set to <code>true</code> if <code>AccessGroupId</code> is not specified.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the authorization rule.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AuthorizeClientVpnIngressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "target_network_cidr" in value:
        pairs.append(
            (f"{key_prefix}TargetNetworkCidr", str(value["target_network_cidr"]))
        )
    if "access_group_id" in value:
        pairs.append((f"{key_prefix}AccessGroupId", str(value["access_group_id"])))
    if "authorize_all_groups" in value:
        pairs.append(
            (
                f"{key_prefix}AuthorizeAllGroups",
                "true" if value["authorize_all_groups"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AuthorizeClientVpnIngressRequest:
    out: AuthorizeClientVpnIngressRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_target_network_cidr = el.find("TargetNetworkCidr")
    if child_target_network_cidr is not None:
        out["target_network_cidr"] = str(child_target_network_cidr.text or "")
    child_access_group_id = el.find("AccessGroupId")
    if child_access_group_id is not None:
        out["access_group_id"] = str(child_access_group_id.text or "")
    child_authorize_all_groups = el.find("AuthorizeAllGroups")
    if child_authorize_all_groups is not None:
        out["authorize_all_groups"] = (
            child_authorize_all_groups.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
