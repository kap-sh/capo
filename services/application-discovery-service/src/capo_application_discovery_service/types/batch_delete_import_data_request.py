"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteImportDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.boolean
    import capo_application_discovery_service.types.to_delete_identifier_list


class BatchDeleteImportDataRequest(TypedDict, closed=True):
    import_task_ids: "capo_application_discovery_service.types.to_delete_identifier_list.ToDeleteIdentifierList"
    """<p>The IDs for the import tasks that you want to delete.</p>"""
    delete_history: NotRequired[
        "capo_application_discovery_service.types.boolean.Boolean"
    ]
    """<p> Set to <code>true</code> to remove the deleted import task from <a>DescribeImportTasks</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteImportDataRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.to_delete_identifier_list

    out["importTaskIds"] = (
        capo_application_discovery_service.types.to_delete_identifier_list.serialize_aws_json_1_1(
            value["import_task_ids"]
        )
    )
    if "delete_history" in value:
        out["deleteHistory"] = value["delete_history"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteImportDataRequest:
    out: BatchDeleteImportDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("importTaskIds") is not None:
        import capo_application_discovery_service.types.to_delete_identifier_list

        out["import_task_ids"] = (
            capo_application_discovery_service.types.to_delete_identifier_list.deserialize_aws_json_1_1(
                data["importTaskIds"]
            )
        )
    else:
        out["import_task_ids"] = []
    if data.get("deleteHistory") is not None:
        out["delete_history"] = data["deleteHistory"]
    return out
