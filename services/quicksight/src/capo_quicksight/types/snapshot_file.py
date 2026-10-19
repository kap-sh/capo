"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_file_format_type
    import capo_quicksight.types.snapshot_file_sheet_selection_list


class SnapshotFile(TypedDict, closed=True):
    sheet_selections: "capo_quicksight.types.snapshot_file_sheet_selection_list.SnapshotFileSheetSelectionList"
    """<p>A list of <code>SnapshotFileSheetSelection</code> objects that contain information on the dashboard sheet that is exported. These objects provide information about the snapshot artifacts that are generated during the job. This structure can hold a maximum of 5 CSV configurations, 5 Excel configurations, or 1 configuration for PDF.</p>"""
    format_type: (
        "capo_quicksight.types.snapshot_file_format_type.SnapshotFileFormatType"
    )
    """<p>The format of the snapshot file to be generated. You can choose between <code>CSV</code>, <code>Excel</code>, or <code>PDF</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFile) -> dict:
    out: dict = {}
    import capo_quicksight.types.snapshot_file_sheet_selection_list

    out["SheetSelections"] = (
        capo_quicksight.types.snapshot_file_sheet_selection_list.serialize_json(
            value["sheet_selections"]
        )
    )
    import capo_quicksight.types.snapshot_file_format_type

    out["FormatType"] = capo_quicksight.types.snapshot_file_format_type.serialize_json(
        value["format_type"]
    )
    return out


def deserialize_json(data: dict) -> SnapshotFile:
    out: SnapshotFile = {}  # type: ignore[typeddict-item]
    if data.get("SheetSelections") is not None:
        import capo_quicksight.types.snapshot_file_sheet_selection_list

        out["sheet_selections"] = (
            capo_quicksight.types.snapshot_file_sheet_selection_list.deserialize_json(
                data["SheetSelections"]
            )
        )
    else:
        out["sheet_selections"] = []
    if data.get("FormatType") is not None:
        import capo_quicksight.types.snapshot_file_format_type

        out["format_type"] = (
            capo_quicksight.types.snapshot_file_format_type.deserialize_json(
                data["FormatType"]
            )
        )
    else:
        import typing

        out["format_type"] = typing.cast(
            "capo_quicksight.types.snapshot_file_format_type.SnapshotFileFormatType", ""
        )
    return out
