"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.aggregation_keys
    import capo_notifications.types.summarization_dimension_overview
    import capo_notifications.types.summarization_dimension_overviews


class AggregationSummary(TypedDict, closed=True):
    event_count: "int"
    """<p>Indicates the number of events associated with the aggregation key.</p>"""
    aggregated_by: "capo_notifications.types.aggregation_keys.AggregationKeys"
    """<p>Indicates the criteria or rules by which notifications have been grouped together.</p>"""
    aggregated_accounts: "capo_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    """<p>Indicates the Amazon Web Services accounts in the aggregation key.</p>"""
    aggregated_regions: "capo_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    """<p>Indicates the Amazon Web Services Regions in the aggregation key.</p>"""
    aggregated_organizational_units: NotRequired[
        "capo_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    ]
    """<p>Indicates the collection of organizational units that are involved in the aggregation key.</p>"""
    additional_summarization_dimensions: NotRequired[
        "capo_notifications.types.summarization_dimension_overviews.SummarizationDimensionOverviews"
    ]
    """<p>List of additional dimensions used to group and summarize data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationSummary) -> dict:
    out: dict = {}
    out["eventCount"] = value["event_count"]
    import capo_notifications.types.aggregation_keys

    out["aggregatedBy"] = capo_notifications.types.aggregation_keys.serialize_json(
        value["aggregated_by"]
    )
    import capo_notifications.types.summarization_dimension_overview

    out["aggregatedAccounts"] = (
        capo_notifications.types.summarization_dimension_overview.serialize_json(
            value["aggregated_accounts"]
        )
    )
    import capo_notifications.types.summarization_dimension_overview

    out["aggregatedRegions"] = (
        capo_notifications.types.summarization_dimension_overview.serialize_json(
            value["aggregated_regions"]
        )
    )
    if "aggregated_organizational_units" in value:
        import capo_notifications.types.summarization_dimension_overview

        out["aggregatedOrganizationalUnits"] = (
            capo_notifications.types.summarization_dimension_overview.serialize_json(
                value["aggregated_organizational_units"]
            )
        )
    if "additional_summarization_dimensions" in value:
        import capo_notifications.types.summarization_dimension_overviews

        out["additionalSummarizationDimensions"] = (
            capo_notifications.types.summarization_dimension_overviews.serialize_json(
                value["additional_summarization_dimensions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AggregationSummary:
    out: AggregationSummary = {}  # type: ignore[typeddict-item]
    if data.get("eventCount") is not None:
        out["event_count"] = data["eventCount"]
    else:
        out["event_count"] = 0
    if data.get("aggregatedBy") is not None:
        import capo_notifications.types.aggregation_keys

        out["aggregated_by"] = (
            capo_notifications.types.aggregation_keys.deserialize_json(
                data["aggregatedBy"]
            )
        )
    else:
        out["aggregated_by"] = []
    if data.get("aggregatedAccounts") is not None:
        import capo_notifications.types.summarization_dimension_overview

        out["aggregated_accounts"] = (
            capo_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedAccounts"]
            )
        )
    else:
        raise DeserializationError("AggregationSummary.aggregated_accounts required")
    if data.get("aggregatedRegions") is not None:
        import capo_notifications.types.summarization_dimension_overview

        out["aggregated_regions"] = (
            capo_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedRegions"]
            )
        )
    else:
        raise DeserializationError("AggregationSummary.aggregated_regions required")
    if data.get("aggregatedOrganizationalUnits") is not None:
        import capo_notifications.types.summarization_dimension_overview

        out["aggregated_organizational_units"] = (
            capo_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedOrganizationalUnits"]
            )
        )
    if data.get("additionalSummarizationDimensions") is not None:
        import capo_notifications.types.summarization_dimension_overviews

        out["additional_summarization_dimensions"] = (
            capo_notifications.types.summarization_dimension_overviews.deserialize_json(
                data["additionalSummarizationDimensions"]
            )
        )
    return out
