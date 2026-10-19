"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionalBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.conditional_field_behavior
    import capo_pinpoint_sms_voice_v2.types.conditional_rule_list


class ConditionalBehavior(TypedDict, closed=True):
    rules: "capo_pinpoint_sms_voice_v2.types.conditional_rule_list.ConditionalRuleList"
    """<p>An ordered list of conditional rules. Rules are evaluated top-to-bottom and the first rule whose conditions all evaluate to true determines the field's behavior. Rules whose conditions do not all match are skipped and evaluation continues to the next rule.</p>"""
    default_behavior: "capo_pinpoint_sms_voice_v2.types.conditional_field_behavior.ConditionalFieldBehavior"
    """<p>The field behavior that applies when no conditional rule in <b>Rules</b> matches. Valid values are <b>REQUIRED</b>, <b>OPTIONAL</b>, and <b>DISALLOWED</b>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalBehavior) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.conditional_rule_list

    out["Rules"] = (
        capo_pinpoint_sms_voice_v2.types.conditional_rule_list.serialize_aws_json_1_0(
            value["rules"]
        )
    )
    out["DefaultBehavior"] = value["default_behavior"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionalBehavior:
    out: ConditionalBehavior = {}  # type: ignore[typeddict-item]
    if data.get("Rules") is not None:
        import capo_pinpoint_sms_voice_v2.types.conditional_rule_list

        out["rules"] = (
            capo_pinpoint_sms_voice_v2.types.conditional_rule_list.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    if data.get("DefaultBehavior") is not None:
        out["default_behavior"] = data["DefaultBehavior"]
    else:
        out["default_behavior"] = ""
    return out
