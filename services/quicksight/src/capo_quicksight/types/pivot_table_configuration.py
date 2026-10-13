"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_customization_visual_options
    import capo_quicksight.types.pivot_table_field_options
    import capo_quicksight.types.pivot_table_field_wells
    import capo_quicksight.types.pivot_table_options
    import capo_quicksight.types.pivot_table_paginated_report_options
    import capo_quicksight.types.pivot_table_sort_configuration
    import capo_quicksight.types.pivot_table_total_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options


class PivotTableConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.pivot_table_field_wells.PivotTableFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.pivot_table_sort_configuration.PivotTableSortConfiguration"
    ]
    """<p>The sort configuration for a <code>PivotTableVisual</code>.</p>"""
    table_options: NotRequired[
        "capo_quicksight.types.pivot_table_options.PivotTableOptions"
    ]
    """<p>The table options for a pivot table visual.</p>"""
    total_options: NotRequired[
        "capo_quicksight.types.pivot_table_total_options.PivotTableTotalOptions"
    ]
    """<p>The total options for a pivot table visual.</p>"""
    field_options: NotRequired[
        "capo_quicksight.types.pivot_table_field_options.PivotTableFieldOptions"
    ]
    """<p>The field options for a pivot table visual.</p>"""
    paginated_report_options: NotRequired[
        "capo_quicksight.types.pivot_table_paginated_report_options.PivotTablePaginatedReportOptions"
    ]
    """<p>The paginated report options for a pivot table visual.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    dashboard_customization_visual_options: NotRequired[
        "capo_quicksight.types.dashboard_customization_visual_options.DashboardCustomizationVisualOptions"
    ]
    """<p>The options that define customizations available to dashboard readers for a specific visual</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.pivot_table_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.pivot_table_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.pivot_table_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.pivot_table_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "table_options" in value:
        import capo_quicksight.types.pivot_table_options

        out["TableOptions"] = capo_quicksight.types.pivot_table_options.serialize_json(
            value["table_options"]
        )
    if "total_options" in value:
        import capo_quicksight.types.pivot_table_total_options

        out["TotalOptions"] = (
            capo_quicksight.types.pivot_table_total_options.serialize_json(
                value["total_options"]
            )
        )
    if "field_options" in value:
        import capo_quicksight.types.pivot_table_field_options

        out["FieldOptions"] = (
            capo_quicksight.types.pivot_table_field_options.serialize_json(
                value["field_options"]
            )
        )
    if "paginated_report_options" in value:
        import capo_quicksight.types.pivot_table_paginated_report_options

        out["PaginatedReportOptions"] = (
            capo_quicksight.types.pivot_table_paginated_report_options.serialize_json(
                value["paginated_report_options"]
            )
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "dashboard_customization_visual_options" in value:
        import capo_quicksight.types.dashboard_customization_visual_options

        out["DashboardCustomizationVisualOptions"] = (
            capo_quicksight.types.dashboard_customization_visual_options.serialize_json(
                value["dashboard_customization_visual_options"]
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


def deserialize_json(data: dict) -> PivotTableConfiguration:
    out: PivotTableConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.pivot_table_field_wells

        out["field_wells"] = (
            capo_quicksight.types.pivot_table_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.pivot_table_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.pivot_table_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("TableOptions") is not None:
        import capo_quicksight.types.pivot_table_options

        out["table_options"] = (
            capo_quicksight.types.pivot_table_options.deserialize_json(
                data["TableOptions"]
            )
        )
    if data.get("TotalOptions") is not None:
        import capo_quicksight.types.pivot_table_total_options

        out["total_options"] = (
            capo_quicksight.types.pivot_table_total_options.deserialize_json(
                data["TotalOptions"]
            )
        )
    if data.get("FieldOptions") is not None:
        import capo_quicksight.types.pivot_table_field_options

        out["field_options"] = (
            capo_quicksight.types.pivot_table_field_options.deserialize_json(
                data["FieldOptions"]
            )
        )
    if data.get("PaginatedReportOptions") is not None:
        import capo_quicksight.types.pivot_table_paginated_report_options

        out["paginated_report_options"] = (
            capo_quicksight.types.pivot_table_paginated_report_options.deserialize_json(
                data["PaginatedReportOptions"]
            )
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("DashboardCustomizationVisualOptions") is not None:
        import capo_quicksight.types.dashboard_customization_visual_options

        out["dashboard_customization_visual_options"] = (
            capo_quicksight.types.dashboard_customization_visual_options.deserialize_json(
                data["DashboardCustomizationVisualOptions"]
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


def redact_sensitive(value: PivotTableConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.pivot_table_field_wells

        out["field_wells"] = (
            capo_quicksight.types.pivot_table_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.pivot_table_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.pivot_table_sort_configuration.redact_sensitive(
                value["sort_configuration"]
            )
        )
    if "field_options" in value:
        import capo_quicksight.types.pivot_table_field_options

        out["field_options"] = (
            capo_quicksight.types.pivot_table_field_options.redact_sensitive(
                value["field_options"]
            )
        )
    return out
