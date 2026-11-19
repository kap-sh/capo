"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalKeyExchangesRequestSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_additional_key_exchange_request

AdditionalKeyExchangesRequestSpecification: TypeAlias = list[
    "capo_ec2.types.vpn_additional_key_exchange_request.VpnAdditionalKeyExchangeRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalKeyExchangesRequestSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_additional_key_exchange_request

        capo_ec2.types.vpn_additional_key_exchange_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AdditionalKeyExchangesRequestSpecification:
    import capo_ec2.types.vpn_additional_key_exchange_request

    out: AdditionalKeyExchangesRequestSpecification = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.vpn_additional_key_exchange_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AdditionalKeyExchangesRequestSpecification:
    import capo_ec2.types.vpn_additional_key_exchange_request

    out: AdditionalKeyExchangesRequestSpecification = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpn_additional_key_exchange_request.deserialize_ec2_query(
                child
            )
        )
    return out
