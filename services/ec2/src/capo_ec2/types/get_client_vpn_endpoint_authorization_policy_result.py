"""Generated from Smithy shape ``com.amazonaws.ec2#GetClientVpnEndpointAuthorizationPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_authorization_policy_shadow_mode
    import capo_ec2.types.client_vpn_authorization_policy_status
    import capo_ec2.types.string


class GetClientVpnEndpointAuthorizationPolicyResult(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    policy_document: NotRequired["capo_ec2.types.string.String"]
    """<p>The authorization policy document, written in the Cedar policy language.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the authorization policy.</p>"""
    shadow_mode: NotRequired[
        "capo_ec2.types.client_vpn_authorization_policy_shadow_mode.ClientVpnAuthorizationPolicyShadowMode"
    ]
    """<p>Specifies whether the authorization policy is evaluated in shadow mode. Possible values include:</p> <ul> <li> <p> <code>enabled</code> - The authorization policy is evaluated and the results are logged, but access is not enforced.</p> </li> <li> <p> <code>disabled</code> - The authorization policy is enforced.</p> </li> </ul>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_authorization_policy_status.ClientVpnAuthorizationPolicyStatus"
    ]
    """<p>The current state of the authorization policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetClientVpnEndpointAuthorizationPolicyResult,
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
    if "status" in value:
        import capo_ec2.types.client_vpn_authorization_policy_status

        capo_ec2.types.client_vpn_authorization_policy_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> GetClientVpnEndpointAuthorizationPolicyResult:
    out: GetClientVpnEndpointAuthorizationPolicyResult = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("clientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_policy_document = el.find("policyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_shadow_mode = el.find("shadowMode")
    if child_shadow_mode is not None:
        import capo_ec2.types.client_vpn_authorization_policy_shadow_mode

        out["shadow_mode"] = (
            capo_ec2.types.client_vpn_authorization_policy_shadow_mode.deserialize_ec2_query(
                child_shadow_mode
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_authorization_policy_status

        out["status"] = (
            capo_ec2.types.client_vpn_authorization_policy_status.deserialize_ec2_query(
                child_status
            )
        )
    return out
