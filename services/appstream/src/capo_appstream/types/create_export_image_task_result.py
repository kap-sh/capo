"""Generated from Smithy shape ``com.amazonaws.appstream#CreateExportImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.export_image_task


class CreateExportImageTaskResult(TypedDict, closed=True):
    export_image_task: NotRequired[
        "capo_appstream.types.export_image_task.ExportImageTask"
    ]
    """<p>Information about the export image task that was created, including the task ID and initial state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportImageTaskResult) -> dict:
    out: dict = {}
    if "export_image_task" in value:
        import capo_appstream.types.export_image_task

        out["ExportImageTask"] = (
            capo_appstream.types.export_image_task.serialize_aws_json_1_1(
                value["export_image_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportImageTaskResult:
    out: CreateExportImageTaskResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTask") is not None:
        import capo_appstream.types.export_image_task

        out["export_image_task"] = (
            capo_appstream.types.export_image_task.deserialize_aws_json_1_1(
                data["ExportImageTask"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateExportImageTaskResult) -> dict:
    out: dict = {}
    if "export_image_task" in value:
        import capo_appstream.types.export_image_task

        out["ExportImageTask"] = capo_appstream.types.export_image_task.serialize_cbor(
            value["export_image_task"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateExportImageTaskResult:
    out: CreateExportImageTaskResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTask") is not None:
        import capo_appstream.types.export_image_task

        out["export_image_task"] = (
            capo_appstream.types.export_image_task.deserialize_cbor(
                data["ExportImageTask"]
            )
        )
    return out
