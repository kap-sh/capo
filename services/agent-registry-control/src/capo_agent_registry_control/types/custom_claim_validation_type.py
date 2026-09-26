"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomClaimValidationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.authorizing_claim_match_value_type
    import capo_agent_registry_control.types.inbound_token_claim_name_type
    import capo_agent_registry_control.types.inbound_token_claim_value_type


class CustomClaimValidationType(TypedDict, closed=True):
    inbound_token_claim_name: "capo_agent_registry_control.types.inbound_token_claim_name_type.InboundTokenClaimNameType"
    """<p>The name of the claim in the inbound token to validate.</p>"""
    inbound_token_claim_value_type: "capo_agent_registry_control.types.inbound_token_claim_value_type.InboundTokenClaimValueType"
    """<p>The value type of the claim in the inbound token, either a string or an array of strings.</p>"""
    authorizing_claim_match_value: "capo_agent_registry_control.types.authorizing_claim_match_value_type.AuthorizingClaimMatchValueType"
    """<p>The value and match operator used to authorize the claim.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomClaimValidationType) -> dict:
    out: dict = {}
    out["inboundTokenClaimName"] = value["inbound_token_claim_name"]
    import capo_agent_registry_control.types.inbound_token_claim_value_type

    out["inboundTokenClaimValueType"] = (
        capo_agent_registry_control.types.inbound_token_claim_value_type.serialize_json(
            value["inbound_token_claim_value_type"]
        )
    )
    import capo_agent_registry_control.types.authorizing_claim_match_value_type

    out["authorizingClaimMatchValue"] = (
        capo_agent_registry_control.types.authorizing_claim_match_value_type.serialize_json(
            value["authorizing_claim_match_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomClaimValidationType:
    out: CustomClaimValidationType = {}  # type: ignore[typeddict-item]
    if data.get("inboundTokenClaimName") is not None:
        out["inbound_token_claim_name"] = data["inboundTokenClaimName"]
    else:
        raise DeserializationError(
            "CustomClaimValidationType.inbound_token_claim_name required"
        )
    if data.get("inboundTokenClaimValueType") is not None:
        import capo_agent_registry_control.types.inbound_token_claim_value_type

        out["inbound_token_claim_value_type"] = (
            capo_agent_registry_control.types.inbound_token_claim_value_type.deserialize_json(
                data["inboundTokenClaimValueType"]
            )
        )
    else:
        raise DeserializationError(
            "CustomClaimValidationType.inbound_token_claim_value_type required"
        )
    if data.get("authorizingClaimMatchValue") is not None:
        import capo_agent_registry_control.types.authorizing_claim_match_value_type

        out["authorizing_claim_match_value"] = (
            capo_agent_registry_control.types.authorizing_claim_match_value_type.deserialize_json(
                data["authorizingClaimMatchValue"]
            )
        )
    else:
        raise DeserializationError(
            "CustomClaimValidationType.authorizing_claim_match_value required"
        )
    return out
