"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyClientVpnEndpointAuthorizationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_authorization_policy_shadow_mode
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.string


class ModifyClientVpnEndpointAuthorizationPolicyRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The authorization policy document, written in the Cedar policy language. This parameter is required when you create the authorization policy for a Client VPN endpoint that does not already have one.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the authorization policy.</p>"""
    shadow_mode: NotRequired[
        "capo_ec2.types.client_vpn_authorization_policy_shadow_mode.ClientVpnAuthorizationPolicyShadowMode"
    ]
    """<p>Specifies whether the authorization policy is evaluated in shadow mode. Possible values include:</p> <ul> <li> <p> <code>enabled</code> - The authorization policy is evaluated and the results are logged, but access is not enforced.</p> </li> <li> <p> <code>disabled</code> - The authorization policy is enforced.</p> </li> </ul> <p>The default value is <code>disabled</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyClientVpnEndpointAuthorizationPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "policy_document" in value:
        pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "shadow_mode" in value:
        import capo_ec2.types.client_vpn_authorization_policy_shadow_mode

        capo_ec2.types.client_vpn_authorization_policy_shadow_mode.serialize_ec2_query(
            value["shadow_mode"], pairs, f"{key_prefix}ShadowMode"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyClientVpnEndpointAuthorizationPolicyRequest:
    out: ModifyClientVpnEndpointAuthorizationPolicyRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_shadow_mode = el.find("ShadowMode")
    if child_shadow_mode is not None:
        import capo_ec2.types.client_vpn_authorization_policy_shadow_mode

        out["shadow_mode"] = (
            capo_ec2.types.client_vpn_authorization_policy_shadow_mode.deserialize_ec2_query(
                child_shadow_mode
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
