"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#FieldCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.condition_operator
    import capo_pinpoint_sms_voice_v2.types.condition_value_list
    import capo_pinpoint_sms_voice_v2.types.field_path


class FieldCondition(TypedDict, closed=True):
    depends_on_field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path of the field whose value determines this condition, for example <b>companyInfo.businessType</b>.</p>"""
    operator: "capo_pinpoint_sms_voice_v2.types.condition_operator.ConditionOperator"
    """<p>The comparison operator to apply between the dependency field's value and <b>Values</b>. Valid values are <b>EQUALS</b>, <b>NOT_EQUALS</b>, <b>IN</b>, <b>NOT_IN</b>, <b>HAS_VALUE</b>, and <b>NO_VALUE</b>. Operators not in this list are treated as evaluating to false, which causes the containing rule to be skipped. This allows forward-compatible additions of new operators without breaking older SDK clients.</p>"""
    values: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.condition_value_list.ConditionValueList"
    ]
    """<p>The values to compare the dependency field's value against. Required for the <b>EQUALS</b>, <b>NOT_EQUALS</b>, <b>IN</b>, and <b>NOT_IN</b> operators. Omitted for <b>HAS_VALUE</b> and <b>NO_VALUE</b>, which test only presence.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldCondition) -> dict:
    out: dict = {}
    out["DependsOnFieldPath"] = value["depends_on_field_path"]
    out["Operator"] = value["operator"]
    if "values" in value:
        import capo_pinpoint_sms_voice_v2.types.condition_value_list

        out["Values"] = (
            capo_pinpoint_sms_voice_v2.types.condition_value_list.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FieldCondition:
    out: FieldCondition = {}  # type: ignore[typeddict-item]
    if data.get("DependsOnFieldPath") is not None:
        out["depends_on_field_path"] = data["DependsOnFieldPath"]
    else:
        out["depends_on_field_path"] = ""
    if data.get("Operator") is not None:
        out["operator"] = data["Operator"]
    else:
        out["operator"] = ""
    if data.get("Values") is not None:
        import capo_pinpoint_sms_voice_v2.types.condition_value_list

        out["values"] = (
            capo_pinpoint_sms_voice_v2.types.condition_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    return out
