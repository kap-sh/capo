"""Generated from Smithy shape ``com.amazonaws.keyspaces#UpdateKeyspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.client_side_timestamps
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.replication_specification


class UpdateKeyspaceRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace. </p>"""
    replication_specification: (
        "capo_keyspaces.types.replication_specification.ReplicationSpecification"
    )
    client_side_timestamps: NotRequired[
        "capo_keyspaces.types.client_side_timestamps.ClientSideTimestamps"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKeyspaceRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    import capo_keyspaces.types.replication_specification

    out["replicationSpecification"] = (
        capo_keyspaces.types.replication_specification.serialize_aws_json_1_0(
            value["replication_specification"]
        )
    )
    if "client_side_timestamps" in value:
        import capo_keyspaces.types.client_side_timestamps

        out["clientSideTimestamps"] = (
            capo_keyspaces.types.client_side_timestamps.serialize_aws_json_1_0(
                value["client_side_timestamps"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKeyspaceRequest:
    out: UpdateKeyspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("replicationSpecification") is not None:
        import capo_keyspaces.types.replication_specification

        out["replication_specification"] = (
            capo_keyspaces.types.replication_specification.deserialize_aws_json_1_0(
                data["replicationSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateKeyspaceRequest.replication_specification required"
        )
    if data.get("clientSideTimestamps") is not None:
        import capo_keyspaces.types.client_side_timestamps

        out["client_side_timestamps"] = (
            capo_keyspaces.types.client_side_timestamps.deserialize_aws_json_1_0(
                data["clientSideTimestamps"]
            )
        )
    return out
