"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.projection


class LocalSecondaryIndex(TypedDict, closed=True):
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the local secondary index. The name must be unique among all other indexes on this table.</p>"""
    key_schema: "capo_dynamodb.types.key_schema.KeySchema"
    """<p>The complete key schema for the local secondary index, consisting of one or more pairs of attribute names and key types:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""
    projection: "capo_dynamodb.types.projection.Projection"
    """<p>Represents attributes that are copied (projected) from the table into the local secondary index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalSecondaryIndex) -> dict:
    out: dict = {}
    out["IndexName"] = value["index_name"]
    import capo_dynamodb.types.key_schema

    out["KeySchema"] = capo_dynamodb.types.key_schema.serialize_aws_json_1_0(
        value["key_schema"]
    )
    import capo_dynamodb.types.projection

    out["Projection"] = capo_dynamodb.types.projection.serialize_aws_json_1_0(
        value["projection"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LocalSecondaryIndex:
    out: LocalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("LocalSecondaryIndex.index_name required")
    if data.get("KeySchema") is not None:
        import capo_dynamodb.types.key_schema

        out["key_schema"] = capo_dynamodb.types.key_schema.deserialize_aws_json_1_0(
            data["KeySchema"]
        )
    else:
        raise DeserializationError("LocalSecondaryIndex.key_schema required")
    if data.get("Projection") is not None:
        import capo_dynamodb.types.projection

        out["projection"] = capo_dynamodb.types.projection.deserialize_aws_json_1_0(
            data["Projection"]
        )
    else:
        raise DeserializationError("LocalSecondaryIndex.projection required")
    return out
