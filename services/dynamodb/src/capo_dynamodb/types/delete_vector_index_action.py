"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteVectorIndexAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name


class DeleteVectorIndexAction(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the vector index to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVectorIndexAction) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVectorIndexAction:
    out: DeleteVectorIndexAction = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    return out
