"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.word_cloud_dimension_field_list
    import capo_quicksight.types.word_cloud_measure_field_list


class WordCloudAggregatedFieldWells(TypedDict, closed=True):
    group_by: NotRequired[
        "capo_quicksight.types.word_cloud_dimension_field_list.WordCloudDimensionFieldList"
    ]
    """<p>The group by field well of a word cloud. Values are grouped by group by fields.</p>"""
    size: NotRequired[
        "capo_quicksight.types.word_cloud_measure_field_list.WordCloudMeasureFieldList"
    ]
    """<p>The size field well of a word cloud. Values are aggregated based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudAggregatedFieldWells) -> dict:
    out: dict = {}
    if "group_by" in value:
        import capo_quicksight.types.word_cloud_dimension_field_list

        out["GroupBy"] = (
            capo_quicksight.types.word_cloud_dimension_field_list.serialize_json(
                value["group_by"]
            )
        )
    if "size" in value:
        import capo_quicksight.types.word_cloud_measure_field_list

        out["Size"] = (
            capo_quicksight.types.word_cloud_measure_field_list.serialize_json(
                value["size"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudAggregatedFieldWells:
    out: WordCloudAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("GroupBy") is not None:
        import capo_quicksight.types.word_cloud_dimension_field_list

        out["group_by"] = (
            capo_quicksight.types.word_cloud_dimension_field_list.deserialize_json(
                data["GroupBy"]
            )
        )
    if data.get("Size") is not None:
        import capo_quicksight.types.word_cloud_measure_field_list

        out["size"] = (
            capo_quicksight.types.word_cloud_measure_field_list.deserialize_json(
                data["Size"]
            )
        )
    return out


def redact_sensitive(value: WordCloudAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_by" in value:
        import capo_quicksight.types.word_cloud_dimension_field_list

        out["group_by"] = (
            capo_quicksight.types.word_cloud_dimension_field_list.redact_sensitive(
                value["group_by"]
            )
        )
    if "size" in value:
        import capo_quicksight.types.word_cloud_measure_field_list

        out["size"] = (
            capo_quicksight.types.word_cloud_measure_field_list.redact_sensitive(
                value["size"]
            )
        )
    return out
