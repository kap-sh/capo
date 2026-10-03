"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MappingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.arn_string
    import capo_cognito_identity.types.claim_name
    import capo_cognito_identity.types.claim_value
    import capo_cognito_identity.types.mapping_rule_match_type


class MappingRule(TypedDict, closed=True):
    claim: "capo_cognito_identity.types.claim_name.ClaimName"
    """<p>The claim name that must be present in the token, for example, "isAdmin" or "paid".</p>"""
    match_type: (
        "capo_cognito_identity.types.mapping_rule_match_type.MappingRuleMatchType"
    )
    """<p>The match condition that specifies how closely the claim value in the IdP token must match <code>Value</code>.</p>"""
    value: "capo_cognito_identity.types.claim_value.ClaimValue"
    """<p>A brief string that the claim must match, for example, "paid" or "yes".</p>"""
    role_arn: "capo_cognito_identity.types.arn_string.ARNString"
    """<p>The role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingRule) -> dict:
    out: dict = {}
    out["Claim"] = value["claim"]
    import capo_cognito_identity.types.mapping_rule_match_type

    out["MatchType"] = (
        capo_cognito_identity.types.mapping_rule_match_type.serialize_aws_json_1_1(
            value["match_type"]
        )
    )
    out["Value"] = value["value"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MappingRule:
    out: MappingRule = {}  # type: ignore[typeddict-item]
    if data.get("Claim") is not None:
        out["claim"] = data["Claim"]
    else:
        raise DeserializationError("MappingRule.claim required")
    if data.get("MatchType") is not None:
        import capo_cognito_identity.types.mapping_rule_match_type

        out["match_type"] = (
            capo_cognito_identity.types.mapping_rule_match_type.deserialize_aws_json_1_1(
                data["MatchType"]
            )
        )
    else:
        raise DeserializationError("MappingRule.match_type required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MappingRule.value required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("MappingRule.role_arn required")
    return out
