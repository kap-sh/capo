"""Generated from Smithy shape ``com.amazonaws.dynamodb#ScanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name_list
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.conditional_operator
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.filter_condition_map
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.key
    import capo_dynamodb.types.positive_integer_object
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.scan_segment
    import capo_dynamodb.types.scan_total_segments
    import capo_dynamodb.types.select
    import capo_dynamodb.types.table_arn


class ScanInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table containing the requested items or if you provide <code>IndexName</code>, the name of the table to which that index belongs.</p> <p>You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The name of a secondary index to scan. This index can be any local secondary index or global secondary index. Note that if you use the <code>IndexName</code> parameter, you must also provide <code>TableName</code>.</p>"""
    attributes_to_get: NotRequired[
        "capo_dynamodb.types.attribute_name_list.AttributeNameList"
    ]
    """<p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    limit: NotRequired[
        "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html">Working with Queries</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    select: NotRequired["capo_dynamodb.types.select.Select"]
    """<p>The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.</p> <ul> <li> <p> <code>ALL_ATTRIBUTES</code> - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.</p> </li> <li> <p> <code>ALL_PROJECTED_ATTRIBUTES</code> - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying <code>ALL_ATTRIBUTES</code>.</p> </li> <li> <p> <code>COUNT</code> - Returns the number of matching items, rather than the matching items themselves. Note that this uses the same quantity of read capacity units as getting the items, and is subject to the same item size calculations.</p> </li> <li> <p> <code>SPECIFIC_ATTRIBUTES</code> - Returns only the attributes listed in <code>ProjectionExpression</code>. This return value is equivalent to specifying <code>ProjectionExpression</code> without specifying any value for <code>Select</code>.</p> <p>If you query or scan a local secondary index and request only attributes that are projected into that index, the operation reads only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency.</p> <p>If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.</p> </li> </ul> <p>If neither <code>Select</code> nor <code>ProjectionExpression</code> are specified, DynamoDB defaults to <code>ALL_ATTRIBUTES</code> when accessing a table, and <code>ALL_PROJECTED_ATTRIBUTES</code> when accessing an index. You cannot use both <code>Select</code> and <code>ProjectionExpression</code> together in a single request, unless the value for <code>Select</code> is <code>SPECIFIC_ATTRIBUTES</code>. (This usage is equivalent to specifying <code>ProjectionExpression</code> without any value for <code>Select</code>.)</p> <note> <p>If you use the <code>ProjectionExpression</code> parameter, then the value for <code>Select</code> can only be <code>SPECIFIC_ATTRIBUTES</code>. Any other value for <code>Select</code> will return an error.</p> </note>"""
    scan_filter: NotRequired[
        "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
    ]
    """<p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html">ScanFilter</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    conditional_operator: NotRequired[
        "capo_dynamodb.types.conditional_operator.ConditionalOperator"
    ]
    """<p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    exclusive_start_key: NotRequired["capo_dynamodb.types.key.Key"]
    """<p>The primary key of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedKey</code> in the previous operation.</p> <p>The data type for <code>ExclusiveStartKey</code> must be String, Number or Binary. No set data types are allowed.</p> <p>In a parallel scan, a <code>Scan</code> request that includes <code>ExclusiveStartKey</code> must specify the same segment whose previous <code>Scan</code> returned the corresponding value of <code>LastEvaluatedKey</code>.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    total_segments: NotRequired[
        "capo_dynamodb.types.scan_total_segments.ScanTotalSegments"
    ]
    """<p>For a parallel <code>Scan</code> request, <code>TotalSegments</code> represents the total number of segments into which the <code>Scan</code> operation will be divided. The value of <code>TotalSegments</code> corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a <code>TotalSegments</code> value of 4.</p> <p>The value for <code>TotalSegments</code> must be greater than or equal to 1, and less than or equal to 1000000. If you specify a <code>TotalSegments</code> value of 1, the <code>Scan</code> operation will be sequential rather than parallel.</p> <p>If you specify <code>TotalSegments</code>, you must also specify <code>Segment</code>.</p>"""
    segment: NotRequired["capo_dynamodb.types.scan_segment.ScanSegment"]
    """<p>For a parallel <code>Scan</code> request, <code>Segment</code> identifies an individual segment to be scanned by an application worker.</p> <p>Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a <code>Segment</code> value of 0, the second thread specifies 1, and so on.</p> <p>The value of <code>LastEvaluatedKey</code> returned from a parallel <code>Scan</code> request must be used as <code>ExclusiveStartKey</code> with the same segment ID in a subsequent <code>Scan</code> operation.</p> <p>The value for <code>Segment</code> must be greater than or equal to 0, and less than the value provided for <code>TotalSegments</code>.</p> <p>If you provide <code>Segment</code>, you must also provide <code>TotalSegments</code>.</p>"""
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    filter_expression: NotRequired[
        "capo_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A string that contains conditions that DynamoDB applies after the <code>Scan</code> operation, but before the data is returned to you. Items that do not satisfy the <code>FilterExpression</code> criteria are not returned.</p> <note> <p>A <code>FilterExpression</code> is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.FilterExpression">Filter Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <code>ProductStatus</code> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    consistent_read: NotRequired["capo_dynamodb.types.consistent_read.ConsistentRead"]
    """<p>A Boolean value that determines the read consistency model during the scan:</p> <ul> <li> <p>If <code>ConsistentRead</code> is <code>false</code>, then the data returned from <code>Scan</code> might not contain the results from other recently completed write operations (<code>PutItem</code>, <code>UpdateItem</code>, or <code>DeleteItem</code>).</p> </li> <li> <p>If <code>ConsistentRead</code> is <code>true</code>, then all of the write operations that completed before the <code>Scan</code> began are guaranteed to be contained in the <code>Scan</code> response.</p> </li> </ul> <p>The default setting for <code>ConsistentRead</code> is <code>false</code>.</p> <p>The <code>ConsistentRead</code> parameter is not supported on global secondary indexes. If you scan a global secondary index with <code>ConsistentRead</code> set to true, you will receive a <code>ValidationException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScanInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "attributes_to_get" in value:
        import capo_dynamodb.types.attribute_name_list

        out["AttributesToGet"] = (
            capo_dynamodb.types.attribute_name_list.serialize_aws_json_1_0(
                value["attributes_to_get"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "select" in value:
        import capo_dynamodb.types.select

        out["Select"] = capo_dynamodb.types.select.serialize_aws_json_1_0(
            value["select"]
        )
    if "scan_filter" in value:
        import capo_dynamodb.types.filter_condition_map

        out["ScanFilter"] = (
            capo_dynamodb.types.filter_condition_map.serialize_aws_json_1_0(
                value["scan_filter"]
            )
        )
    if "conditional_operator" in value:
        import capo_dynamodb.types.conditional_operator

        out["ConditionalOperator"] = (
            capo_dynamodb.types.conditional_operator.serialize_aws_json_1_0(
                value["conditional_operator"]
            )
        )
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
    if "total_segments" in value:
        out["TotalSegments"] = value["total_segments"]
    if "segment" in value:
        out["Segment"] = value["segment"]
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
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
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScanInput:
    out: ScanInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("ScanInput.table_name required")
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("AttributesToGet") is not None:
        import capo_dynamodb.types.attribute_name_list

        out["attributes_to_get"] = (
            capo_dynamodb.types.attribute_name_list.deserialize_aws_json_1_0(
                data["AttributesToGet"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("Select") is not None:
        import capo_dynamodb.types.select

        out["select"] = capo_dynamodb.types.select.deserialize_aws_json_1_0(
            data["Select"]
        )
    if data.get("ScanFilter") is not None:
        import capo_dynamodb.types.filter_condition_map

        out["scan_filter"] = (
            capo_dynamodb.types.filter_condition_map.deserialize_aws_json_1_0(
                data["ScanFilter"]
            )
        )
    if data.get("ConditionalOperator") is not None:
        import capo_dynamodb.types.conditional_operator

        out["conditional_operator"] = (
            capo_dynamodb.types.conditional_operator.deserialize_aws_json_1_0(
                data["ConditionalOperator"]
            )
        )
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
    if data.get("TotalSegments") is not None:
        out["total_segments"] = data["TotalSegments"]
    if data.get("Segment") is not None:
        out["segment"] = data["Segment"]
    if data.get("ProjectionExpression") is not None:
        out["projection_expression"] = data["ProjectionExpression"]
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
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
    if data.get("ConsistentRead") is not None:
        out["consistent_read"] = data["ConsistentRead"]
    return out
