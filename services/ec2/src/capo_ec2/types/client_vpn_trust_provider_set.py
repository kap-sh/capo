"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnTrustProviderSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_trust_provider

ClientVpnTrustProviderSet: TypeAlias = list[
    "capo_ec2.types.client_vpn_trust_provider.ClientVpnTrustProvider"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnTrustProviderSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.client_vpn_trust_provider

        capo_ec2.types.client_vpn_trust_provider.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ClientVpnTrustProviderSet:
    import capo_ec2.types.client_vpn_trust_provider

    out: ClientVpnTrustProviderSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.client_vpn_trust_provider.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ClientVpnTrustProviderSet:
    import capo_ec2.types.client_vpn_trust_provider

    out: ClientVpnTrustProviderSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.client_vpn_trust_provider.deserialize_ec2_query(child)
        )
    return out
