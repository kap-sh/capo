"""Generated from Smithy shape ``com.amazonaws.ec2#VpnAdditionalKeyExchange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_key_exchange_methods_list
    import capo_ec2.types.additional_key_exchange_requirement
    import capo_ec2.types.integer


class VpnAdditionalKeyExchange(TypedDict, closed=True):
    additional_key_exchange_round: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The additional key exchange round number.</p>"""
    key_exchange_methods: NotRequired[
        "capo_ec2.types.additional_key_exchange_methods_list.AdditionalKeyExchangeMethodsList"
    ]
    """<p>The key exchange method numbers permitted for this round.</p>"""
    requirement: NotRequired[
        "capo_ec2.types.additional_key_exchange_requirement.AdditionalKeyExchangeRequirement"
    ]
    """<p>Indicates whether this round is mandatory.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnAdditionalKeyExchange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "additional_key_exchange_round" in value:
        pairs.append(
            (
                f"{key_prefix}AdditionalKeyExchangeRound",
                str(value["additional_key_exchange_round"]),
            )
        )
    if "key_exchange_methods" in value:
        import capo_ec2.types.additional_key_exchange_methods_list

        capo_ec2.types.additional_key_exchange_methods_list.serialize_ec2_query(
            value["key_exchange_methods"], pairs, f"{key_prefix}KeyExchangeMethodSet"
        )
    if "requirement" in value:
        import capo_ec2.types.additional_key_exchange_requirement

        capo_ec2.types.additional_key_exchange_requirement.serialize_ec2_query(
            value["requirement"], pairs, f"{key_prefix}Requirement"
        )


def deserialize_ec2_query(el: Element) -> VpnAdditionalKeyExchange:
    out: VpnAdditionalKeyExchange = {}  # type: ignore[typeddict-item]
    child_additional_key_exchange_round = el.find("additionalKeyExchangeRound")
    if child_additional_key_exchange_round is not None:
        out["additional_key_exchange_round"] = int(
            child_additional_key_exchange_round.text or ""
        )
    child_key_exchange_methods = el.find("keyExchangeMethodSet")
    if child_key_exchange_methods is not None:
        import capo_ec2.types.additional_key_exchange_methods_list

        out["key_exchange_methods"] = (
            capo_ec2.types.additional_key_exchange_methods_list.deserialize_ec2_query(
                child_key_exchange_methods
            )
        )
    child_requirement = el.find("requirement")
    if child_requirement is not None:
        import capo_ec2.types.additional_key_exchange_requirement

        out["requirement"] = (
            capo_ec2.types.additional_key_exchange_requirement.deserialize_ec2_query(
                child_requirement
            )
        )
    return out
