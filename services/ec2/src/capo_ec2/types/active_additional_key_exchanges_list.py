"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveAdditionalKeyExchangesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.active_vpn_tunnel_additional_key_exchange

ActiveAdditionalKeyExchangesList: TypeAlias = list[
    "capo_ec2.types.active_vpn_tunnel_additional_key_exchange.ActiveVpnTunnelAdditionalKeyExchange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ActiveAdditionalKeyExchangesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.active_vpn_tunnel_additional_key_exchange

        capo_ec2.types.active_vpn_tunnel_additional_key_exchange.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ActiveAdditionalKeyExchangesList:
    import capo_ec2.types.active_vpn_tunnel_additional_key_exchange

    out: ActiveAdditionalKeyExchangesList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.active_vpn_tunnel_additional_key_exchange.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ActiveAdditionalKeyExchangesList:
    import capo_ec2.types.active_vpn_tunnel_additional_key_exchange

    out: ActiveAdditionalKeyExchangesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.active_vpn_tunnel_additional_key_exchange.deserialize_ec2_query(
                child
            )
        )
    return out
