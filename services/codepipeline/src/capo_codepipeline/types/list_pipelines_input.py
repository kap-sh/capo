"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListPipelinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.max_pipelines
    import capo_codepipeline.types.next_token


class ListPipelinesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>An identifier that was returned from the previous list pipelines call. It can be used to return the next set of pipelines in the list.</p>"""
    max_results: NotRequired["capo_codepipeline.types.max_pipelines.MaxPipelines"]
    """<p>The maximum number of pipelines to return in a single call. To retrieve the remaining pipelines, make another call with the returned nextToken value. The minimum value you can specify is 1. The maximum accepted value is 1000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesInput:
    out: ListPipelinesInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPipelinesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListPipelinesInput:
    out: ListPipelinesInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
