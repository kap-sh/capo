"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.session_filter_list
    import capo_ssm.types.session_max_results
    import capo_ssm.types.session_state


class DescribeSessionsRequest(TypedDict, closed=True):
    state: "capo_ssm.types.session_state.SessionState"
    """<p>The session status to retrieve a list of sessions for. For example, "Active".</p>"""
    max_results: NotRequired["capo_ssm.types.session_max_results.SessionMaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    filters: NotRequired["capo_ssm.types.session_filter_list.SessionFilterList"]
    """<p>One or more filters to limit the type of sessions returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.session_state

    out["State"] = capo_ssm.types.session_state.serialize_aws_json_1_1(value["state"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_ssm.types.session_filter_list

        out["Filters"] = capo_ssm.types.session_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsRequest:
    out: DescribeSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        import capo_ssm.types.session_state

        out["state"] = capo_ssm.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    else:
        raise DeserializationError("DescribeSessionsRequest.state required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_ssm.types.session_filter_list

        out["filters"] = capo_ssm.types.session_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
