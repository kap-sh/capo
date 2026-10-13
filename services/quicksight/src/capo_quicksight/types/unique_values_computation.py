"""Generated from Smithy shape ``com.amazonaws.quicksight#UniqueValuesComputation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class UniqueValuesComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    category: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UniqueValuesComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "category" in value:
        import capo_quicksight.types.dimension_field

        out["Category"] = capo_quicksight.types.dimension_field.serialize_json(
            value["category"]
        )
    return out


def deserialize_json(data: dict) -> UniqueValuesComputation:
    out: UniqueValuesComputation = {}  # type: ignore[typeddict-item]
    if data.get("ComputationId") is not None:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("UniqueValuesComputation.computation_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Category") is not None:
        import capo_quicksight.types.dimension_field

        out["category"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Category"]
        )
    return out


def redact_sensitive(value: UniqueValuesComputation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        import capo_quicksight.types.dimension_field

        out["category"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["category"]
        )
    return out
