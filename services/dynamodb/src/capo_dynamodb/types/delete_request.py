"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.key


class DeleteRequest(TypedDict, closed=True):
    key: "capo_dynamodb.types.key.Key"
    """<p>A map of attribute name to attribute values, representing the primary key of the item to delete. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRequest) -> dict:
    out: dict = {}
    import capo_dynamodb.types.key

    out["Key"] = capo_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRequest:
    out: DeleteRequest = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_dynamodb.types.key

        out["key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        out["key"] = {}
    return out
