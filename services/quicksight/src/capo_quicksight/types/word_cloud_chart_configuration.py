"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.word_cloud_field_wells
    import capo_quicksight.types.word_cloud_options
    import capo_quicksight.types.word_cloud_sort_configuration


class WordCloudChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.word_cloud_field_wells.WordCloudFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.word_cloud_sort_configuration.WordCloudSortConfiguration"
    ]
    """<p>The sort configuration of a word cloud visual.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) for the word cloud category.</p>"""
    word_cloud_options: NotRequired[
        "capo_quicksight.types.word_cloud_options.WordCloudOptions"
    ]
    """<p>The options for a word cloud visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.word_cloud_field_wells

        out["FieldWells"] = capo_quicksight.types.word_cloud_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.word_cloud_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.word_cloud_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "category_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "word_cloud_options" in value:
        import capo_quicksight.types.word_cloud_options

        out["WordCloudOptions"] = (
            capo_quicksight.types.word_cloud_options.serialize_json(
                value["word_cloud_options"]
            )
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudChartConfiguration:
    out: WordCloudChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.word_cloud_field_wells

        out["field_wells"] = (
            capo_quicksight.types.word_cloud_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.word_cloud_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.word_cloud_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("CategoryLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if data.get("WordCloudOptions") is not None:
        import capo_quicksight.types.word_cloud_options

        out["word_cloud_options"] = (
            capo_quicksight.types.word_cloud_options.deserialize_json(
                data["WordCloudOptions"]
            )
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: WordCloudChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.word_cloud_field_wells

        out["field_wells"] = (
            capo_quicksight.types.word_cloud_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    return out
