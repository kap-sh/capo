"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.time_stamp


class ListAppVersionsRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["capo_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    start_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Lower limit of the time range to filter the application versions.</p>"""
    end_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Upper limit of the time range to filter the application versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionsRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "start_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["startTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["endTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> ListAppVersionsRequest:
    out: ListAppVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("ListAppVersionsRequest.app_arn required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("startTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["start_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["end_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    return out
