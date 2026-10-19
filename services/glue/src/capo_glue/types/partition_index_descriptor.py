"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndexDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.backfill_errors
    import capo_glue.types.key_schema_element_list
    import capo_glue.types.name_string
    import capo_glue.types.partition_index_status


class PartitionIndexDescriptor(TypedDict, closed=True):
    index_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partition index.</p>"""
    keys: "capo_glue.types.key_schema_element_list.KeySchemaElementList"
    """<p>A list of one or more keys, as <code>KeySchemaElement</code> structures, for the partition index.</p>"""
    index_status: "capo_glue.types.partition_index_status.PartitionIndexStatus"
    """<p>The status of the partition index. </p> <p>The possible statuses are:</p> <ul> <li> <p>CREATING: The index is being created. When an index is in a CREATING state, the index or its table cannot be deleted.</p> </li> <li> <p>ACTIVE: The index creation succeeds.</p> </li> <li> <p>FAILED: The index creation fails. </p> </li> <li> <p>DELETING: The index is deleted from the list of indexes.</p> </li> </ul>"""
    backfill_errors: NotRequired["capo_glue.types.backfill_errors.BackfillErrors"]
    """<p>A list of errors that can occur when registering partition indexes for an existing table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndexDescriptor) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    import capo_glue.types.key_schema_element_list

    out["Keys"] = capo_glue.types.key_schema_element_list.serialize_aws_json_1_1(
        value["keys"]
    )
    import capo_glue.types.partition_index_status

    out["IndexStatus"] = capo_glue.types.partition_index_status.serialize_aws_json_1_1(
        value["index_status"]
    )
    if "backfill_errors" in value:
        import capo_glue.types.backfill_errors

        out["BackfillErrors"] = capo_glue.types.backfill_errors.serialize_aws_json_1_1(
            value["backfill_errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionIndexDescriptor:
    out: PartitionIndexDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("Keys") is not None:
        import capo_glue.types.key_schema_element_list

        out["keys"] = capo_glue.types.key_schema_element_list.deserialize_aws_json_1_1(
            data["Keys"]
        )
    else:
        out["keys"] = []
    if data.get("IndexStatus") is not None:
        import capo_glue.types.partition_index_status

        out["index_status"] = (
            capo_glue.types.partition_index_status.deserialize_aws_json_1_1(
                data["IndexStatus"]
            )
        )
    else:
        import typing

        out["index_status"] = typing.cast(
            "capo_glue.types.partition_index_status.PartitionIndexStatus", ""
        )
    if data.get("BackfillErrors") is not None:
        import capo_glue.types.backfill_errors

        out["backfill_errors"] = (
            capo_glue.types.backfill_errors.deserialize_aws_json_1_1(
                data["BackfillErrors"]
            )
        )
    return out
