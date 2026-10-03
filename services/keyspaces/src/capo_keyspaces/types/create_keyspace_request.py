"""Generated from Smithy shape ``com.amazonaws.keyspaces#CreateKeyspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.replication_specification
    import capo_keyspaces.types.tag_list


class CreateKeyspaceRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace to be created.</p>"""
    tags: NotRequired["capo_keyspaces.types.tag_list.TagList"]
    """<p>A list of key-value pair tags to be attached to the keyspace.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html">Adding tags and labels to Amazon Keyspaces resources</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    replication_specification: NotRequired[
        "capo_keyspaces.types.replication_specification.ReplicationSpecification"
    ]
    """<p> The replication specification of the keyspace includes:</p> <ul> <li> <p> <code>replicationStrategy</code> - the required value is <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>.</p> </li> <li> <p> <code>regionList</code> - if the <code>replicationStrategy</code> is <code>MULTI_REGION</code>, the <code>regionList</code> requires the current Region and at least one additional Amazon Web Services Region where the keyspace is going to be replicated in.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateKeyspaceRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    if "tags" in value:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "replication_specification" in value:
        import capo_keyspaces.types.replication_specification

        out["replicationSpecification"] = (
            capo_keyspaces.types.replication_specification.serialize_aws_json_1_0(
                value["replication_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateKeyspaceRequest:
    out: CreateKeyspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("CreateKeyspaceRequest.keyspace_name required")
    if data.get("tags") is not None:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("replicationSpecification") is not None:
        import capo_keyspaces.types.replication_specification

        out["replication_specification"] = (
            capo_keyspaces.types.replication_specification.deserialize_aws_json_1_0(
                data["replicationSpecification"]
            )
        )
    return out
