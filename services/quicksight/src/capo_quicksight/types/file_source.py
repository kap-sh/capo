"""Generated from Smithy shape ``com.amazonaws.quicksight#FileSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.integer
    import capo_quicksight.types.upload_settings


class FileSource(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the data source.</p>"""
    upload_settings: NotRequired["capo_quicksight.types.upload_settings.UploadSettings"]
    """<p>Information about the format for the source file.</p>"""
    sheet_index: "capo_quicksight.types.integer.Integer"
    """<p>The zero-based index of the sheet to use within the file. For files that contain multiple sheets, this identifies which sheet to read. Files that contain a single sheet, or that have no concept of sheets, use sheet 0.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The column schema of the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSource) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    if "upload_settings" in value:
        import capo_quicksight.types.upload_settings

        out["UploadSettings"] = capo_quicksight.types.upload_settings.serialize_json(
            value["upload_settings"]
        )
    out["SheetIndex"] = value.get("sheet_index", 0)
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> FileSource:
    out: FileSource = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        out["data_source_arn"] = ""
    if data.get("UploadSettings") is not None:
        import capo_quicksight.types.upload_settings

        out["upload_settings"] = capo_quicksight.types.upload_settings.deserialize_json(
            data["UploadSettings"]
        )
    if data.get("SheetIndex") is not None:
        out["sheet_index"] = data["SheetIndex"]
    else:
        out["sheet_index"] = 0
    if data.get("InputColumns") is not None:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        out["input_columns"] = []
    return out
