"""Generated from Smithy shape ``com.amazonaws.appstream#ListExportImageTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.export_image_tasks
    import capo_appstream.types.string


class ListExportImageTasksResult(TypedDict, closed=True):
    export_image_tasks: NotRequired[
        "capo_appstream.types.export_image_tasks.ExportImageTasks"
    ]
    """<p>The list of export image tasks that match the specified criteria.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use for retrieving the next page of results. This field is only present when there are more results available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExportImageTasksResult) -> dict:
    out: dict = {}
    if "export_image_tasks" in value:
        import capo_appstream.types.export_image_tasks

        out["ExportImageTasks"] = (
            capo_appstream.types.export_image_tasks.serialize_aws_json_1_1(
                value["export_image_tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExportImageTasksResult:
    out: ListExportImageTasksResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTasks") is not None:
        import capo_appstream.types.export_image_tasks

        out["export_image_tasks"] = (
            capo_appstream.types.export_image_tasks.deserialize_aws_json_1_1(
                data["ExportImageTasks"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListExportImageTasksResult) -> dict:
    out: dict = {}
    if "export_image_tasks" in value:
        import capo_appstream.types.export_image_tasks

        out["ExportImageTasks"] = (
            capo_appstream.types.export_image_tasks.serialize_cbor(
                value["export_image_tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListExportImageTasksResult:
    out: ListExportImageTasksResult = {}  # type: ignore[typeddict-item]
    if data.get("ExportImageTasks") is not None:
        import capo_appstream.types.export_image_tasks

        out["export_image_tasks"] = (
            capo_appstream.types.export_image_tasks.deserialize_cbor(
                data["ExportImageTasks"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
