"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_export_file_type_list
    import capo_cleanroomsml.types.trained_model_exports_max_size


class TrainedModelExportsConfigurationPolicy(TypedDict, closed=True):
    max_size: "capo_cleanroomsml.types.trained_model_exports_max_size.TrainedModelExportsMaxSize"
    """<p>The maximum size of the data that can be exported.</p>"""
    files_to_export: "capo_cleanroomsml.types.trained_model_export_file_type_list.TrainedModelExportFileTypeList"
    """<p>The files that are exported during the trained model export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportsConfigurationPolicy) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_exports_max_size

    out["maxSize"] = (
        capo_cleanroomsml.types.trained_model_exports_max_size.serialize_json(
            value["max_size"]
        )
    )
    import capo_cleanroomsml.types.trained_model_export_file_type_list

    out["filesToExport"] = (
        capo_cleanroomsml.types.trained_model_export_file_type_list.serialize_json(
            value["files_to_export"]
        )
    )
    return out


def deserialize_json(data: dict) -> TrainedModelExportsConfigurationPolicy:
    out: TrainedModelExportsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if data.get("maxSize") is not None:
        import capo_cleanroomsml.types.trained_model_exports_max_size

        out["max_size"] = (
            capo_cleanroomsml.types.trained_model_exports_max_size.deserialize_json(
                data["maxSize"]
            )
        )
    else:
        raise DeserializationError(
            "TrainedModelExportsConfigurationPolicy.max_size required"
        )
    if data.get("filesToExport") is not None:
        import capo_cleanroomsml.types.trained_model_export_file_type_list

        out["files_to_export"] = (
            capo_cleanroomsml.types.trained_model_export_file_type_list.deserialize_json(
                data["filesToExport"]
            )
        )
    else:
        out["files_to_export"] = []
    return out
