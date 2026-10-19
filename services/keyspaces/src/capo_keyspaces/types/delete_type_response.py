"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.type_name


class DeleteTypeResponse(TypedDict, closed=True):
    keyspace_arn: "capo_keyspaces.types.arn.ARN"
    """<p> The unique identifier of the keyspace from which the type was deleted in the format of an Amazon Resource Name (ARN). </p>"""
    type_name: "capo_keyspaces.types.type_name.TypeName"
    """<p> The name of the type that was deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTypeResponse) -> dict:
    out: dict = {}
    out["keyspaceArn"] = value["keyspace_arn"]
    out["typeName"] = value["type_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTypeResponse:
    out: DeleteTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceArn") is not None:
        out["keyspace_arn"] = data["keyspaceArn"]
    else:
        out["keyspace_arn"] = ""
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    return out
