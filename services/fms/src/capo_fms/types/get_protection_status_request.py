"""Generated from Smithy shape ``com.amazonaws.fms#GetProtectionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token
    import capo_fms.types.policy_id
    import capo_fms.types.time_stamp


class GetProtectionStatusRequest(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the policy for which you want to get the attack information.</p>"""
    member_account_id: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account that is in scope of the policy that you want to get the details for.</p>"""
    start_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The start of the time period to query for the attacks. This is a <code>timestamp</code> type. The request syntax listing indicates a <code>number</code> type because the default used by Firewall Manager is Unix time in seconds. However, any valid <code>timestamp</code> format is allowed.</p>"""
    end_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The end of the time period to query for the attacks. This is a <code>timestamp</code> type. The request syntax listing indicates a <code>number</code> type because the default used by Firewall Manager is Unix time in seconds. However, any valid <code>timestamp</code> format is allowed.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> and you have more objects than the number that you specify for <code>MaxResults</code>, Firewall Manager returns a <code>NextToken</code> value in the response, which you can use to retrieve another group of objects. For the second and subsequent <code>GetProtectionStatus</code> requests, specify the value of <code>NextToken</code> from the previous response to get information about another batch of objects.</p>"""
    max_results: NotRequired[
        "capo_fms.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Specifies the number of objects that you want Firewall Manager to return for this request. If you have more objects than the number that you specify for <code>MaxResults</code>, the response includes a <code>NextToken</code> value that you can use to get another batch of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProtectionStatusRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    if "member_account_id" in value:
        out["MemberAccountId"] = value["member_account_id"]
    if "start_time" in value:
        import capo_fms.types.time_stamp

        out["StartTime"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_fms.types.time_stamp

        out["EndTime"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProtectionStatusRequest:
    out: GetProtectionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("MemberAccountId") is not None:
        out["member_account_id"] = data["MemberAccountId"]
    if data.get("StartTime") is not None:
        import capo_fms.types.time_stamp

        out["start_time"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_fms.types.time_stamp

        out["end_time"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
