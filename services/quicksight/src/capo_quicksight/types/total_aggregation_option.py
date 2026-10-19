"""Generated from Smithy shape ``com.amazonaws.quicksight#TotalAggregationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.total_aggregation_function


class TotalAggregationOption(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field id that's associated with the total aggregation option.</p>"""
    total_aggregation_function: (
        "capo_quicksight.types.total_aggregation_function.TotalAggregationFunction"
    )
    """<p>The total aggregation function that you want to set for a specified field id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TotalAggregationOption) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.total_aggregation_function

    out["TotalAggregationFunction"] = (
        capo_quicksight.types.total_aggregation_function.serialize_json(
            value["total_aggregation_function"]
        )
    )
    return out


def deserialize_json(data: dict) -> TotalAggregationOption:
    out: TotalAggregationOption = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("TotalAggregationFunction") is not None:
        import capo_quicksight.types.total_aggregation_function

        out["total_aggregation_function"] = (
            capo_quicksight.types.total_aggregation_function.deserialize_json(
                data["TotalAggregationFunction"]
            )
        )
    else:
        raise DeserializationError(
            "TotalAggregationOption.total_aggregation_function required"
        )
    return out
