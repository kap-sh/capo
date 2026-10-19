"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListAssessmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.assessment_target_filter
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.framework_filters
    import capo_marketplace_catalog.types.framework_id
    import capo_marketplace_catalog.types.list_assessments_max_result_integer
    import capo_marketplace_catalog.types.next_token


class ListAssessmentsRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    framework_id: NotRequired["capo_marketplace_catalog.types.framework_id.FrameworkId"]
    """<p>The unique identifier of a framework. When specified, only assessments performed against this framework are returned. For example, <code>AMISecurity</code>.</p>"""
    assessment_target_filter: NotRequired[
        "capo_marketplace_catalog.types.assessment_target_filter.AssessmentTargetFilter"
    ]
    """<p>Filters the list of assessments to those performed against a specific entity or change set.</p>"""
    framework_filters: NotRequired[
        "capo_marketplace_catalog.types.framework_filters.FrameworkFilters"
    ]
    """<p>Framework-specific filters. Set exactly one member to filter results to assessments performed against that framework.</p>"""
    max_results: NotRequired[
        "capo_marketplace_catalog.types.list_assessments_max_result_integer.ListAssessmentsMaxResultInteger"
    ]
    """<p>Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20. Valid values range from 1 to 100.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "framework_id" in value:
        out["FrameworkId"] = value["framework_id"]
    if "assessment_target_filter" in value:
        import capo_marketplace_catalog.types.assessment_target_filter

        out["AssessmentTargetFilter"] = (
            capo_marketplace_catalog.types.assessment_target_filter.serialize_json(
                value["assessment_target_filter"]
            )
        )
    if "framework_filters" in value:
        import capo_marketplace_catalog.types.framework_filters

        out["FrameworkFilters"] = (
            capo_marketplace_catalog.types.framework_filters.serialize_json(
                value["framework_filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentsRequest:
    out: ListAssessmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListAssessmentsRequest.catalog required")
    if data.get("FrameworkId") is not None:
        out["framework_id"] = data["FrameworkId"]
    if data.get("AssessmentTargetFilter") is not None:
        import capo_marketplace_catalog.types.assessment_target_filter

        out["assessment_target_filter"] = (
            capo_marketplace_catalog.types.assessment_target_filter.deserialize_json(
                data["AssessmentTargetFilter"]
            )
        )
    if data.get("FrameworkFilters") is not None:
        import capo_marketplace_catalog.types.framework_filters

        out["framework_filters"] = (
            capo_marketplace_catalog.types.framework_filters.deserialize_json(
                data["FrameworkFilters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
