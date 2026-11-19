"""Generated from Smithy shape ``com.amazonaws.appstream#GetExportImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.export_image_task


class GetExportImageTaskResult(TypedDict, closed=True):
    export_image_task: NotRequired[
        "capo_appstream.types.export_image_task.ExportImageTask"
    ]
    """<p>Information about the export image task, including its current state, created date, and any error details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportImageTaskResult) -> dict:
    out: dict = {}
    if "export_image_task" in value:
        import capo_appstream.types.export_image_task

        out["ExportImageTask"] = (
            capo_appstream.types.export_image_task.serialize_aws_json_1_1(
                value["export_image_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportImageTaskResult:
    out: GetExportImageTaskResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTask") is not None:
        import capo_appstream.types.export_image_task

        out["export_image_task"] = (
            capo_appstream.types.export_image_task.deserialize_aws_json_1_1(
                data["ExportImageTask"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetExportImageTaskResult) -> dict:
    out: dict = {}
    if "export_image_task" in value:
        import capo_appstream.types.export_image_task

        out["ExportImageTask"] = capo_appstream.types.export_image_task.serialize_cbor(
            value["export_image_task"]
        )
    return out


def deserialize_cbor(data: dict) -> GetExportImageTaskResult:
    out: GetExportImageTaskResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTask") is not None:
        import capo_appstream.types.export_image_task

        out["export_image_task"] = (
            capo_appstream.types.export_image_task.deserialize_cbor(
                data["ExportImageTask"]
            )
        )
    return out
