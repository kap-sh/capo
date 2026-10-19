"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_id
    import capo_iotsitewise.types.export_data_type_list
    import capo_iotsitewise.types.trim_settings


class DatasetItem(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.dataset_id.DatasetId"
    """<p>The unique identifier for the dataset.</p>"""
    trim_settings: NotRequired["capo_iotsitewise.types.trim_settings.TrimSettings"]
    """<p>The trim settings applied to all items in the dataset. When omitted, the full dataset time range is used.</p>"""
    export_data_types: NotRequired[
        "capo_iotsitewise.types.export_data_type_list.ExportDataTypeList"
    ]
    """<p>The optional subset of data types to export. If omitted, all data types are exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetItem) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    if "trim_settings" in value:
        import capo_iotsitewise.types.trim_settings

        out["trimSettings"] = capo_iotsitewise.types.trim_settings.serialize_json(
            value["trim_settings"]
        )
    if "export_data_types" in value:
        import capo_iotsitewise.types.export_data_type_list

        out["exportDataTypes"] = (
            capo_iotsitewise.types.export_data_type_list.serialize_json(
                value["export_data_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetItem:
    out: DatasetItem = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("trimSettings") is not None:
        import capo_iotsitewise.types.trim_settings

        out["trim_settings"] = capo_iotsitewise.types.trim_settings.deserialize_json(
            data["trimSettings"]
        )
    if data.get("exportDataTypes") is not None:
        import capo_iotsitewise.types.export_data_type_list

        out["export_data_types"] = (
            capo_iotsitewise.types.export_data_type_list.deserialize_json(
                data["exportDataTypes"]
            )
        )
    return out
