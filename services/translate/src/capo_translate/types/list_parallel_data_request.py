"""Generated from Smithy shape ``com.amazonaws.translate#ListParallelDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.max_results_integer
    import capo_translate.types.next_token


class ListParallelDataRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p>A string that specifies the next page of results to return in a paginated response.</p>"""
    max_results: NotRequired[
        "capo_translate.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of parallel data resources returned for each request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListParallelDataRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListParallelDataRequest:
    out: ListParallelDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListParallelDataRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListParallelDataRequest:
    out: ListParallelDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
