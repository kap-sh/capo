"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomClaimValidationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type
    import capo_bedrock_agentcore_control.types.inbound_token_claim_name_type
    import capo_bedrock_agentcore_control.types.inbound_token_claim_value_type


class CustomClaimValidationType(TypedDict, closed=True):
    inbound_token_claim_name: "capo_bedrock_agentcore_control.types.inbound_token_claim_name_type.InboundTokenClaimNameType"
    """<p>The name of the custom claim field to check.</p>"""
    inbound_token_claim_value_type: "capo_bedrock_agentcore_control.types.inbound_token_claim_value_type.InboundTokenClaimValueType"
    """<p>The data type of the claim value to check for.</p> <ul> <li> <p>Use <code>STRING</code> if you want to find an exact match to a string you define.</p> </li> <li> <p>Use <code>STRING_ARRAY</code> if you want to fnd a match to at least one value in an array you define.</p> </li> </ul>"""
    authorizing_claim_match_value: "capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type.AuthorizingClaimMatchValueType"
    """<p>Defines the value or values to match for and the relationship of the match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomClaimValidationType) -> dict:
    out: dict = {}
    out["inboundTokenClaimName"] = value["inbound_token_claim_name"]
    import capo_bedrock_agentcore_control.types.inbound_token_claim_value_type

    out["inboundTokenClaimValueType"] = (
        capo_bedrock_agentcore_control.types.inbound_token_claim_value_type.serialize_json(
            value["inbound_token_claim_value_type"]
        )
    )
    import capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type

    out["authorizingClaimMatchValue"] = (
        capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type.serialize_json(
            value["authorizing_claim_match_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomClaimValidationType:
    out: CustomClaimValidationType = {}  # type: ignore[typeddict-item]
    if data.get("inboundTokenClaimName") is not None:
        out["inbound_token_claim_name"] = data["inboundTokenClaimName"]
    else:
        out["inbound_token_claim_name"] = ""
    if data.get("inboundTokenClaimValueType") is not None:
        import capo_bedrock_agentcore_control.types.inbound_token_claim_value_type

        out["inbound_token_claim_value_type"] = (
            capo_bedrock_agentcore_control.types.inbound_token_claim_value_type.deserialize_json(
                data["inboundTokenClaimValueType"]
            )
        )
    else:
        import typing

        out["inbound_token_claim_value_type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.inbound_token_claim_value_type.InboundTokenClaimValueType",
            "",
        )
    if data.get("authorizingClaimMatchValue") is not None:
        import capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type

        out["authorizing_claim_match_value"] = (
            capo_bedrock_agentcore_control.types.authorizing_claim_match_value_type.deserialize_json(
                data["authorizingClaimMatchValue"]
            )
        )
    else:
        raise DeserializationError(
            "CustomClaimValidationType.authorizing_claim_match_value required"
        )
    return out
