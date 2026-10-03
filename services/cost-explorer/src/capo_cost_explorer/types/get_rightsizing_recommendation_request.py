"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetRightsizingRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.recommendations_page_size
    import capo_cost_explorer.types.rightsizing_recommendation_configuration


class GetRightsizingRecommendationRequest(TypedDict, closed=True):
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    configuration: NotRequired[
        "capo_cost_explorer.types.rightsizing_recommendation_configuration.RightsizingRecommendationConfiguration"
    ]
    """<p>You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither. </p>"""
    service: "capo_cost_explorer.types.generic_string.GenericString"
    """<p>The specific service that you want recommendations for. The only valid value for <code>GetRightsizingRecommendation</code> is "<code>AmazonEC2</code>".</p>"""
    page_size: (
        "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    )
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRightsizingRecommendationRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "configuration" in value:
        import capo_cost_explorer.types.rightsizing_recommendation_configuration

        out["Configuration"] = (
            capo_cost_explorer.types.rightsizing_recommendation_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    out["Service"] = value["service"]
    out["PageSize"] = value.get("page_size", 0)
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRightsizingRecommendationRequest:
    out: GetRightsizingRecommendationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("Configuration") is not None:
        import capo_cost_explorer.types.rightsizing_recommendation_configuration

        out["configuration"] = (
            capo_cost_explorer.types.rightsizing_recommendation_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        raise DeserializationError(
            "GetRightsizingRecommendationRequest.service required"
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
