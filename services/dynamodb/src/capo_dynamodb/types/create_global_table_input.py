"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_list
    import capo_dynamodb.types.table_name


class CreateGlobalTableInput(TypedDict, closed=True):
    global_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replication_group: "capo_dynamodb.types.replica_list.ReplicaList"
    """<p>The Regions where the global table needs to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    import capo_dynamodb.types.replica_list

    out["ReplicationGroup"] = capo_dynamodb.types.replica_list.serialize_aws_json_1_0(
        value["replication_group"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateGlobalTableInput:
    out: CreateGlobalTableInput = {}  # type: ignore[typeddict-item]
    if data.get("GlobalTableName") is not None:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        out["global_table_name"] = ""
    if data.get("ReplicationGroup") is not None:
        import capo_dynamodb.types.replica_list

        out["replication_group"] = (
            capo_dynamodb.types.replica_list.deserialize_aws_json_1_0(
                data["ReplicationGroup"]
            )
        )
    else:
        out["replication_group"] = []
    return out
