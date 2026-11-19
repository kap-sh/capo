"""Generated from Smithy shape ``com.amazonaws.ec2#VpnAdditionalKeyExchangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_key_exchange_methods_request_list
    import capo_ec2.types.additional_key_exchange_requirement
    import capo_ec2.types.additional_key_exchange_round


class VpnAdditionalKeyExchangeRequest(TypedDict, closed=True):
    additional_key_exchange_round: NotRequired[
        "capo_ec2.types.additional_key_exchange_round.AdditionalKeyExchangeRound"
    ]
    """<p>The additional key exchange round number.</p> <p>Valid range: Minimum value of 1. Maximum value of 7.</p>"""
    key_exchange_methods: NotRequired[
        "capo_ec2.types.additional_key_exchange_methods_request_list.AdditionalKeyExchangeMethodsRequestList"
    ]
    """<p>The key exchange method numbers that are permitted for this round. The method numbers are the IANA IKEv2 key exchange method transform IDs.</p> <p>A <code>required</code> round must specify at least one method. An <code>optional</code> round can omit this parameter or specify an empty list. If omitted or empty for an optional round, the round is disabled.</p> <p>IKEv2 requires that the initial Diffie-Hellman exchange and each required round use a different key exchange method. The permitted methods must allow a distinct method to be selected for each of them.</p> <p>Valid values: <code>2</code> | <code>5</code> | <code>14</code> | <code>15</code> | <code>16</code> | <code>17</code> | <code>18</code> | <code>19</code> | <code>20</code> | <code>21</code> | <code>22</code> | <code>23</code> | <code>24</code> | <code>35</code> | <code>36</code> | <code>37</code> </p>"""
    requirement: NotRequired[
        "capo_ec2.types.additional_key_exchange_requirement.AdditionalKeyExchangeRequirement"
    ]
    """<p>Indicates whether this round is mandatory. If <code>required</code>, the tunnel isn't established unless the customer gateway device negotiates this round. If <code>optional</code>, the round is negotiated only if the customer gateway device supports it.</p> <p>Valid values: <code>required</code> | <code>optional</code> </p> <p>Default: <code>required</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnAdditionalKeyExchangeRequest, pairs: list[tuple[str, str]], prefix: str
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
        import capo_ec2.types.additional_key_exchange_methods_request_list

        capo_ec2.types.additional_key_exchange_methods_request_list.serialize_ec2_query(
            value["key_exchange_methods"], pairs, f"{key_prefix}KeyExchangeMethod"
        )
    if "requirement" in value:
        import capo_ec2.types.additional_key_exchange_requirement

        capo_ec2.types.additional_key_exchange_requirement.serialize_ec2_query(
            value["requirement"], pairs, f"{key_prefix}Requirement"
        )


def deserialize_ec2_query(el: Element) -> VpnAdditionalKeyExchangeRequest:
    out: VpnAdditionalKeyExchangeRequest = {}  # type: ignore[typeddict-item]
    child_additional_key_exchange_round = el.find("AdditionalKeyExchangeRound")
    if child_additional_key_exchange_round is not None:
        out["additional_key_exchange_round"] = int(
            child_additional_key_exchange_round.text or ""
        )
    child_key_exchange_methods = el.find("KeyExchangeMethod")
    if child_key_exchange_methods is not None:
        import capo_ec2.types.additional_key_exchange_methods_request_list

        out["key_exchange_methods"] = (
            capo_ec2.types.additional_key_exchange_methods_request_list.deserialize_ec2_query(
                child_key_exchange_methods
            )
        )
    child_requirement = el.find("Requirement")
    if child_requirement is not None:
        import capo_ec2.types.additional_key_exchange_requirement

        out["requirement"] = (
            capo_ec2.types.additional_key_exchange_requirement.deserialize_ec2_query(
                child_requirement
            )
        )
    return out
