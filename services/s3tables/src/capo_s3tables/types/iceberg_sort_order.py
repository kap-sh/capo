"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_sort_field_list


class IcebergSortOrder(TypedDict, closed=True):
    order_id: "int"
    """<p>The unique identifier for this sort order. If not specified, defaults to <code>1</code>. The order ID is used by Apache Iceberg to track sort order evolution.</p>"""
    fields: "capo_s3tables.types.iceberg_sort_field_list.IcebergSortFieldList"
    """<p>The list of sort fields that define how data is sorted within files. Each field specifies a source field, sort direction, and null ordering. This field is required if <code>writeOrder</code> is provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSortOrder) -> dict:
    out: dict = {}
    out["order-id"] = value["order_id"]
    import capo_s3tables.types.iceberg_sort_field_list

    out["fields"] = capo_s3tables.types.iceberg_sort_field_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> IcebergSortOrder:
    out: IcebergSortOrder = {}  # type: ignore[typeddict-item]
    if data.get("order-id") is not None:
        out["order_id"] = data["order-id"]
    else:
        out["order_id"] = 0
    if data.get("fields") is not None:
        import capo_s3tables.types.iceberg_sort_field_list

        out["fields"] = capo_s3tables.types.iceberg_sort_field_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
