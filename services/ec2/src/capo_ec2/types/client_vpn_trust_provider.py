"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnTrustProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_device_trust_provider_type
    import capo_ec2.types.string


class ClientVpnTrustProvider(TypedDict, closed=True):
    trust_provider_type: NotRequired[
        "capo_ec2.types.client_vpn_device_trust_provider_type.ClientVpnDeviceTrustProviderType"
    ]
    """<p>The type of the device trust provider. Possible values include:</p> <ul> <li> <p> <code>crowdstrike</code> - CrowdStrike device trust provider.</p> </li> <li> <p> <code>jamf</code> - Jamf device trust provider.</p> </li> <li> <p> <code>jumpcloud</code> - JumpCloud device trust provider.</p> </li> </ul>"""
    tenant_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The tenant ID associated with your device trust provider account.</p>"""
    public_signing_key_url: NotRequired["capo_ec2.types.string.String"]
    """<p>The URL of the public signing key that is used to verify the identity token issued by the device trust provider.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnTrustProvider, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_provider_type" in value:
        import capo_ec2.types.client_vpn_device_trust_provider_type

        capo_ec2.types.client_vpn_device_trust_provider_type.serialize_ec2_query(
            value["trust_provider_type"], pairs, f"{key_prefix}TrustProviderType"
        )
    if "tenant_id" in value:
        pairs.append((f"{key_prefix}TenantId", str(value["tenant_id"])))
    if "public_signing_key_url" in value:
        pairs.append(
            (f"{key_prefix}PublicSigningKeyUrl", str(value["public_signing_key_url"]))
        )


def deserialize_ec2_query(el: Element) -> ClientVpnTrustProvider:
    out: ClientVpnTrustProvider = {}  # type: ignore[typeddict-item]
    child_trust_provider_type = el.find("trustProviderType")
    if child_trust_provider_type is not None:
        import capo_ec2.types.client_vpn_device_trust_provider_type

        out["trust_provider_type"] = (
            capo_ec2.types.client_vpn_device_trust_provider_type.deserialize_ec2_query(
                child_trust_provider_type
            )
        )
    child_tenant_id = el.find("tenantId")
    if child_tenant_id is not None:
        out["tenant_id"] = str(child_tenant_id.text or "")
    child_public_signing_key_url = el.find("publicSigningKeyUrl")
    if child_public_signing_key_url is not None:
        out["public_signing_key_url"] = str(child_public_signing_key_url.text or "")
    return out
