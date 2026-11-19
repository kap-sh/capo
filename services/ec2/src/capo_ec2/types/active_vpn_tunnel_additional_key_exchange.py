"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveVpnTunnelAdditionalKeyExchange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class ActiveVpnTunnelAdditionalKeyExchange(TypedDict, closed=True):
    additional_key_exchange_round: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The additional key exchange round number.</p>"""
    key_exchange_method: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The key exchange method number negotiated for this round.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ActiveVpnTunnelAdditionalKeyExchange,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "additional_key_exchange_round" in value:
        pairs.append(
            (
                f"{key_prefix}AdditionalKeyExchangeRound",
                str(value["additional_key_exchange_round"]),
            )
        )
    if "key_exchange_method" in value:
        pairs.append(
            (f"{key_prefix}KeyExchangeMethod", str(value["key_exchange_method"]))
        )


def deserialize_ec2_query(el: Element) -> ActiveVpnTunnelAdditionalKeyExchange:
    out: ActiveVpnTunnelAdditionalKeyExchange = {}  # type: ignore[typeddict-item]
    child_additional_key_exchange_round = el.find("additionalKeyExchangeRound")
    if child_additional_key_exchange_round is not None:
        out["additional_key_exchange_round"] = int(
            child_additional_key_exchange_round.text or ""
        )
    child_key_exchange_method = el.find("keyExchangeMethod")
    if child_key_exchange_method is not None:
        out["key_exchange_method"] = int(child_key_exchange_method.text or "")
    return out
