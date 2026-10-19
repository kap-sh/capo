"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteKeyspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_name


class DeleteKeyspaceRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeyspaceRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeyspaceRequest:
    out: DeleteKeyspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    return out
