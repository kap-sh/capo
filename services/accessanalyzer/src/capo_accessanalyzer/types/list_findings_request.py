"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.sort_criteria
    import capo_accessanalyzer.types.token


class ListFindingsRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve findings from.</p>"""
    filter: NotRequired[
        "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    ]
    """<p>A filter to match for the findings to return.</p>"""
    sort: NotRequired["capo_accessanalyzer.types.sort_criteria.SortCriteria"]
    """<p>The sort order for the findings returned.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    if "filter" in value:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.serialize_json(
            value["filter"]
        )
    if "sort" in value:
        import capo_accessanalyzer.types.sort_criteria

        out["sort"] = capo_accessanalyzer.types.sort_criteria.serialize_json(
            value["sort"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListFindingsRequest:
    out: ListFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("ListFindingsRequest.analyzer_arn required")
    if data.get("filter") is not None:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.deserialize_json(
            data["filter"]
        )
    if data.get("sort") is not None:
        import capo_accessanalyzer.types.sort_criteria

        out["sort"] = capo_accessanalyzer.types.sort_criteria.deserialize_json(
            data["sort"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
