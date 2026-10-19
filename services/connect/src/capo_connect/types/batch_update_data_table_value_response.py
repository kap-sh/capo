"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.batch_update_data_table_value_failure_result_list
    import capo_connect.types.batch_update_data_table_value_success_result_list


class BatchUpdateDataTableValueResponse(TypedDict, closed=True):
    successful: "capo_connect.types.batch_update_data_table_value_success_result_list.BatchUpdateDataTableValueSuccessResultList"
    """<p>A list of successfully updated values with their new lock versions and identifiers.</p>"""
    failed: "capo_connect.types.batch_update_data_table_value_failure_result_list.BatchUpdateDataTableValueFailureResultList"
    """<p>A list of values that failed to be updated with error messages explaining the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueResponse) -> dict:
    out: dict = {}
    import capo_connect.types.batch_update_data_table_value_success_result_list

    out["Successful"] = (
        capo_connect.types.batch_update_data_table_value_success_result_list.serialize_json(
            value["successful"]
        )
    )
    import capo_connect.types.batch_update_data_table_value_failure_result_list

    out["Failed"] = (
        capo_connect.types.batch_update_data_table_value_failure_result_list.serialize_json(
            value["failed"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDataTableValueResponse:
    out: BatchUpdateDataTableValueResponse = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_connect.types.batch_update_data_table_value_success_result_list

        out["successful"] = (
            capo_connect.types.batch_update_data_table_value_success_result_list.deserialize_json(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_connect.types.batch_update_data_table_value_failure_result_list

        out["failed"] = (
            capo_connect.types.batch_update_data_table_value_failure_result_list.deserialize_json(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
