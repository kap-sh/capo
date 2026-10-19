"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_list
    import capo_sustainability.types.emissions_type_list
    import capo_sustainability.types.filter_expression
    import capo_sustainability.types.granularity_configuration
    import capo_sustainability.types.max_results
    import capo_sustainability.types.next_token
    import capo_sustainability.types.time_granularity
    import capo_sustainability.types.time_period


class GetEstimatedCarbonEmissionsRequest(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p> The date range for fetching estimated carbon emissions. The range must include the start date of a month for that month's data to be included in the response. </p>"""
    group_by: NotRequired["capo_sustainability.types.dimension_list.DimensionList"]
    """<p>The dimensions available for grouping estimated carbon emissions.</p>"""
    filter_by: NotRequired[
        "capo_sustainability.types.filter_expression.FilterExpression"
    ]
    """<p> The criteria for filtering estimated carbon emissions. To determine which dimensions are available to be filtered by, you can first call <a>GetEstimatedCarbonEmissionsDimensionValues</a> </p>"""
    emissions_types: NotRequired[
        "capo_sustainability.types.emissions_type_list.EmissionsTypeList"
    ]
    """<p>The emission types to include in the results. If absent, returns <code>TOTAL_LBM_CARBON_EMISSIONS</code> and <code>TOTAL_MBM_CARBON_EMISSIONS</code> emissions types. </p>"""
    granularity: NotRequired[
        "capo_sustainability.types.time_granularity.TimeGranularity"
    ]
    """<p> The time granularity for the results. If absent, uses <code>MONTHLY</code> time granularity. The smallest supported granularity for carbon emissions is <code>MONTHLY</code>. </p> <p> If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting <code>2025-04-01T00:00:00Z</code> to <code>2026-04-01T00:00:00Z</code> with <code>YEARLY_CALENDAR</code> granularity will return the last 9 months for 2025 and the first 3 months of 2026. </p>"""
    granularity_configuration: NotRequired[
        "capo_sustainability.types.granularity_configuration.GranularityConfiguration"
    ]
    """<p>Configuration for fiscal year calculations when using <code>YEARLY_FISCAL</code> or <code>QUARTERLY_FISCAL</code> granularity. </p>"""
    max_results: NotRequired["capo_sustainability.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Default is 1000.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsRequest) -> dict:
    out: dict = {}
    import capo_sustainability.types.time_period

    out["TimePeriod"] = capo_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    if "group_by" in value:
        import capo_sustainability.types.dimension_list

        out["GroupBy"] = capo_sustainability.types.dimension_list.serialize_json(
            value["group_by"]
        )
    if "filter_by" in value:
        import capo_sustainability.types.filter_expression

        out["FilterBy"] = capo_sustainability.types.filter_expression.serialize_json(
            value["filter_by"]
        )
    if "emissions_types" in value:
        import capo_sustainability.types.emissions_type_list

        out["EmissionsTypes"] = (
            capo_sustainability.types.emissions_type_list.serialize_json(
                value["emissions_types"]
            )
        )
    if "granularity" in value:
        import capo_sustainability.types.time_granularity

        out["Granularity"] = capo_sustainability.types.time_granularity.serialize_json(
            value["granularity"]
        )
    if "granularity_configuration" in value:
        import capo_sustainability.types.granularity_configuration

        out["GranularityConfiguration"] = (
            capo_sustainability.types.granularity_configuration.serialize_json(
                value["granularity_configuration"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsRequest:
    out: GetEstimatedCarbonEmissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedCarbonEmissionsRequest.time_period required"
        )
    if data.get("GroupBy") is not None:
        import capo_sustainability.types.dimension_list

        out["group_by"] = capo_sustainability.types.dimension_list.deserialize_json(
            data["GroupBy"]
        )
    if data.get("FilterBy") is not None:
        import capo_sustainability.types.filter_expression

        out["filter_by"] = capo_sustainability.types.filter_expression.deserialize_json(
            data["FilterBy"]
        )
    if data.get("EmissionsTypes") is not None:
        import capo_sustainability.types.emissions_type_list

        out["emissions_types"] = (
            capo_sustainability.types.emissions_type_list.deserialize_json(
                data["EmissionsTypes"]
            )
        )
    if data.get("Granularity") is not None:
        import capo_sustainability.types.time_granularity

        out["granularity"] = (
            capo_sustainability.types.time_granularity.deserialize_json(
                data["Granularity"]
            )
        )
    if data.get("GranularityConfiguration") is not None:
        import capo_sustainability.types.granularity_configuration

        out["granularity_configuration"] = (
            capo_sustainability.types.granularity_configuration.deserialize_json(
                data["GranularityConfiguration"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
