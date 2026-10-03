"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.conditional_operator
    import capo_dynamodb.types.expected_attribute_map
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.put_item_input_attribute_map
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.return_item_collection_metrics
    import capo_dynamodb.types.return_value
    import capo_dynamodb.types.return_values_on_condition_check_failure
    import capo_dynamodb.types.table_arn


class PutItemInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table to contain the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    item: "capo_dynamodb.types.put_item_input_attribute_map.PutItemInputAttributeMap"
    """<p>A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p> <p>You must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key.</p> <p>If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.</p> <p>If the table has vector indexes, the following validations apply to write operations. A violation of any of these constraints results in a <code>ValidationException</code>:</p> <ul> <li> <p>The vector attribute must be a list of numbers with dimensions matching the index configuration.</p> </li> <li> <p>Vector values must fit in 32-bit IEEE-754 floating point format (f32).</p> </li> <li> <p>Partition key and inline filter attributes defined in the search schema must have data types matching the index schema definition.</p> </li> </ul> <p>Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index.</p> <p>For more information about primary keys, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey">Primary Key</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>Each element in the <code>Item</code> map is an <code>AttributeValue</code> object.</p>"""
    expected: NotRequired[
        "capo_dynamodb.types.expected_attribute_map.ExpectedAttributeMap"
    ]
    """<p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html">Expected</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values: NotRequired["capo_dynamodb.types.return_value.ReturnValue"]
    """<p>Use <code>ReturnValues</code> if you want to get the item attributes as they appeared before they were updated with the <code>PutItem</code> request. For <code>PutItem</code>, the valid values are:</p> <ul> <li> <p> <code>NONE</code> - If <code>ReturnValues</code> is not specified, or if its value is <code>NONE</code>, then nothing is returned. (This setting is the default for <code>ReturnValues</code>.)</p> </li> <li> <p> <code>ALL_OLD</code> - If <code>PutItem</code> overwrote an attribute name-value pair, then the content of the old item is returned.</p> </li> </ul> <p>The values returned are strongly consistent.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p> <note> <p>The <code>ReturnValues</code> parameter is used by several DynamoDB operations; however, <code>PutItem</code> does not recognize any values other than <code>NONE</code> or <code>ALL_OLD</code>.</p> </note>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    return_item_collection_metrics: NotRequired[
        "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
    ]
    """<p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>"""
    conditional_operator: NotRequired[
        "capo_dynamodb.types.conditional_operator.ConditionalOperator"
    ]
    """<p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    condition_expression: NotRequired[
        "capo_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A condition that must be satisfied in order for a conditional <code>PutItem</code> operation to succeed.</p> <p>An expression can contain any of the following:</p> <ul> <li> <p>Functions: <code>attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size</code> </p> <p>These function names are case-sensitive.</p> </li> <li> <p>Comparison operators: <code>= | <> | < | > | <= | >= | BETWEEN | IN </code> </p> </li> <li> <p> Logical operators: <code>AND | OR | NOT</code> </p> </li> </ul> <p>For more information on condition expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <i>ProductStatus</i> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values_on_condition_check_failure: NotRequired[
        "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for a <code>PutItem</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutItemInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.put_item_input_attribute_map

    out["Item"] = (
        capo_dynamodb.types.put_item_input_attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    )
    if "expected" in value:
        import capo_dynamodb.types.expected_attribute_map

        out["Expected"] = (
            capo_dynamodb.types.expected_attribute_map.serialize_aws_json_1_0(
                value["expected"]
            )
        )
    if "return_values" in value:
        import capo_dynamodb.types.return_value

        out["ReturnValues"] = capo_dynamodb.types.return_value.serialize_aws_json_1_0(
            value["return_values"]
        )
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    if "return_item_collection_metrics" in value:
        import capo_dynamodb.types.return_item_collection_metrics

        out["ReturnItemCollectionMetrics"] = (
            capo_dynamodb.types.return_item_collection_metrics.serialize_aws_json_1_0(
                value["return_item_collection_metrics"]
            )
        )
    if "conditional_operator" in value:
        import capo_dynamodb.types.conditional_operator

        out["ConditionalOperator"] = (
            capo_dynamodb.types.conditional_operator.serialize_aws_json_1_0(
                value["conditional_operator"]
            )
        )
    if "condition_expression" in value:
        out["ConditionExpression"] = value["condition_expression"]
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
    if "return_values_on_condition_check_failure" in value:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutItemInput:
    out: PutItemInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("PutItemInput.table_name required")
    if data.get("Item") is not None:
        import capo_dynamodb.types.put_item_input_attribute_map

        out["item"] = (
            capo_dynamodb.types.put_item_input_attribute_map.deserialize_aws_json_1_0(
                data["Item"]
            )
        )
    else:
        raise DeserializationError("PutItemInput.item required")
    if data.get("Expected") is not None:
        import capo_dynamodb.types.expected_attribute_map

        out["expected"] = (
            capo_dynamodb.types.expected_attribute_map.deserialize_aws_json_1_0(
                data["Expected"]
            )
        )
    if data.get("ReturnValues") is not None:
        import capo_dynamodb.types.return_value

        out["return_values"] = (
            capo_dynamodb.types.return_value.deserialize_aws_json_1_0(
                data["ReturnValues"]
            )
        )
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    if data.get("ReturnItemCollectionMetrics") is not None:
        import capo_dynamodb.types.return_item_collection_metrics

        out["return_item_collection_metrics"] = (
            capo_dynamodb.types.return_item_collection_metrics.deserialize_aws_json_1_0(
                data["ReturnItemCollectionMetrics"]
            )
        )
    if data.get("ConditionalOperator") is not None:
        import capo_dynamodb.types.conditional_operator

        out["conditional_operator"] = (
            capo_dynamodb.types.conditional_operator.deserialize_aws_json_1_0(
                data["ConditionalOperator"]
            )
        )
    if data.get("ConditionExpression") is not None:
        out["condition_expression"] = data["ConditionExpression"]
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
    if data.get("ReturnValuesOnConditionCheckFailure") is not None:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
