"""Generated from Smithy shape ``com.amazonaws.configservice#ListResourceEvaluationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.list_resource_evaluations_page_item_limit
    import capo_config_service.types.resource_evaluation_filters
    import capo_config_service.types.string


class ListResourceEvaluationsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_config_service.types.resource_evaluation_filters.ResourceEvaluationFilters"
    ]
    """<p>Returns a <code>ResourceEvaluationFilters</code> object.</p>"""
    limit: NotRequired[
        "capo_config_service.types.list_resource_evaluations_page_item_limit.ListResourceEvaluationsPageItemLimit"
    ]
    """<p>The maximum number of evaluations returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceEvaluationsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_config_service.types.resource_evaluation_filters

        out["Filters"] = (
            capo_config_service.types.resource_evaluation_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceEvaluationsRequest:
    out: ListResourceEvaluationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_config_service.types.resource_evaluation_filters

        out["filters"] = (
            capo_config_service.types.resource_evaluation_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
