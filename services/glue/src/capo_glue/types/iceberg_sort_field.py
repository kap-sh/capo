"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_null_order
    import capo_glue.types.iceberg_sort_direction
    import capo_glue.types.iceberg_transform_string
    import capo_glue.types.integer


class IcebergSortField(TypedDict, closed=True):
    source_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the source field from the table schema that this sort field is based on.</p>"""
    transform: "capo_glue.types.iceberg_transform_string.IcebergTransformString"
    """<p>The transformation function applied to the source field before sorting, such as identity, bucket, or truncate.</p>"""
    direction: "capo_glue.types.iceberg_sort_direction.IcebergSortDirection"
    """<p>The sort direction for this field, either ascending or descending.</p>"""
    null_order: "capo_glue.types.iceberg_null_order.IcebergNullOrder"
    """<p>The ordering behavior for null values in this field, specifying whether nulls should appear first or last in the sort order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortField) -> dict:
    out: dict = {}
    out["SourceId"] = value.get("source_id", 0)
    out["Transform"] = value["transform"]
    import capo_glue.types.iceberg_sort_direction

    out["Direction"] = capo_glue.types.iceberg_sort_direction.serialize_aws_json_1_1(
        value["direction"]
    )
    import capo_glue.types.iceberg_null_order

    out["NullOrder"] = capo_glue.types.iceberg_null_order.serialize_aws_json_1_1(
        value["null_order"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSortField:
    out: IcebergSortField = {}  # type: ignore[typeddict-item]
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    else:
        out["source_id"] = 0
    if data.get("Transform") is not None:
        out["transform"] = data["Transform"]
    else:
        out["transform"] = ""
    if data.get("Direction") is not None:
        import capo_glue.types.iceberg_sort_direction

        out["direction"] = (
            capo_glue.types.iceberg_sort_direction.deserialize_aws_json_1_1(
                data["Direction"]
            )
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_glue.types.iceberg_sort_direction.IcebergSortDirection", ""
        )
    if data.get("NullOrder") is not None:
        import capo_glue.types.iceberg_null_order

        out["null_order"] = capo_glue.types.iceberg_null_order.deserialize_aws_json_1_1(
            data["NullOrder"]
        )
    else:
        import typing

        out["null_order"] = typing.cast(
            "capo_glue.types.iceberg_null_order.IcebergNullOrder", ""
        )
    return out
