"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_null_order
    import capo_s3tables.types.iceberg_sort_direction


class IcebergSortField(TypedDict, closed=True):
    source_id: "int"
    """<p>The ID of the source schema field to sort by. This must reference a valid field ID from the table schema.</p>"""
    transform: "str"
    """<p>The transform to apply to the source field before sorting. Use <code>identity</code> to sort by the field value directly, or specify other transforms as needed.</p>"""
    direction: "capo_s3tables.types.iceberg_sort_direction.IcebergSortDirection"
    """<p>The sort direction. Valid values are <code>asc</code> for ascending order or <code>desc</code> for descending order.</p>"""
    null_order: "capo_s3tables.types.iceberg_null_order.IcebergNullOrder"
    """<p>Specifies how null values are ordered. Valid values are <code>nulls-first</code> to place nulls before non-null values, or <code>nulls-last</code> to place nulls after non-null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSortField) -> dict:
    out: dict = {}
    out["source-id"] = value["source_id"]
    out["transform"] = value["transform"]
    import capo_s3tables.types.iceberg_sort_direction

    out["direction"] = capo_s3tables.types.iceberg_sort_direction.serialize_json(
        value["direction"]
    )
    import capo_s3tables.types.iceberg_null_order

    out["null-order"] = capo_s3tables.types.iceberg_null_order.serialize_json(
        value["null_order"]
    )
    return out


def deserialize_json(data: dict) -> IcebergSortField:
    out: IcebergSortField = {}  # type: ignore[typeddict-item]
    if data.get("source-id") is not None:
        out["source_id"] = data["source-id"]
    else:
        out["source_id"] = 0
    if data.get("transform") is not None:
        out["transform"] = data["transform"]
    else:
        out["transform"] = ""
    if data.get("direction") is not None:
        import capo_s3tables.types.iceberg_sort_direction

        out["direction"] = capo_s3tables.types.iceberg_sort_direction.deserialize_json(
            data["direction"]
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_s3tables.types.iceberg_sort_direction.IcebergSortDirection", ""
        )
    if data.get("null-order") is not None:
        import capo_s3tables.types.iceberg_null_order

        out["null_order"] = capo_s3tables.types.iceberg_null_order.deserialize_json(
            data["null-order"]
        )
    else:
        import typing

        out["null_order"] = typing.cast(
            "capo_s3tables.types.iceberg_null_order.IcebergNullOrder", ""
        )
    return out
