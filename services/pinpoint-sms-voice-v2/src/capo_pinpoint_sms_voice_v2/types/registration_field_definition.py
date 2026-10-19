"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFieldDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.conditional_behavior
    import capo_pinpoint_sms_voice_v2.types.field_path
    import capo_pinpoint_sms_voice_v2.types.field_requirement
    import capo_pinpoint_sms_voice_v2.types.field_type
    import capo_pinpoint_sms_voice_v2.types.registration_field_display_hints
    import capo_pinpoint_sms_voice_v2.types.section_path
    import capo_pinpoint_sms_voice_v2.types.select_validation
    import capo_pinpoint_sms_voice_v2.types.text_validation


class RegistrationFieldDefinition(TypedDict, closed=True):
    section_path: "capo_pinpoint_sms_voice_v2.types.section_path.SectionPath"
    """<p>The section path of the field.</p>"""
    field_path: "capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""
    field_type: "capo_pinpoint_sms_voice_v2.types.field_type.FieldType"
    """<p>The type of field.</p>"""
    field_requirement: (
        "capo_pinpoint_sms_voice_v2.types.field_requirement.FieldRequirement"
    )
    """<p>Specifies if the field for the registration form is required, conditional or optional.</p>"""
    select_validation: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.select_validation.SelectValidation"
    ]
    """<p>The validation rules for a select field.</p>"""
    text_validation: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.text_validation.TextValidation"
    ]
    """<p>The validation rules for a text field.</p>"""
    display_hints: "capo_pinpoint_sms_voice_v2.types.registration_field_display_hints.RegistrationFieldDisplayHints"
    """<p>An array of RegistrationFieldDisplayHints objects for the field.</p>"""
    conditional_behavior: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.conditional_behavior.ConditionalBehavior"
    ]
    """<p>The conditional behavior rules for this field. Only present when <b>FieldRequirement</b> is <b>CONDITIONAL</b>. Rules are evaluated in order and the first matching rule determines the field's resolved requirement. If no rule matches, the <b>DefaultBehavior</b> applies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFieldDefinition) -> dict:
    out: dict = {}
    out["SectionPath"] = value["section_path"]
    out["FieldPath"] = value["field_path"]
    out["FieldType"] = value["field_type"]
    out["FieldRequirement"] = value["field_requirement"]
    if "select_validation" in value:
        import capo_pinpoint_sms_voice_v2.types.select_validation

        out["SelectValidation"] = (
            capo_pinpoint_sms_voice_v2.types.select_validation.serialize_aws_json_1_0(
                value["select_validation"]
            )
        )
    if "text_validation" in value:
        import capo_pinpoint_sms_voice_v2.types.text_validation

        out["TextValidation"] = (
            capo_pinpoint_sms_voice_v2.types.text_validation.serialize_aws_json_1_0(
                value["text_validation"]
            )
        )
    import capo_pinpoint_sms_voice_v2.types.registration_field_display_hints

    out["DisplayHints"] = (
        capo_pinpoint_sms_voice_v2.types.registration_field_display_hints.serialize_aws_json_1_0(
            value["display_hints"]
        )
    )
    if "conditional_behavior" in value:
        import capo_pinpoint_sms_voice_v2.types.conditional_behavior

        out["ConditionalBehavior"] = (
            capo_pinpoint_sms_voice_v2.types.conditional_behavior.serialize_aws_json_1_0(
                value["conditional_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationFieldDefinition:
    out: RegistrationFieldDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SectionPath") is not None:
        out["section_path"] = data["SectionPath"]
    else:
        out["section_path"] = ""
    if data.get("FieldPath") is not None:
        out["field_path"] = data["FieldPath"]
    else:
        out["field_path"] = ""
    if data.get("FieldType") is not None:
        out["field_type"] = data["FieldType"]
    else:
        out["field_type"] = ""
    if data.get("FieldRequirement") is not None:
        out["field_requirement"] = data["FieldRequirement"]
    else:
        out["field_requirement"] = ""
    if data.get("SelectValidation") is not None:
        import capo_pinpoint_sms_voice_v2.types.select_validation

        out["select_validation"] = (
            capo_pinpoint_sms_voice_v2.types.select_validation.deserialize_aws_json_1_0(
                data["SelectValidation"]
            )
        )
    if data.get("TextValidation") is not None:
        import capo_pinpoint_sms_voice_v2.types.text_validation

        out["text_validation"] = (
            capo_pinpoint_sms_voice_v2.types.text_validation.deserialize_aws_json_1_0(
                data["TextValidation"]
            )
        )
    if data.get("DisplayHints") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_field_display_hints

        out["display_hints"] = (
            capo_pinpoint_sms_voice_v2.types.registration_field_display_hints.deserialize_aws_json_1_0(
                data["DisplayHints"]
            )
        )
    else:
        raise DeserializationError("RegistrationFieldDefinition.display_hints required")
    if data.get("ConditionalBehavior") is not None:
        import capo_pinpoint_sms_voice_v2.types.conditional_behavior

        out["conditional_behavior"] = (
            capo_pinpoint_sms_voice_v2.types.conditional_behavior.deserialize_aws_json_1_0(
                data["ConditionalBehavior"]
            )
        )
    return out
