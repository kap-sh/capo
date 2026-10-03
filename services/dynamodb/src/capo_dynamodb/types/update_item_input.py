"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_updates
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.conditional_operator
    import capo_dynamodb.types.expected_attribute_map
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.key
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.return_item_collection_metrics
    import capo_dynamodb.types.return_value
    import capo_dynamodb.types.return_values_on_condition_check_failure
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.update_expression


class UpdateItemInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table containing the item to update. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    key: "capo_dynamodb.types.key.Key"
    """<p>The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.</p> <p>For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.</p>"""
    attribute_updates: NotRequired[
        "capo_dynamodb.types.attribute_updates.AttributeUpdates"
    ]
    """<p>This is a legacy parameter. Use <code>UpdateExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributeUpdates.html">AttributeUpdates</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expected: NotRequired[
        "capo_dynamodb.types.expected_attribute_map.ExpectedAttributeMap"
    ]
    """<p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html">Expected</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    conditional_operator: NotRequired[
        "capo_dynamodb.types.conditional_operator.ConditionalOperator"
    ]
    """<p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values: NotRequired["capo_dynamodb.types.return_value.ReturnValue"]
    """<p>Use <code>ReturnValues</code> if you want to get the item attributes as they appear before or after they are successfully updated. For <code>UpdateItem</code>, the valid values are:</p> <ul> <li> <p> <code>NONE</code> - If <code>ReturnValues</code> is not specified, or if its value is <code>NONE</code>, then nothing is returned. (This setting is the default for <code>ReturnValues</code>.)</p> </li> <li> <p> <code>ALL_OLD</code> - Returns all of the attributes of the item, as they appeared before the UpdateItem operation.</p> </li> <li> <p> <code>UPDATED_OLD</code> - Returns only the updated attributes, as they appeared before the UpdateItem operation.</p> </li> <li> <p> <code>ALL_NEW</code> - Returns all of the attributes of the item, as they appear after the UpdateItem operation.</p> </li> <li> <p> <code>UPDATED_NEW</code> - Returns only the updated attributes, as they appear after the UpdateItem operation.</p> </li> </ul> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p> <p>The values returned are strongly consistent.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    return_item_collection_metrics: NotRequired[
        "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
    ]
    """<p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>"""
    update_expression: NotRequired[
        "capo_dynamodb.types.update_expression.UpdateExpression"
    ]
    """<p>An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them.</p> <p>The following action values are available for <code>UpdateExpression</code>.</p> <ul> <li> <p> <code>SET</code> - Adds one or more attributes and values to an item. If any of these attributes already exist, they are replaced by the new values. You can also use <code>SET</code> to add or subtract from an attribute that is of type Number. For example: <code>SET myNum = myNum + :val</code> </p> <p> <code>SET</code> supports the following functions:</p> <ul> <li> <p> <code>if_not_exists (path, operand)</code> - if the item does not contain an attribute at the specified path, then <code>if_not_exists</code> evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item.</p> </li> <li> <p> <code>list_append (operand, operand)</code> - evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands.</p> </li> </ul> <p>These function names are case-sensitive.</p> </li> <li> <p> <code>REMOVE</code> - Removes one or more attributes from an item.</p> </li> <li> <p> <code>ADD</code> - Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of <code>ADD</code> depends on the data type of the attribute:</p> <ul> <li> <p>If the existing attribute is a number, and if <code>Value</code> is also a number, then <code>Value</code> is mathematically added to the existing attribute. If <code>Value</code> is a negative number, then it is subtracted from the existing attribute.</p> <note> <p>If you use <code>ADD</code> to increment or decrement a number value for an item that doesn't exist before the update, DynamoDB uses <code>0</code> as the initial value.</p> <p>Similarly, if you use <code>ADD</code> for an existing item to increment or decrement an attribute value that doesn't exist before the update, DynamoDB uses <code>0</code> as the initial value. For example, suppose that the item you want to update doesn't have an attribute named <code>itemcount</code>, but you decide to <code>ADD</code> the number <code>3</code> to this attribute anyway. DynamoDB will create the <code>itemcount</code> attribute, set its initial value to <code>0</code>, and finally add <code>3</code> to it. The result will be a new <code>itemcount</code> attribute in the item, with a value of <code>3</code>.</p> </note> </li> <li> <p>If the existing data type is a set and if <code>Value</code> is also a set, then <code>Value</code> is added to the existing set. For example, if the attribute value is the set <code>[1,2]</code>, and the <code>ADD</code> action specified <code>[3]</code>, then the final attribute value is <code>[1,2,3]</code>. An error occurs if an <code>ADD</code> action is specified for a set attribute and the attribute type specified does not match the existing set type. </p> <p>Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the <code>Value</code> must also be a set of strings.</p> </li> </ul> <important> <p>The <code>ADD</code> action only supports Number and set data types.</p> </important> </li> <li> <p> <code>DELETE</code> - Deletes an element from a set.</p> <p>If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set <code>[a,b,c]</code> and the <code>DELETE</code> action specifies <code>[a,c]</code>, then the final attribute value is <code>[b]</code>. Specifying an empty set is an error.</p> <important> <p>The <code>DELETE</code> action only supports set data types.</p> </important> </li> </ul> <p>You can have many actions in a single expression, such as the following: <code>SET a=:value1, b=:value2 DELETE :value3, :value4, :value5</code> </p> <p>For more information on update expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.Modifying.html">Modifying Items and Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    condition_expression: NotRequired[
        "capo_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A condition that must be satisfied in order for a conditional update to succeed.</p> <p>An expression can contain any of the following:</p> <ul> <li> <p>Functions: <code>attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size</code> </p> <p>These function names are case-sensitive.</p> </li> <li> <p>Comparison operators: <code>= | <> | < | > | <= | >= | BETWEEN | IN </code> </p> </li> <li> <p> Logical operators: <code>AND | OR | NOT</code> </p> </li> </ul> <p>For more information about condition expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Specifying Conditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>.) To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information about expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <code>ProductStatus</code> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values_on_condition_check_failure: NotRequired[
        "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for an <code>UpdateItem</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateItemInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.key

    out["Key"] = capo_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    if "attribute_updates" in value:
        import capo_dynamodb.types.attribute_updates

        out["AttributeUpdates"] = (
            capo_dynamodb.types.attribute_updates.serialize_aws_json_1_0(
                value["attribute_updates"]
            )
        )
    if "expected" in value:
        import capo_dynamodb.types.expected_attribute_map

        out["Expected"] = (
            capo_dynamodb.types.expected_attribute_map.serialize_aws_json_1_0(
                value["expected"]
            )
        )
    if "conditional_operator" in value:
        import capo_dynamodb.types.conditional_operator

        out["ConditionalOperator"] = (
            capo_dynamodb.types.conditional_operator.serialize_aws_json_1_0(
                value["conditional_operator"]
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
    if "update_expression" in value:
        out["UpdateExpression"] = value["update_expression"]
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


def deserialize_aws_json_1_0(data: dict) -> UpdateItemInput:
    out: UpdateItemInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdateItemInput.table_name required")
    if data.get("Key") is not None:
        import capo_dynamodb.types.key

        out["key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("UpdateItemInput.key required")
    if data.get("AttributeUpdates") is not None:
        import capo_dynamodb.types.attribute_updates

        out["attribute_updates"] = (
            capo_dynamodb.types.attribute_updates.deserialize_aws_json_1_0(
                data["AttributeUpdates"]
            )
        )
    if data.get("Expected") is not None:
        import capo_dynamodb.types.expected_attribute_map

        out["expected"] = (
            capo_dynamodb.types.expected_attribute_map.deserialize_aws_json_1_0(
                data["Expected"]
            )
        )
    if data.get("ConditionalOperator") is not None:
        import capo_dynamodb.types.conditional_operator

        out["conditional_operator"] = (
            capo_dynamodb.types.conditional_operator.deserialize_aws_json_1_0(
                data["ConditionalOperator"]
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
    if data.get("UpdateExpression") is not None:
        out["update_expression"] = data["UpdateExpression"]
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
