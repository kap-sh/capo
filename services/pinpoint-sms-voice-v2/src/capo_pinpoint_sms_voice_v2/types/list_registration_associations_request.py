"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListRegistrationAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_association_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn


class ListRegistrationAssociationsRequest(TypedDict, closed=True):
    registration_id: (
        "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_association_filter_list.RegistrationAssociationFilterList"
    ]
    """<p>An array of RegistrationAssociationFilter to apply to the results that are returned.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegistrationAssociationsRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.registration_association_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.registration_association_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegistrationAssociationsRequest:
    out: ListRegistrationAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_association_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.registration_association_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
