"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AuthorizingClaimMatchValueType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.claim_match_operator_type
    import capo_agent_registry_control.types.claim_match_value_type


class AuthorizingClaimMatchValueType(TypedDict, closed=True):
    claim_match_value: (
        "capo_agent_registry_control.types.claim_match_value_type.ClaimMatchValueType"
    )
    """<p>The expected value or values that the claim is compared against.</p>"""
    claim_match_operator: "capo_agent_registry_control.types.claim_match_operator_type.ClaimMatchOperatorType"
    """<p>The operator used to compare the claim value against the expected value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizingClaimMatchValueType) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.claim_match_value_type

    out["claimMatchValue"] = (
        capo_agent_registry_control.types.claim_match_value_type.serialize_json(
            value["claim_match_value"]
        )
    )
    import capo_agent_registry_control.types.claim_match_operator_type

    out["claimMatchOperator"] = (
        capo_agent_registry_control.types.claim_match_operator_type.serialize_json(
            value["claim_match_operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthorizingClaimMatchValueType:
    out: AuthorizingClaimMatchValueType = {}  # type: ignore[typeddict-item]
    if data.get("claimMatchValue") is not None:
        import capo_agent_registry_control.types.claim_match_value_type

        out["claim_match_value"] = (
            capo_agent_registry_control.types.claim_match_value_type.deserialize_json(
                data["claimMatchValue"]
            )
        )
    else:
        raise DeserializationError(
            "AuthorizingClaimMatchValueType.claim_match_value required"
        )
    if data.get("claimMatchOperator") is not None:
        import capo_agent_registry_control.types.claim_match_operator_type

        out["claim_match_operator"] = (
            capo_agent_registry_control.types.claim_match_operator_type.deserialize_json(
                data["claimMatchOperator"]
            )
        )
    else:
        raise DeserializationError(
            "AuthorizingClaimMatchValueType.claim_match_operator required"
        )
    return out
