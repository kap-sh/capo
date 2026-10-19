"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.partition_key_enforcement_level
    import capo_timestream_write.types.partition_key_type
    import capo_timestream_write.types.schema_name


class PartitionKey(TypedDict, closed=True):
    type: "capo_timestream_write.types.partition_key_type.PartitionKeyType"
    """<p> The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key). </p>"""
    name: NotRequired["capo_timestream_write.types.schema_name.SchemaName"]
    """<p> The name of the attribute used for a dimension key. </p>"""
    enforcement_in_record: NotRequired[
        "capo_timestream_write.types.partition_key_enforcement_level.PartitionKeyEnforcementLevel"
    ]
    """<p> The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED (dimension key must be specified) and OPTIONAL (dimension key does not have to be specified). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKey) -> dict:
    out: dict = {}
    import capo_timestream_write.types.partition_key_type

    out["Type"] = capo_timestream_write.types.partition_key_type.serialize_aws_json_1_0(
        value["type"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "enforcement_in_record" in value:
        import capo_timestream_write.types.partition_key_enforcement_level

        out["EnforcementInRecord"] = (
            capo_timestream_write.types.partition_key_enforcement_level.serialize_aws_json_1_0(
                value["enforcement_in_record"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PartitionKey:
    out: PartitionKey = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_timestream_write.types.partition_key_type

        out["type"] = (
            capo_timestream_write.types.partition_key_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_timestream_write.types.partition_key_type.PartitionKeyType", ""
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EnforcementInRecord") is not None:
        import capo_timestream_write.types.partition_key_enforcement_level

        out["enforcement_in_record"] = (
            capo_timestream_write.types.partition_key_enforcement_level.deserialize_aws_json_1_0(
                data["EnforcementInRecord"]
            )
        )
    return out
