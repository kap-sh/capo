"""Generated from Smithy shape ``com.amazonaws.ec2#DevicePostureResponseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_trust_provider_set


class DevicePostureResponseOptions(TypedDict, closed=True):
    trust_providers: NotRequired[
        "capo_ec2.types.client_vpn_trust_provider_set.ClientVpnTrustProviderSet"
    ]
    """<p>The device trust providers configured for the Client VPN endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DevicePostureResponseOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_providers" in value:
        import capo_ec2.types.client_vpn_trust_provider_set

        capo_ec2.types.client_vpn_trust_provider_set.serialize_ec2_query(
            value["trust_providers"], pairs, f"{key_prefix}TrustProviderSet"
        )


def deserialize_ec2_query(el: Element) -> DevicePostureResponseOptions:
    out: DevicePostureResponseOptions = {}  # type: ignore[typeddict-item]
    child_trust_providers = el.find("trustProviderSet")
    if child_trust_providers is not None:
        import capo_ec2.types.client_vpn_trust_provider_set

        out["trust_providers"] = (
            capo_ec2.types.client_vpn_trust_provider_set.deserialize_ec2_query(
                child_trust_providers
            )
        )
    return out
