"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationTypeDefinitionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_type_definition_list


class DescribeRegistrationTypeDefinitionsResult(TypedDict, closed=True):
    registration_type_definitions: "capo_pinpoint_sms_voice_v2.types.registration_type_definition_list.RegistrationTypeDefinitionList"
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationTypeDefinitionsResult) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.registration_type_definition_list

    out["RegistrationTypeDefinitions"] = (
        capo_pinpoint_sms_voice_v2.types.registration_type_definition_list.serialize_aws_json_1_0(
            value["registration_type_definitions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationTypeDefinitionsResult:
    out: DescribeRegistrationTypeDefinitionsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationTypeDefinitions") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_type_definition_list

        out["registration_type_definitions"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_definition_list.deserialize_aws_json_1_0(
                data["RegistrationTypeDefinitions"]
            )
        )
    else:
        out["registration_type_definitions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
