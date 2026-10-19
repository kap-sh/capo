"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListPoolOriginationIdentitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list


class ListPoolOriginationIdentitiesRequest(TypedDict, closed=True):
    pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    """<p>The unique identifier for the pool. This value can be either the PoolId or PoolArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list.PoolOriginationIdentitiesFilterList"
    ]
    """<p>An array of PoolOriginationIdentitiesFilter objects to filter the results..</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPoolOriginationIdentitiesRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPoolOriginationIdentitiesRequest:
    out: ListPoolOriginationIdentitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("Filters") is not None:
        import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
