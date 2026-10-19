"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchSchemaElement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name
    import capo_dynamodb.types.search_schema_element_type


class SearchSchemaElement(TypedDict, closed=True):
    attribute_name: "capo_dynamodb.types.attribute_name.AttributeName"
    """<p>The name of the attribute.</p>"""
    search_schema_element_type: (
        "capo_dynamodb.types.search_schema_element_type.SearchSchemaElementType"
    )
    """<p>The role of the attribute in the search schema. Valid values:</p> <ul> <li> <p> <code>HASH</code> - A partition key that partitions the vector index for independent scaling. When specified, you must provide this attribute's value in the <code>SearchConditionExpression</code>.</p> </li> <li> <p> <code>INLINE_FILTER</code> - An attribute projected into the vector index for filtering at the storage layer during search. Inline filters are optional in the <code>SearchConditionExpression</code>.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSchemaElement) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_dynamodb.types.search_schema_element_type

    out["SearchSchemaElementType"] = (
        capo_dynamodb.types.search_schema_element_type.serialize_aws_json_1_0(
            value["search_schema_element_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchSchemaElement:
    out: SearchSchemaElement = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("SearchSchemaElementType") is not None:
        import capo_dynamodb.types.search_schema_element_type

        out["search_schema_element_type"] = (
            capo_dynamodb.types.search_schema_element_type.deserialize_aws_json_1_0(
                data["SearchSchemaElementType"]
            )
        )
    else:
        import typing

        out["search_schema_element_type"] = typing.cast(
            "capo_dynamodb.types.search_schema_element_type.SearchSchemaElementType", ""
        )
    return out
