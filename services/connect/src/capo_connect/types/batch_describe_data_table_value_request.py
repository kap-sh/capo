"""Generated from Smithy shape ``com.amazonaws.connect#BatchDescribeDataTableValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_value_identifier_list
    import capo_connect.types.instance_id


class BatchDescribeDataTableValueRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    values: "capo_connect.types.data_table_value_identifier_list.DataTableValueIdentifierList"
    """<p>A list of value identifiers to retrieve, each specifying primary values and attribute names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeDataTableValueRequest) -> dict:
    out: dict = {}
    import capo_connect.types.data_table_value_identifier_list

    out["Values"] = capo_connect.types.data_table_value_identifier_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> BatchDescribeDataTableValueRequest:
    out: BatchDescribeDataTableValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_connect.types.data_table_value_identifier_list

        out["values"] = (
            capo_connect.types.data_table_value_identifier_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
