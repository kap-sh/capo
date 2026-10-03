"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ipam_cidr_authorization_context
    import capo_ec2.types.ipam_external_resource_verification_token_id
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.string
    import capo_ec2.types.verification_method


class ProvisionIpamPoolCidrRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool to which you want to assign a CIDR.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR you want to assign to the IPAM pool. Either "NetmaskLength" or "Cidr" is required. This value will be null if you specify "NetmaskLength" and will be filled in during the provisioning process.</p>"""
    cidr_authorization_context: NotRequired[
        "capo_ec2.types.ipam_cidr_authorization_context.IpamCidrAuthorizationContext"
    ]
    """<p>A signed document that proves that you are authorized to bring a specified IP address range to Amazon using BYOIP. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""
    netmask_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. Either "NetmaskLength" or "Cidr" is required.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    verification_method: NotRequired[
        "capo_ec2.types.verification_method.VerificationMethod"
    ]
    """<p>The method for verifying control of a public IP address range. Defaults to <code>remarks-x509</code> if not specified. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""
    ipam_external_resource_verification_token_id: NotRequired[
        "capo_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>Verification token ID. This option only applies to IPv4 and IPv6 pools in the public scope.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProvisionIpamPoolCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "cidr_authorization_context" in value:
        import capo_ec2.types.ipam_cidr_authorization_context

        capo_ec2.types.ipam_cidr_authorization_context.serialize_ec2_query(
            value["cidr_authorization_context"],
            pairs,
            f"{key_prefix}CidrAuthorizationContext",
        )
    if "netmask_length" in value:
        pairs.append((f"{key_prefix}NetmaskLength", str(value["netmask_length"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "verification_method" in value:
        import capo_ec2.types.verification_method

        capo_ec2.types.verification_method.serialize_ec2_query(
            value["verification_method"], pairs, f"{key_prefix}VerificationMethod"
        )
    if "ipam_external_resource_verification_token_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamExternalResourceVerificationTokenId",
                str(value["ipam_external_resource_verification_token_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ProvisionIpamPoolCidrRequest:
    out: ProvisionIpamPoolCidrRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_cidr_authorization_context = el.find("CidrAuthorizationContext")
    if child_cidr_authorization_context is not None:
        import capo_ec2.types.ipam_cidr_authorization_context

        out["cidr_authorization_context"] = (
            capo_ec2.types.ipam_cidr_authorization_context.deserialize_ec2_query(
                child_cidr_authorization_context
            )
        )
    child_netmask_length = el.find("NetmaskLength")
    if child_netmask_length is not None:
        out["netmask_length"] = int(child_netmask_length.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_verification_method = el.find("VerificationMethod")
    if child_verification_method is not None:
        import capo_ec2.types.verification_method

        out["verification_method"] = (
            capo_ec2.types.verification_method.deserialize_ec2_query(
                child_verification_method
            )
        )
    child_ipam_external_resource_verification_token_id = el.find(
        "IpamExternalResourceVerificationTokenId"
    )
    if child_ipam_external_resource_verification_token_id is not None:
        out["ipam_external_resource_verification_token_id"] = str(
            child_ipam_external_resource_verification_token_id.text or ""
        )
    return out
