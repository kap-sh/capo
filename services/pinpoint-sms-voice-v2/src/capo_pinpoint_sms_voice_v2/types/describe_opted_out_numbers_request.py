"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeOptedOutNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import capo_pinpoint_sms_voice_v2.types.opted_out_filter_list
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_list


class DescribeOptedOutNumbersRequest(TypedDict, closed=True):
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    )
    """<p>The OptOutListName or OptOutListArn of the OptOutList. You can use <a>DescribeOptOutLists</a> to find the values for OptOutListName and OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    opted_out_numbers: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opted_out_number_list.OptedOutNumberList"
    ]
    """<p>An array of phone numbers to search for in the OptOutList.</p> <p>If you specify an opted out number that isn't valid, an exception is returned.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.opted_out_filter_list.OptedOutFilterList"
    ]
    """<p>An array of OptedOutFilter objects to filter the results on.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeOptedOutNumbersRequest) -> dict:
    out: dict = {}
    out["OptOutListName"] = value["opt_out_list_name"]
    if "opted_out_numbers" in value:
        import capo_pinpoint_sms_voice_v2.types.opted_out_number_list

        out["OptedOutNumbers"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_number_list.serialize_aws_json_1_0(
                value["opted_out_numbers"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.opted_out_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeOptedOutNumbersRequest:
    out: DescribeOptedOutNumbersRequest = {}  # type: ignore[typeddict-item]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        out["opt_out_list_name"] = ""
    if data.get("OptedOutNumbers") is not None:
        import capo_pinpoint_sms_voice_v2.types.opted_out_number_list

        out["opted_out_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_number_list.deserialize_aws_json_1_0(
                data["OptedOutNumbers"]
            )
        )
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.opted_out_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.opted_out_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
