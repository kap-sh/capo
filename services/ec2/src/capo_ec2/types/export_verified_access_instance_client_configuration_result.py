"""Generated from Smithy shape ``com.amazonaws.ec2#ExportVerifiedAccessInstanceClientConfigurationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.device_trust_provider_type_list
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list
    import capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration


class ExportVerifiedAccessInstanceClientConfigurationResult(TypedDict, closed=True):
    version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version.</p>"""
    verified_access_instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Verified Access instance.</p>"""
    region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region.</p>"""
    device_trust_providers: NotRequired[
        "capo_ec2.types.device_trust_provider_type_list.DeviceTrustProviderTypeList"
    ]
    """<p>The device trust providers.</p>"""
    user_trust_provider: NotRequired[
        "capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration.VerifiedAccessInstanceUserTrustProviderClientConfiguration"
    ]
    """<p>The user identity trust provider.</p>"""
    open_vpn_configurations: NotRequired[
        "capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list.VerifiedAccessInstanceOpenVpnClientConfigurationList"
    ]
    """<p>The Open VPN configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportVerifiedAccessInstanceClientConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
            )
        )
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "device_trust_providers" in value:
        import capo_ec2.types.device_trust_provider_type_list

        capo_ec2.types.device_trust_provider_type_list.serialize_ec2_query(
            value["device_trust_providers"],
            pairs,
            f"{key_prefix}DeviceTrustProviderSet",
        )
    if "user_trust_provider" in value:
        import capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration

        capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration.serialize_ec2_query(
            value["user_trust_provider"], pairs, f"{key_prefix}UserTrustProvider"
        )
    if "open_vpn_configurations" in value:
        import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list

        capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list.serialize_ec2_query(
            value["open_vpn_configurations"],
            pairs,
            f"{key_prefix}OpenVpnConfigurationSet",
        )


def deserialize_ec2_query(
    el: Element,
) -> ExportVerifiedAccessInstanceClientConfigurationResult:
    out: ExportVerifiedAccessInstanceClientConfigurationResult = {}  # type: ignore[typeddict-item]
    child_version = el.find("version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    child_verified_access_instance_id = el.find("verifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_region = el.find("region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_device_trust_providers = el.find("deviceTrustProviderSet")
    if child_device_trust_providers is not None:
        import capo_ec2.types.device_trust_provider_type_list

        out["device_trust_providers"] = (
            capo_ec2.types.device_trust_provider_type_list.deserialize_ec2_query(
                child_device_trust_providers
            )
        )
    child_user_trust_provider = el.find("userTrustProvider")
    if child_user_trust_provider is not None:
        import capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration

        out["user_trust_provider"] = (
            capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration.deserialize_ec2_query(
                child_user_trust_provider
            )
        )
    child_open_vpn_configurations = el.find("openVpnConfigurationSet")
    if child_open_vpn_configurations is not None:
        import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list

        out["open_vpn_configurations"] = (
            capo_ec2.types.verified_access_instance_open_vpn_client_configuration_list.deserialize_ec2_query(
                child_open_vpn_configurations
            )
        )
    return out


def redact_sensitive(
    value: ExportVerifiedAccessInstanceClientConfigurationResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_trust_provider" in value:
        import capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration

        out["user_trust_provider"] = (
            capo_ec2.types.verified_access_instance_user_trust_provider_client_configuration.redact_sensitive(
                value["user_trust_provider"]
            )
        )
    return out
