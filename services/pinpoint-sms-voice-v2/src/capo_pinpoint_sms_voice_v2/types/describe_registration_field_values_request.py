"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationFieldValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_path_list
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.registration_version_number
    import capo_pinpoint_sms_voice_v2.types.section_path


class DescribeRegistrationFieldValuesRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    version_number: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    ]
    """<p>The version number of the registration.</p>"""
    section_path: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.section_path.SectionPath"
    ]
    """<p>The path to the section of the registration.</p>"""
    field_paths: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.field_path_list.FieldPathList"
    ]
    """<p>An array of paths to the registration form field.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationFieldValuesRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "section_path" in value:
        out["SectionPath"] = value["section_path"]
    if "field_paths" in value:
        import capo_pinpoint_sms_voice_v2.types.field_path_list

        out["FieldPaths"] = (
            capo_pinpoint_sms_voice_v2.types.field_path_list.serialize_aws_json_1_0(
                value["field_paths"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationFieldValuesRequest:
    out: DescribeRegistrationFieldValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("SectionPath") is not None:
        out["section_path"] = data["SectionPath"]
    if data.get("FieldPaths") is not None:
        import capo_pinpoint_sms_voice_v2.types.field_path_list

        out["field_paths"] = (
            capo_pinpoint_sms_voice_v2.types.field_path_list.deserialize_aws_json_1_0(
                data["FieldPaths"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
