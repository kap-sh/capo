"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizingClaimMatchValueType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.claim_match_operator_type
    import capo_bedrock_agentcore_control.types.claim_match_value_type


class AuthorizingClaimMatchValueType(TypedDict, closed=True):
    claim_match_value: "capo_bedrock_agentcore_control.types.claim_match_value_type.ClaimMatchValueType"
    """<p>The value or values to match for.</p>"""
    claim_match_operator: "capo_bedrock_agentcore_control.types.claim_match_operator_type.ClaimMatchOperatorType"
    """<p>Defines the relationship between the claim field value and the value or values you're matching for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizingClaimMatchValueType) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.claim_match_value_type

    out["claimMatchValue"] = (
        capo_bedrock_agentcore_control.types.claim_match_value_type.serialize_json(
            value["claim_match_value"]
        )
    )
    import capo_bedrock_agentcore_control.types.claim_match_operator_type

    out["claimMatchOperator"] = (
        capo_bedrock_agentcore_control.types.claim_match_operator_type.serialize_json(
            value["claim_match_operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthorizingClaimMatchValueType:
    out: AuthorizingClaimMatchValueType = {}  # type: ignore[typeddict-item]
    if data.get("claimMatchValue") is not None:
        import capo_bedrock_agentcore_control.types.claim_match_value_type

        out["claim_match_value"] = (
            capo_bedrock_agentcore_control.types.claim_match_value_type.deserialize_json(
                data["claimMatchValue"]
            )
        )
    else:
        out["claim_match_value"] = {"$unknown": {"name": ""}}
    if data.get("claimMatchOperator") is not None:
        import capo_bedrock_agentcore_control.types.claim_match_operator_type

        out["claim_match_operator"] = (
            capo_bedrock_agentcore_control.types.claim_match_operator_type.deserialize_json(
                data["claimMatchOperator"]
            )
        )
    else:
        import typing

        out["claim_match_operator"] = typing.cast(
            "capo_bedrock_agentcore_control.types.claim_match_operator_type.ClaimMatchOperatorType",
            "",
        )
    return out
