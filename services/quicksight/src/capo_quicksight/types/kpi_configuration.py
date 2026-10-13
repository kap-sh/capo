"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kpi_field_wells
    import capo_quicksight.types.kpi_options
    import capo_quicksight.types.kpi_sort_configuration
    import capo_quicksight.types.visual_interaction_options


class KPIConfiguration(TypedDict, closed=True):
    field_wells: NotRequired["capo_quicksight.types.kpi_field_wells.KPIFieldWells"]
    """<p>The field well configuration of a KPI visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.kpi_sort_configuration.KPISortConfiguration"
    ]
    """<p>The sort configuration of a KPI visual.</p>"""
    kpi_options: NotRequired["capo_quicksight.types.kpi_options.KPIOptions"]
    """<p>The options that determine the presentation of a KPI visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.kpi_field_wells

        out["FieldWells"] = capo_quicksight.types.kpi_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.kpi_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.kpi_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "kpi_options" in value:
        import capo_quicksight.types.kpi_options

        out["KPIOptions"] = capo_quicksight.types.kpi_options.serialize_json(
            value["kpi_options"]
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIConfiguration:
    out: KPIConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.kpi_field_wells

        out["field_wells"] = capo_quicksight.types.kpi_field_wells.deserialize_json(
            data["FieldWells"]
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.kpi_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.kpi_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("KPIOptions") is not None:
        import capo_quicksight.types.kpi_options

        out["kpi_options"] = capo_quicksight.types.kpi_options.deserialize_json(
            data["KPIOptions"]
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: KPIConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.kpi_field_wells

        out["field_wells"] = capo_quicksight.types.kpi_field_wells.redact_sensitive(
            value["field_wells"]
        )
    if "kpi_options" in value:
        import capo_quicksight.types.kpi_options

        out["kpi_options"] = capo_quicksight.types.kpi_options.redact_sensitive(
            value["kpi_options"]
        )
    return out
