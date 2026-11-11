"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_update_case_error_entry_list
    import capo_connectcases.types.batch_update_case_success_entry_list


class BatchUpdateCaseResponse(TypedDict, closed=True):
    successful_cases: "capo_connectcases.types.batch_update_case_success_entry_list.BatchUpdateCaseSuccessEntryList"
    """<p>The list of cases that were successfully updated.</p>"""
    failed_cases: "capo_connectcases.types.batch_update_case_error_entry_list.BatchUpdateCaseErrorEntryList"
    """<p>The list of cases that were not updated. Each entry includes an error code and message. Possible error codes include:</p> <ul> <li> <p> <code>CASE_NOT_FOUND</code> - No case exists with the specified case ID.</p> </li> <li> <p> <code>VALIDATION_ERROR</code> - The request contains invalid input.</p> </li> <li> <p> <code>CONFLICT</code> - Another operation is in progress on the case, such as a concurrent update or a merge of the case into another case.</p> </li> <li> <p> <code>THROTTLED</code> - The request rate exceeded the allowed limit.</p> </li> <li> <p> <code>ACCESS_DENIED</code> - The caller lacks permission to perform the operation.</p> </li> <li> <p> <code>SERVICE_QUOTA_EXCEEDED</code> - The request exceeded a service quota.</p> </li> <li> <p> <code>DOMAIN_NOT_FOUND</code> - The case domain was deleted while the request was being processed.</p> </li> <li> <p> <code>INTERNAL_ERROR</code> - An unexpected error occurred on the server.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.batch_update_case_success_entry_list

    out["successfulCases"] = (
        capo_connectcases.types.batch_update_case_success_entry_list.serialize_json(
            value["successful_cases"]
        )
    )
    import capo_connectcases.types.batch_update_case_error_entry_list

    out["failedCases"] = (
        capo_connectcases.types.batch_update_case_error_entry_list.serialize_json(
            value["failed_cases"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateCaseResponse:
    out: BatchUpdateCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("successfulCases") is not None:
        import capo_connectcases.types.batch_update_case_success_entry_list

        out["successful_cases"] = (
            capo_connectcases.types.batch_update_case_success_entry_list.deserialize_json(
                data["successfulCases"]
            )
        )
    else:
        out["successful_cases"] = []
    if data.get("failedCases") is not None:
        import capo_connectcases.types.batch_update_case_error_entry_list

        out["failed_cases"] = (
            capo_connectcases.types.batch_update_case_error_entry_list.deserialize_json(
                data["failedCases"]
            )
        )
    else:
        out["failed_cases"] = []
    return out
