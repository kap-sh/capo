"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.batch_describe_data_table_value_failure_result_list
    import capo_connect.types.batch_describe_data_table_value_success_result_list


class BatchDescribeDataTableValueResponse(TypedDict, closed=True):
    successful: "capo_connect.types.batch_describe_data_table_value_success_result_list.BatchDescribeDataTableValueSuccessResultList"
    """<p>A list of successfully retrieved values with their data, metadata, and lock version information.</p>"""
    failed: "capo_connect.types.batch_describe_data_table_value_failure_result_list.BatchDescribeDataTableValueFailureResultList"
    """<p>A list of values that failed to be retrieved with error messages explaining the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueResponse) -> dict:
    out: dict = {}
    import capo_connect.types.batch_describe_data_table_value_success_result_list

    out["Successful"] = (
        capo_connect.types.batch_describe_data_table_value_success_result_list.serialize_json(
            value["successful"]
        )
    )
    import capo_connect.types.batch_describe_data_table_value_failure_result_list

    out["Failed"] = (
        capo_connect.types.batch_describe_data_table_value_failure_result_list.serialize_json(
            value["failed"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDescribeDataTableValueResponse:
    out: BatchDescribeDataTableValueResponse = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_connect.types.batch_describe_data_table_value_success_result_list

        out["successful"] = (
            capo_connect.types.batch_describe_data_table_value_success_result_list.deserialize_json(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_connect.types.batch_describe_data_table_value_failure_result_list

        out["failed"] = (
            capo_connect.types.batch_describe_data_table_value_failure_result_list.deserialize_json(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
