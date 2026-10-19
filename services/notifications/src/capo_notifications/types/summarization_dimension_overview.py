"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.sample_aggregation_dimension_values


class SummarizationDimensionOverview(TypedDict, closed=True):
    name: "str"
    """<p>Name of the summarization dimension.</p>"""
    count: "int"
    """<p>Total number of occurrences for this dimension.</p>"""
    sample_values: NotRequired[
        "capo_notifications.types.sample_aggregation_dimension_values.SampleAggregationDimensionValues"
    ]
    """<p>Indicates the sample values found within the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionOverview) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["count"] = value["count"]
    if "sample_values" in value:
        import capo_notifications.types.sample_aggregation_dimension_values

        out["sampleValues"] = (
            capo_notifications.types.sample_aggregation_dimension_values.serialize_json(
                value["sample_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummarizationDimensionOverview:
    out: SummarizationDimensionOverview = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("sampleValues") is not None:
        import capo_notifications.types.sample_aggregation_dimension_values

        out["sample_values"] = (
            capo_notifications.types.sample_aggregation_dimension_values.deserialize_json(
                data["sampleValues"]
            )
        )
    return out
