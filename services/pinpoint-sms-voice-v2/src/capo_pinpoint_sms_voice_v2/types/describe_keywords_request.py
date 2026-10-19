"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeKeywordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword_filter_list
    import capo_pinpoint_sms_voice_v2.types.keyword_list
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn


class DescribeKeywordsRequest(TypedDict, closed=True):
    origination_identity: (
        "capo_pinpoint_sms_voice_v2.types.phone_or_pool_id_or_arn.PhoneOrPoolIdOrArn"
    )
    """<p>The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use <a>DescribePhoneNumbers</a> to find the values for PhoneNumberId and PhoneNumberArn while <a>DescribeSenderIds</a> can be used to get the values for SenderId and SenderIdArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    keywords: NotRequired["capo_pinpoint_sms_voice_v2.types.keyword_list.KeywordList"]
    """<p>An array of keywords to search for.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.keyword_filter_list.KeywordFilterList"
    ]
    """<p>An array of keyword filters to filter the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeKeywordsRequest) -> dict:
    out: dict = {}
    out["OriginationIdentity"] = value["origination_identity"]
    if "keywords" in value:
        import capo_pinpoint_sms_voice_v2.types.keyword_list

        out["Keywords"] = (
            capo_pinpoint_sms_voice_v2.types.keyword_list.serialize_aws_json_1_0(
                value["keywords"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.keyword_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.keyword_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeKeywordsRequest:
    out: DescribeKeywordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    else:
        out["origination_identity"] = ""
    if data.get("Keywords") is not None:
        import capo_pinpoint_sms_voice_v2.types.keyword_list

        out["keywords"] = (
            capo_pinpoint_sms_voice_v2.types.keyword_list.deserialize_aws_json_1_0(
                data["Keywords"]
            )
        )
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.keyword_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.keyword_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
