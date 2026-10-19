"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.search_vector_list
    import capo_dynamodb.types.string
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.top_k_integer


class SearchVectorsInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name or Amazon Resource Name (ARN) of the table containing the vector index.</p>"""
    index_name: "capo_dynamodb.types.index_name.IndexName"
    """<p>The name of the vector index to search. The index must be in the <code>ACTIVE</code> state.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. Use the <code>#</code> character in an expression to dereference an attribute name.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression. Use the <code>:</code> character in an expression to dereference an attribute value.</p>"""
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes to retrieve from the index. Separate attribute names with commas. If not specified, the operation returns all attributes projected into the vector index.</p> <p>Only attributes projected into the vector index can be retrieved.</p>"""
    search_vector: "capo_dynamodb.types.search_vector_list.SearchVectorList"
    """<p>The search vector to compare against the indexed vectors. Each element is a 32-bit IEEE-754 floating point number, provided in DynamoDB list format.</p> <p>The number of dimensions must match the number of dimensions configured for the vector index.</p>"""
    search_condition_expression: NotRequired["capo_dynamodb.types.string.String"]
    """<p>A condition expression used to filter the vector search results. The expression can reference attributes defined in the vector index search schema, including <code>HASH</code> and <code>INLINE_FILTER</code> key elements.</p> <p>Only the equality operator (<code>=</code>) is supported for <code>HASH</code> attributes. Comparison and range operators are supported for <code>INLINE_FILTER</code> attributes. Only top-level attributes from the search schema can be referenced.</p>"""
    top_k: "capo_dynamodb.types.top_k_integer.TopKInteger"
    """<p>The number of most similar results to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchVectorsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["IndexName"] = value["index_name"]
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    if "expression_attribute_names" in value:
        import capo_dynamodb.types.expression_attribute_name_map

        out["ExpressionAttributeNames"] = (
            capo_dynamodb.types.expression_attribute_name_map.serialize_aws_json_1_0(
                value["expression_attribute_names"]
            )
        )
    if "expression_attribute_values" in value:
        import capo_dynamodb.types.expression_attribute_value_map

        out["ExpressionAttributeValues"] = (
            capo_dynamodb.types.expression_attribute_value_map.serialize_aws_json_1_0(
                value["expression_attribute_values"]
            )
        )
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    import capo_dynamodb.types.search_vector_list

    out["SearchVector"] = capo_dynamodb.types.search_vector_list.serialize_aws_json_1_0(
        value["search_vector"]
    )
    if "search_condition_expression" in value:
        out["SearchConditionExpression"] = value["search_condition_expression"]
    out["TopK"] = value["top_k"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchVectorsInput:
    out: SearchVectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    else:
        out["index_name"] = ""
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    if data.get("ExpressionAttributeNames") is not None:
        import capo_dynamodb.types.expression_attribute_name_map

        out["expression_attribute_names"] = (
            capo_dynamodb.types.expression_attribute_name_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeNames"]
            )
        )
    if data.get("ExpressionAttributeValues") is not None:
        import capo_dynamodb.types.expression_attribute_value_map

        out["expression_attribute_values"] = (
            capo_dynamodb.types.expression_attribute_value_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeValues"]
            )
        )
    if data.get("ProjectionExpression") is not None:
        out["projection_expression"] = data["ProjectionExpression"]
    if data.get("SearchVector") is not None:
        import capo_dynamodb.types.search_vector_list

        out["search_vector"] = (
            capo_dynamodb.types.search_vector_list.deserialize_aws_json_1_0(
                data["SearchVector"]
            )
        )
    else:
        out["search_vector"] = []
    if data.get("SearchConditionExpression") is not None:
        out["search_condition_expression"] = data["SearchConditionExpression"]
    if data.get("TopK") is not None:
        out["top_k"] = data["TopK"]
    else:
        out["top_k"] = 0
    return out
