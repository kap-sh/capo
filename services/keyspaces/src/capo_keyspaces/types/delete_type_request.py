"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.type_name


class DeleteTypeRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace of the to be deleted type. </p>"""
    type_name: "capo_keyspaces.types.type_name.TypeName"
    """<p> The name of the type to be deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTypeRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["typeName"] = value["type_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTypeRequest:
    out: DeleteTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    return out
