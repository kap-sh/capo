"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.sankey_diagram_field_wells
    import capo_quicksight.types.sankey_diagram_sort_configuration
    import capo_quicksight.types.visual_interaction_options


class SankeyDiagramChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.sankey_diagram_field_wells.SankeyDiagramFieldWells"
    ]
    """<p>The field well configuration of a sankey diagram.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.sankey_diagram_sort_configuration.SankeyDiagramSortConfiguration"
    ]
    """<p>The sort configuration of a sankey diagram.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a sankey diagram.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.sankey_diagram_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.sankey_diagram_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.sankey_diagram_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.sankey_diagram_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["DataLabels"] = capo_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramChartConfiguration:
    out: SankeyDiagramChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.sankey_diagram_field_wells

        out["field_wells"] = (
            capo_quicksight.types.sankey_diagram_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.sankey_diagram_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.sankey_diagram_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("DataLabels") is not None:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.deserialize_json(
            data["DataLabels"]
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: SankeyDiagramChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.sankey_diagram_field_wells

        out["field_wells"] = (
            capo_quicksight.types.sankey_diagram_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.redact_sensitive(
            value["data_labels"]
        )
    return out
