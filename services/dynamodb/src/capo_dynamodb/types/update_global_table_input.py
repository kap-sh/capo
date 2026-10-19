"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_update_list
    import capo_dynamodb.types.table_name


class UpdateGlobalTableInput(TypedDict, closed=True):
    global_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replica_updates: "capo_dynamodb.types.replica_update_list.ReplicaUpdateList"
    """<p>A list of Regions that should be added or removed from the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    import capo_dynamodb.types.replica_update_list

    out["ReplicaUpdates"] = (
        capo_dynamodb.types.replica_update_list.serialize_aws_json_1_0(
            value["replica_updates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGlobalTableInput:
    out: UpdateGlobalTableInput = {}  # type: ignore[typeddict-item]
    if data.get("GlobalTableName") is not None:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        out["global_table_name"] = ""
    if data.get("ReplicaUpdates") is not None:
        import capo_dynamodb.types.replica_update_list

        out["replica_updates"] = (
            capo_dynamodb.types.replica_update_list.deserialize_aws_json_1_0(
                data["ReplicaUpdates"]
            )
        )
    else:
        out["replica_updates"] = []
    return out
