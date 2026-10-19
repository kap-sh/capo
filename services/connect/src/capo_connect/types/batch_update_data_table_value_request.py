"""Generated from Smithy shape ``com.amazonaws.connect#BatchUpdateDataTableValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_value_list
    import capo_connect.types.instance_id


class BatchUpdateDataTableValueRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    values: "capo_connect.types.data_table_value_list.DataTableValueList"
    """<p>A list of values to update, each including the current lock version to ensure optimistic locking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDataTableValueRequest) -> dict:
    out: dict = {}
    import capo_connect.types.data_table_value_list

    out["Values"] = capo_connect.types.data_table_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDataTableValueRequest:
    out: BatchUpdateDataTableValueRequest = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_connect.types.data_table_value_list

        out["values"] = capo_connect.types.data_table_value_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
