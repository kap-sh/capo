"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RulesConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.mapping_rules_list


class RulesConfigurationType(TypedDict, closed=True):
    rules: "capo_cognito_identity.types.mapping_rules_list.MappingRulesList"
    """<p>An array of rules. You can specify up to 25 rules per identity provider.</p> <p>Rules are evaluated in order. The first one to match specifies the role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RulesConfigurationType) -> dict:
    out: dict = {}
    import capo_cognito_identity.types.mapping_rules_list

    out["Rules"] = (
        capo_cognito_identity.types.mapping_rules_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RulesConfigurationType:
    out: RulesConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("Rules") is not None:
        import capo_cognito_identity.types.mapping_rules_list

        out["rules"] = (
            capo_cognito_identity.types.mapping_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    return out
