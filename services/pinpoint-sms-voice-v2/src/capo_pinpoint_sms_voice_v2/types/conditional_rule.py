"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionalRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.conditional_field_behavior
    import capo_pinpoint_sms_voice_v2.types.conditional_validation
    import capo_pinpoint_sms_voice_v2.types.field_condition_list


class ConditionalRule(TypedDict, closed=True):
    conditions: (
        "capo_pinpoint_sms_voice_v2.types.field_condition_list.FieldConditionList"
    )
    """<p>The conditions that must all evaluate to true for this rule to match. Conditions are combined with logical AND. Use multiple rules with the same <b>RuleBehavior</b> to express logical OR.</p>"""
    rule_behavior: "capo_pinpoint_sms_voice_v2.types.conditional_field_behavior.ConditionalFieldBehavior"
    """<p>The field behavior that applies when all conditions in this rule match. Valid values are <b>REQUIRED</b>, <b>OPTIONAL</b>, and <b>DISALLOWED</b>.</p>"""
    conditional_validation: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.conditional_validation.ConditionalValidation"
    ]
    """<p>Optional per-rule validation constraints (minimum length, maximum length, regex pattern, allowed select values) that override the field's default validation when this rule matches.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalRule) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.field_condition_list

    out["Conditions"] = (
        capo_pinpoint_sms_voice_v2.types.field_condition_list.serialize_aws_json_1_0(
            value["conditions"]
        )
    )
    out["RuleBehavior"] = value["rule_behavior"]
    if "conditional_validation" in value:
        import capo_pinpoint_sms_voice_v2.types.conditional_validation

        out["ConditionalValidation"] = (
            capo_pinpoint_sms_voice_v2.types.conditional_validation.serialize_aws_json_1_0(
                value["conditional_validation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionalRule:
    out: ConditionalRule = {}  # type: ignore[typeddict-item]
    if data.get("Conditions") is not None:
        import capo_pinpoint_sms_voice_v2.types.field_condition_list

        out["conditions"] = (
            capo_pinpoint_sms_voice_v2.types.field_condition_list.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    else:
        out["conditions"] = []
    if data.get("RuleBehavior") is not None:
        out["rule_behavior"] = data["RuleBehavior"]
    else:
        out["rule_behavior"] = ""
    if data.get("ConditionalValidation") is not None:
        import capo_pinpoint_sms_voice_v2.types.conditional_validation

        out["conditional_validation"] = (
            capo_pinpoint_sms_voice_v2.types.conditional_validation.deserialize_aws_json_1_0(
                data["ConditionalValidation"]
            )
        )
    return out
