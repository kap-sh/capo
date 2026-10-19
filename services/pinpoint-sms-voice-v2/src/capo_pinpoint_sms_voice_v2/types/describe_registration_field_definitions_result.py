"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationFieldDefinitionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_field_definition_list
    import capo_pinpoint_sms_voice_v2.types.registration_type


class DescribeRegistrationFieldDefinitionsResult(TypedDict, closed=True):
    registration_type: (
        "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_field_definitions: "capo_pinpoint_sms_voice_v2.types.registration_field_definition_list.RegistrationFieldDefinitionList"
    """<p>An array of RegistrationFieldDefinitions objects that contain the details for the requested fields. </p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationFieldDefinitionsResult) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
    import capo_pinpoint_sms_voice_v2.types.registration_field_definition_list

    out["RegistrationFieldDefinitions"] = (
        capo_pinpoint_sms_voice_v2.types.registration_field_definition_list.serialize_aws_json_1_0(
            value["registration_field_definitions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationFieldDefinitionsResult:
    out: DescribeRegistrationFieldDefinitionsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationType") is not None:
        out["registration_type"] = data["RegistrationType"]
    else:
        out["registration_type"] = ""
    if data.get("RegistrationFieldDefinitions") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_field_definition_list

        out["registration_field_definitions"] = (
            capo_pinpoint_sms_voice_v2.types.registration_field_definition_list.deserialize_aws_json_1_0(
                data["RegistrationFieldDefinitions"]
            )
        )
    else:
        out["registration_field_definitions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
