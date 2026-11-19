"""Generated from Smithy shape ``com.amazonaws.datasync#ListAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.max_results
    import capo_datasync.types.next_token


class ListAgentsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_datasync.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of DataSync agents to list in a response. By default, a response shows a maximum of 100 agents.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>Specifies an opaque string that indicates the position to begin the next list of results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAgentsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAgentsRequest:
    out: ListAgentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgentsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgentsRequest:
    out: ListAgentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
