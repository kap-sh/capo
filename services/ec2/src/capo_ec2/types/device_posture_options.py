"""Generated from Smithy shape ``com.amazonaws.ec2#DevicePostureOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_trust_provider_request_list


class DevicePostureOptions(TypedDict, closed=True):
    trust_providers: NotRequired[
        "capo_ec2.types.client_vpn_trust_provider_request_list.ClientVpnTrustProviderRequestList"
    ]
    """<p>The device trust providers to configure for the Client VPN endpoint.</p>"""
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether device posture evaluation is enabled for the Client VPN endpoint. Specify <code>false</code> to disable device posture, which clears the configured device trust providers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DevicePostureOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_providers" in value:
        import capo_ec2.types.client_vpn_trust_provider_request_list

        capo_ec2.types.client_vpn_trust_provider_request_list.serialize_ec2_query(
            value["trust_providers"], pairs, f"{key_prefix}TrustProvider"
        )
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> DevicePostureOptions:
    out: DevicePostureOptions = {}  # type: ignore[typeddict-item]
    child_trust_providers = el.find("TrustProvider")
    if child_trust_providers is not None:
        import capo_ec2.types.client_vpn_trust_provider_request_list

        out["trust_providers"] = (
            capo_ec2.types.client_vpn_trust_provider_request_list.deserialize_ec2_query(
                child_trust_providers
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
