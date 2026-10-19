"""Generated from Smithy shape ``com.amazonaws.glue#FieldDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.bool
    import capo_glue.types.field_data_type
    import capo_glue.types.filter_overrides


class FieldDefinition(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field in the entity schema.</p>"""
    field_data_type: "capo_glue.types.field_data_type.FieldDataType"
    """<p>The data type of the field.</p>"""
    response_date_format: NotRequired["str"]
    """<p>The format pattern for parsing date values from API responses. Required when the API uses a non-ISO-8601 format. Accepts Java <code>DateTimeFormatter</code> patterns (for example, <code>EEE, d MMM yyyy HH:mm:ss Z</code>), <code>EPOCH_SECONDS</code> for Unix epoch seconds, or <code>EPOCH_MILLIS</code> for Unix epoch milliseconds.</p>"""
    is_partitionable: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be used for partitioning queries to the data source.</p>"""
    is_nullable: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether this field can contain null values.</p>"""
    is_queryable: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be used in filter predicates when querying data.</p>"""
    is_orderable: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether this field can be used for ordering results.</p>"""
    filter_overrides: NotRequired["capo_glue.types.filter_overrides.FilterOverrides"]
    """<p>Per-field overrides for filter behavior, allowing customization of how filters are applied to this specific field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.field_data_type

    out["FieldDataType"] = capo_glue.types.field_data_type.serialize_aws_json_1_1(
        value["field_data_type"]
    )
    if "response_date_format" in value:
        out["ResponseDateFormat"] = value["response_date_format"]
    if "is_partitionable" in value:
        out["IsPartitionable"] = value["is_partitionable"]
    if "is_nullable" in value:
        out["IsNullable"] = value["is_nullable"]
    if "is_queryable" in value:
        out["IsQueryable"] = value["is_queryable"]
    if "is_orderable" in value:
        out["IsOrderable"] = value["is_orderable"]
    if "filter_overrides" in value:
        import capo_glue.types.filter_overrides

        out["FilterOverrides"] = (
            capo_glue.types.filter_overrides.serialize_aws_json_1_1(
                value["filter_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldDefinition:
    out: FieldDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("FieldDataType") is not None:
        import capo_glue.types.field_data_type

        out["field_data_type"] = (
            capo_glue.types.field_data_type.deserialize_aws_json_1_1(
                data["FieldDataType"]
            )
        )
    else:
        import typing

        out["field_data_type"] = typing.cast(
            "capo_glue.types.field_data_type.FieldDataType", ""
        )
    if data.get("ResponseDateFormat") is not None:
        out["response_date_format"] = data["ResponseDateFormat"]
    if data.get("IsPartitionable") is not None:
        out["is_partitionable"] = data["IsPartitionable"]
    if data.get("IsNullable") is not None:
        out["is_nullable"] = data["IsNullable"]
    if data.get("IsQueryable") is not None:
        out["is_queryable"] = data["IsQueryable"]
    if data.get("IsOrderable") is not None:
        out["is_orderable"] = data["IsOrderable"]
    if data.get("FilterOverrides") is not None:
        import capo_glue.types.filter_overrides

        out["filter_overrides"] = (
            capo_glue.types.filter_overrides.deserialize_aws_json_1_1(
                data["FilterOverrides"]
            )
        )
    return out
