"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_sort_order_field_list
    import capo_glue.types.integer


class IcebergSortOrder(TypedDict, closed=True):
    order_id: "capo_glue.types.integer.Integer"
    """<p>The unique identifier for this sort order specification within the Iceberg table's metadata.</p>"""
    fields: "capo_glue.types.iceberg_sort_order_field_list.IcebergSortOrderFieldList"
    """<p>The list of fields and their sort directions that define the ordering criteria for the Iceberg table data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortOrder) -> dict:
    out: dict = {}
    out["OrderId"] = value.get("order_id", 0)
    import capo_glue.types.iceberg_sort_order_field_list

    out["Fields"] = (
        capo_glue.types.iceberg_sort_order_field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSortOrder:
    out: IcebergSortOrder = {}  # type: ignore[typeddict-item]
    if data.get("OrderId") is not None:
        out["order_id"] = data["OrderId"]
    else:
        out["order_id"] = 0
    if data.get("Fields") is not None:
        import capo_glue.types.iceberg_sort_order_field_list

        out["fields"] = (
            capo_glue.types.iceberg_sort_order_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        out["fields"] = []
    return out
