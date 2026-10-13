"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.search_results_list
    import capo_sagemaker.types.total_hits


class SearchResponse(TypedDict, closed=True):
    results: NotRequired["capo_sagemaker.types.search_results_list.SearchResultsList"]
    """<p>A list of <code>SearchRecord</code> objects.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>Search</code> request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request.</p>"""
    total_hits: NotRequired["capo_sagemaker.types.total_hits.TotalHits"]
    """<p>The total number of matching results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_sagemaker.types.search_results_list

        out["Results"] = (
            capo_sagemaker.types.search_results_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "total_hits" in value:
        import capo_sagemaker.types.total_hits

        out["TotalHits"] = capo_sagemaker.types.total_hits.serialize_aws_json_1_1(
            value["total_hits"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchResponse:
    out: SearchResponse = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_sagemaker.types.search_results_list

        out["results"] = (
            capo_sagemaker.types.search_results_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TotalHits") is not None:
        import capo_sagemaker.types.total_hits

        out["total_hits"] = capo_sagemaker.types.total_hits.deserialize_aws_json_1_1(
            data["TotalHits"]
        )
    return out


def redact_sensitive(value: SearchResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_sagemaker.types.search_results_list

        out["results"] = capo_sagemaker.types.search_results_list.redact_sensitive(
            value["results"]
        )
    return out
