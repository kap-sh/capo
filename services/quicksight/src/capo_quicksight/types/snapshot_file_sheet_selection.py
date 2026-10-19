"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileSheetSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.snapshot_file_sheet_selection_scope
    import capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list


class SnapshotFileSheetSelection(TypedDict, closed=True):
    sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The sheet ID of the dashboard to generate the snapshot artifact from. This value is required for CSV, Excel, and PDF format types.</p>"""
    selection_scope: "capo_quicksight.types.snapshot_file_sheet_selection_scope.SnapshotFileSheetSelectionScope"
    """<p>The selection scope of the visuals on a sheet of a dashboard that you are generating a snapthot of. You can choose one of the following options.</p> <ul> <li> <p> <code>ALL_VISUALS</code> - Selects all visuals that are on the sheet. This value is required if the snapshot is a PDF.</p> </li> <li> <p> <code>SELECTED_VISUALS</code> - Select the visual that you want to add to the snapshot. This value is required if the snapshot is a CSV or Excel workbook.</p> </li> </ul>"""
    visual_ids: NotRequired[
        "capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list.SnapshotFileSheetSelectionVisualIdList"
    ]
    """<p> A structure that lists the IDs of the visuals in the selected sheet. Supported visual types are table, pivot table visuals. This value is required if you are generating a CSV or Excel workbook. This value supports a maximum of 1 visual ID for CSV and 5 visual IDs across up to 5 sheet selections for Excel. If you are generating an Excel workbook, the order of the visual IDs provided in this structure determines the order of the worksheets in the Excel file. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileSheetSelection) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    import capo_quicksight.types.snapshot_file_sheet_selection_scope

    out["SelectionScope"] = (
        capo_quicksight.types.snapshot_file_sheet_selection_scope.serialize_json(
            value["selection_scope"]
        )
    )
    if "visual_ids" in value:
        import capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list

        out["VisualIds"] = (
            capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list.serialize_json(
                value["visual_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotFileSheetSelection:
    out: SnapshotFileSheetSelection = {}  # type: ignore[typeddict-item]
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    else:
        out["sheet_id"] = ""
    if data.get("SelectionScope") is not None:
        import capo_quicksight.types.snapshot_file_sheet_selection_scope

        out["selection_scope"] = (
            capo_quicksight.types.snapshot_file_sheet_selection_scope.deserialize_json(
                data["SelectionScope"]
            )
        )
    else:
        import typing

        out["selection_scope"] = typing.cast(
            "capo_quicksight.types.snapshot_file_sheet_selection_scope.SnapshotFileSheetSelectionScope",
            "",
        )
    if data.get("VisualIds") is not None:
        import capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list

        out["visual_ids"] = (
            capo_quicksight.types.snapshot_file_sheet_selection_visual_id_list.deserialize_json(
                data["VisualIds"]
            )
        )
    return out
