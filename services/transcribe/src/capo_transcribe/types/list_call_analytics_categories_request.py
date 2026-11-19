"""Generated from Smithy shape ``com.amazonaws.transcribe#ListCallAnalyticsCategoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.max_results
    import capo_transcribe.types.next_token


class ListCallAnalyticsCategoriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListCallAnalyticsCategories</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["capo_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of Call Analytics categories to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCallAnalyticsCategoriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCallAnalyticsCategoriesRequest:
    out: ListCallAnalyticsCategoriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCallAnalyticsCategoriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListCallAnalyticsCategoriesRequest:
    out: ListCallAnalyticsCategoriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
