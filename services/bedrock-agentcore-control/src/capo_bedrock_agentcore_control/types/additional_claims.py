"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AdditionalClaims``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.additional_claim_name
    import capo_bedrock_agentcore_control.types.additional_claim_value

AdditionalClaims: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.additional_claim_name.AdditionalClaimName",
    "capo_bedrock_agentcore_control.types.additional_claim_value.AdditionalClaimValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalClaims) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalClaims:
    out: AdditionalClaims = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: AdditionalClaims) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
