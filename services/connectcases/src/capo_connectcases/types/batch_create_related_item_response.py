"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_error_entry_list
    import capo_connectcases.types.batch_create_related_item_success_entry_list


class BatchCreateRelatedItemResponse(TypedDict, closed=True):
    successful_items: "capo_connectcases.types.batch_create_related_item_success_entry_list.BatchCreateRelatedItemSuccessEntryList"
    """<p>The list of related items that were successfully created and associated with their cases.</p>"""
    failed_items: "capo_connectcases.types.batch_create_related_item_error_entry_list.BatchCreateRelatedItemErrorEntryList"
    """<p>The list of related items that were not created. Each entry includes an error code and message. Possible error codes include:</p> <ul> <li> <p> <code>CASE_NOT_FOUND</code> - No case exists with the specified case ID.</p> </li> <li> <p> <code>VALIDATION_ERROR</code> - The request contains invalid input.</p> </li> <li> <p> <code>CONFLICT</code> - Another operation is in progress on the case, such as a concurrent update or a merge of the case into another case.</p> </li> <li> <p> <code>THROTTLED</code> - The request rate exceeded the allowed limit.</p> </li> <li> <p> <code>ACCESS_DENIED</code> - The caller lacks permission to perform the operation.</p> </li> <li> <p> <code>SERVICE_QUOTA_EXCEEDED</code> - The request exceeded a service quota.</p> </li> <li> <p> <code>DOMAIN_NOT_FOUND</code> - The case domain was deleted while the request was being processed.</p> </li> <li> <p> <code>INTERNAL_ERROR</code> - An unexpected error occurred on the server.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.batch_create_related_item_success_entry_list

    out["successfulItems"] = (
        capo_connectcases.types.batch_create_related_item_success_entry_list.serialize_json(
            value["successful_items"]
        )
    )
    import capo_connectcases.types.batch_create_related_item_error_entry_list

    out["failedItems"] = (
        capo_connectcases.types.batch_create_related_item_error_entry_list.serialize_json(
            value["failed_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateRelatedItemResponse:
    out: BatchCreateRelatedItemResponse = {}  # type: ignore[typeddict-item]
    if data.get("successfulItems") is not None:
        import capo_connectcases.types.batch_create_related_item_success_entry_list

        out["successful_items"] = (
            capo_connectcases.types.batch_create_related_item_success_entry_list.deserialize_json(
                data["successfulItems"]
            )
        )
    else:
        out["successful_items"] = []
    if data.get("failedItems") is not None:
        import capo_connectcases.types.batch_create_related_item_error_entry_list

        out["failed_items"] = (
            capo_connectcases.types.batch_create_related_item_error_entry_list.deserialize_json(
                data["failedItems"]
            )
        )
    else:
        out["failed_items"] = []
    return out
