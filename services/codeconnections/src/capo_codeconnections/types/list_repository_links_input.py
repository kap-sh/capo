"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListRepositoryLinksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.max_results
    import capo_codeconnections.types.sharp_next_token


class ListRepositoryLinksInput(TypedDict, closed=True):
    max_results: NotRequired["capo_codeconnections.types.max_results.MaxResults"]
    """<p> A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired[
        "capo_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p> An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoryLinksInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoryLinksInput:
    out: ListRepositoryLinksInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
