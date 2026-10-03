"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListFindingsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.sort_criteria
    import capo_accessanalyzer.types.token


class ListFindingsV2Request(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve findings from.</p>"""
    filter: NotRequired[
        "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    ]
    """<p>A filter to match for the findings to return.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    sort: NotRequired["capo_accessanalyzer.types.sort_criteria.SortCriteria"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsV2Request) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    if "filter" in value:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.serialize_json(
            value["filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort" in value:
        import capo_accessanalyzer.types.sort_criteria

        out["sort"] = capo_accessanalyzer.types.sort_criteria.serialize_json(
            value["sort"]
        )
    return out


def deserialize_json(data: dict) -> ListFindingsV2Request:
    out: ListFindingsV2Request = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("ListFindingsV2Request.analyzer_arn required")
    if data.get("filter") is not None:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.deserialize_json(
            data["filter"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("sort") is not None:
        import capo_accessanalyzer.types.sort_criteria

        out["sort"] = capo_accessanalyzer.types.sort_criteria.deserialize_json(
            data["sort"]
        )
    return out
