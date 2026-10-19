"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.connection_arn
    import capo_codestar_connections.types.tag_list


class CreateConnectionOutput(TypedDict, closed=True):
    connection_arn: "capo_codestar_connections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to be created. The ARN is used as the connection reference when the connection is shared between Amazon Web Services services.</p> <note> <p>The ARN is never reused if the connection is deleted.</p> </note>"""
    tags: NotRequired["capo_codestar_connections.types.tag_list.TagList"]
    """<p>Specifies the tags applied to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionOutput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    if "tags" in value:
        import capo_codestar_connections.types.tag_list

        out["Tags"] = capo_codestar_connections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionOutput:
    out: CreateConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("Tags") is not None:
        import capo_codestar_connections.types.tag_list

        out["tags"] = capo_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
