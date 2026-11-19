"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalKeyExchangesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_additional_key_exchange

AdditionalKeyExchangesList: TypeAlias = list[
    "capo_ec2.types.vpn_additional_key_exchange.VpnAdditionalKeyExchange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalKeyExchangesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_additional_key_exchange

        capo_ec2.types.vpn_additional_key_exchange.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AdditionalKeyExchangesList:
    import capo_ec2.types.vpn_additional_key_exchange

    out: AdditionalKeyExchangesList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.vpn_additional_key_exchange.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AdditionalKeyExchangesList:
    import capo_ec2.types.vpn_additional_key_exchange

    out: AdditionalKeyExchangesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpn_additional_key_exchange.deserialize_ec2_query(child)
        )
    return out
