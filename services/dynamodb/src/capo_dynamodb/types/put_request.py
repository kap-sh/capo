"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.put_item_input_attribute_map


class PutRequest(TypedDict, closed=True):
    item: "capo_dynamodb.types.put_item_input_attribute_map.PutItemInputAttributeMap"
    """<p>A map of attribute name to attribute values, representing the primary key of an item to be processed by <code>PutItem</code>. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRequest) -> dict:
    out: dict = {}
    import capo_dynamodb.types.put_item_input_attribute_map

    out["Item"] = (
        capo_dynamodb.types.put_item_input_attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutRequest:
    out: PutRequest = {}  # type: ignore[typeddict-item]
    if data.get("Item") is not None:
        import capo_dynamodb.types.put_item_input_attribute_map

        out["item"] = (
            capo_dynamodb.types.put_item_input_attribute_map.deserialize_aws_json_1_0(
                data["Item"]
            )
        )
    else:
        out["item"] = {}
    return out
