"""Generated from Smithy shape ``com.amazonaws.dynamodb#QueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name_list
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.conditional_operator
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.filter_condition_map
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.key
    import capo_dynamodb.types.key_conditions
    import capo_dynamodb.types.key_expression
    import capo_dynamodb.types.positive_integer_object
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.select
    import capo_dynamodb.types.table_arn


class QueryInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table containing the requested items. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the <code>IndexName</code> parameter, you must also provide <code>TableName.</code> </p>"""
    select: NotRequired["capo_dynamodb.types.select.Select"]
    """<p>The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.</p> <ul> <li> <p> <code>ALL_ATTRIBUTES</code> - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.</p> </li> <li> <p> <code>ALL_PROJECTED_ATTRIBUTES</code> - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying <code>ALL_ATTRIBUTES</code>.</p> </li> <li> <p> <code>COUNT</code> - Returns the number of matching items, rather than the matching items themselves. Note that this uses the same quantity of read capacity units as getting the items, and is subject to the same item size calculations.</p> </li> <li> <p> <code>SPECIFIC_ATTRIBUTES</code> - Returns only the attributes listed in <code>ProjectionExpression</code>. This return value is equivalent to specifying <code>ProjectionExpression</code> without specifying any value for <code>Select</code>.</p> <p>If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency.</p> <p>If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.</p> </li> </ul> <p>If neither <code>Select</code> nor <code>ProjectionExpression</code> are specified, DynamoDB defaults to <code>ALL_ATTRIBUTES</code> when accessing a table, and <code>ALL_PROJECTED_ATTRIBUTES</code> when accessing an index. You cannot use both <code>Select</code> and <code>ProjectionExpression</code> together in a single request, unless the value for <code>Select</code> is <code>SPECIFIC_ATTRIBUTES</code>. (This usage is equivalent to specifying <code>ProjectionExpression</code> without any value for <code>Select</code>.)</p> <note> <p>If you use the <code>ProjectionExpression</code> parameter, then the value for <code>Select</code> can only be <code>SPECIFIC_ATTRIBUTES</code>. Any other value for <code>Select</code> will return an error.</p> </note>"""
    attributes_to_get: NotRequired[
        "capo_dynamodb.types.attribute_name_list.AttributeNameList"
    ]
    """<p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    limit: NotRequired[
        "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html">Query and Scan</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    consistent_read: NotRequired["capo_dynamodb.types.consistent_read.ConsistentRead"]
    """<p>Determines the read consistency model: If set to <code>true</code>, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.</p> <p>Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with <code>ConsistentRead</code> set to <code>true</code>, you will receive a <code>ValidationException</code>.</p>"""
    key_conditions: NotRequired["capo_dynamodb.types.key_conditions.KeyConditions"]
    """<p>This is a legacy parameter. Use <code>KeyConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html">KeyConditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    query_filter: NotRequired[
        "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
    ]
    """<p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html">QueryFilter</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    conditional_operator: NotRequired[
        "capo_dynamodb.types.conditional_operator.ConditionalOperator"
    ]
    """<p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    scan_index_forward: NotRequired["capo_dynamodb.types.boolean_object.BooleanObject"]
    """<p>Specifies the order for index traversal: If <code>true</code> (default), the traversal is performed in ascending order; if <code>false</code>, the traversal is performed in descending order. </p> <p>Items with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned.</p> <p>If <code>ScanIndexForward</code> is <code>true</code>, DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If <code>ScanIndexForward</code> is <code>false</code>, DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.</p>"""
    exclusive_start_key: NotRequired["capo_dynamodb.types.key.Key"]
    """<p>The primary key of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedKey</code> in the previous operation.</p> <p>The data type for <code>ExclusiveStartKey</code> must be String, Number, or Binary. No set data types are allowed.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    filter_expression: NotRequired[
        "capo_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A string that contains conditions that DynamoDB applies after the <code>Query</code> operation, but before the data is returned to you. Items that do not satisfy the <code>FilterExpression</code> criteria are not returned.</p> <p>A <code>FilterExpression</code> does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.</p> <note> <p>A <code>FilterExpression</code> is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html">Filter Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    key_condition_expression: NotRequired[
        "capo_dynamodb.types.key_expression.KeyExpression"
    ]
    """<p>The condition that specifies the key values for items to be retrieved by the <code>Query</code> action.</p> <p>The condition must perform an equality test on a single partition key value.</p> <p>The condition can optionally perform one of several comparison tests on a single sort key value. This allows <code>Query</code> to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.</p> <p>The partition key equality test is required, and must be specified in the following format:</p> <p> <code>partitionKeyName</code> <i>=</i> <code>:partitionkeyval</code> </p> <p>If you also want to provide a condition for the sort key, it must be combined using <code>AND</code> with the condition for the sort key. Following is an example, using the <b>=</b> comparison operator for the sort key:</p> <p> <code>partitionKeyName</code> <code>=</code> <code>:partitionkeyval</code> <code>AND</code> <code>sortKeyName</code> <code>=</code> <code>:sortkeyval</code> </p> <p>Valid comparisons for the sort key condition are as follows:</p> <ul> <li> <p> <code>sortKeyName</code> <code>=</code> <code>:sortkeyval</code> - true if the sort key value is equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code><</code> <code>:sortkeyval</code> - true if the sort key value is less than <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code><=</code> <code>:sortkeyval</code> - true if the sort key value is less than or equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>></code> <code>:sortkeyval</code> - true if the sort key value is greater than <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>>= </code> <code>:sortkeyval</code> - true if the sort key value is greater than or equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>BETWEEN</code> <code>:sortkeyval1</code> <code>AND</code> <code>:sortkeyval2</code> - true if the sort key value is greater than or equal to <code>:sortkeyval1</code>, and less than or equal to <code>:sortkeyval2</code>.</p> </li> <li> <p> <code>begins_with (</code> <code>sortKeyName</code>, <code>:sortkeyval</code> <code>)</code> - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name <code>begins_with</code> is case-sensitive.</p> </li> </ul> <p>Use the <code>ExpressionAttributeValues</code> parameter to replace tokens such as <code>:partitionval</code> and <code>:sortval</code> with actual values at runtime.</p> <p>You can optionally use the <code>ExpressionAttributeNames</code> parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following <code>KeyConditionExpression</code> parameter causes an error because <i>Size</i> is a reserved word:</p> <ul> <li> <p> <code>Size = :myval</code> </p> </li> </ul> <p>To work around this, define a placeholder (such a <code>#S</code>) to represent the attribute name <i>Size</i>. <code>KeyConditionExpression</code> then is as follows:</p> <ul> <li> <p> <code>#S = :myval</code> </p> </li> </ul> <p>For a list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>For more information on <code>ExpressionAttributeNames</code> and <code>ExpressionAttributeValues</code>, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html">Using Placeholders for Attribute Names and Values</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <i>ProductStatus</i> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Specifying Conditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "select" in value:
        import capo_dynamodb.types.select

        out["Select"] = capo_dynamodb.types.select.serialize_aws_json_1_0(
            value["select"]
        )
    if "attributes_to_get" in value:
        import capo_dynamodb.types.attribute_name_list

        out["AttributesToGet"] = (
            capo_dynamodb.types.attribute_name_list.serialize_aws_json_1_0(
                value["attributes_to_get"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
    if "key_conditions" in value:
        import capo_dynamodb.types.key_conditions

        out["KeyConditions"] = (
            capo_dynamodb.types.key_conditions.serialize_aws_json_1_0(
                value["key_conditions"]
            )
        )
    if "query_filter" in value:
        import capo_dynamodb.types.filter_condition_map

        out["QueryFilter"] = (
            capo_dynamodb.types.filter_condition_map.serialize_aws_json_1_0(
                value["query_filter"]
            )
        )
    if "conditional_operator" in value:
        import capo_dynamodb.types.conditional_operator

        out["ConditionalOperator"] = (
            capo_dynamodb.types.conditional_operator.serialize_aws_json_1_0(
                value["conditional_operator"]
            )
        )
    if "scan_index_forward" in value:
        out["ScanIndexForward"] = value["scan_index_forward"]
    if "exclusive_start_key" in value:
        import capo_dynamodb.types.key

        out["ExclusiveStartKey"] = capo_dynamodb.types.key.serialize_aws_json_1_0(
            value["exclusive_start_key"]
        )
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "key_condition_expression" in value:
        out["KeyConditionExpression"] = value["key_condition_expression"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryInput:
    out: QueryInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("QueryInput.table_name required")
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("Select") is not None:
        import capo_dynamodb.types.select

        out["select"] = capo_dynamodb.types.select.deserialize_aws_json_1_0(
            data["Select"]
        )
    if data.get("AttributesToGet") is not None:
        import capo_dynamodb.types.attribute_name_list

        out["attributes_to_get"] = (
            capo_dynamodb.types.attribute_name_list.deserialize_aws_json_1_0(
                data["AttributesToGet"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("ConsistentRead") is not None:
        out["consistent_read"] = data["ConsistentRead"]
    if data.get("KeyConditions") is not None:
        import capo_dynamodb.types.key_conditions

        out["key_conditions"] = (
            capo_dynamodb.types.key_conditions.deserialize_aws_json_1_0(
                data["KeyConditions"]
            )
        )
    if data.get("QueryFilter") is not None:
        import capo_dynamodb.types.filter_condition_map

        out["query_filter"] = (
            capo_dynamodb.types.filter_condition_map.deserialize_aws_json_1_0(
                data["QueryFilter"]
            )
        )
    if data.get("ConditionalOperator") is not None:
        import capo_dynamodb.types.conditional_operator

        out["conditional_operator"] = (
            capo_dynamodb.types.conditional_operator.deserialize_aws_json_1_0(
                data["ConditionalOperator"]
            )
        )
    if data.get("ScanIndexForward") is not None:
        out["scan_index_forward"] = data["ScanIndexForward"]
    if data.get("ExclusiveStartKey") is not None:
        import capo_dynamodb.types.key

        out["exclusive_start_key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(
            data["ExclusiveStartKey"]
        )
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    if data.get("ProjectionExpression") is not None:
        out["projection_expression"] = data["ProjectionExpression"]
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    if data.get("KeyConditionExpression") is not None:
        out["key_condition_expression"] = data["KeyConditionExpression"]
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
    return out
