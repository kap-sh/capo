"""Generated from Smithy shape ``com.amazonaws.glue#JDBCConnectorOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_non_negative_long
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.jdbc_data_type_mapping


class JDBCConnectorOptions(TypedDict, closed=True):
    filter_predicate: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Extra condition clause to filter data from source. For example:</p> <p> <code>BillingCity='Mountain View'</code> </p> <p>When using a query instead of a table name, you should validate that the query works with the specified <code>filterPredicate</code>.</p>"""
    partition_column: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The name of an integer column that is used for partitioning. This option works only when it's included with <code>lowerBound</code>, <code>upperBound</code>, and <code>numPartitions</code>. This option works the same way as in the Spark SQL JDBC reader.</p>"""
    lower_bound: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The minimum value of <code>partitionColumn</code> that is used to decide partition stride.</p>"""
    upper_bound: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The maximum value of <code>partitionColumn</code> that is used to decide partition stride.</p>"""
    num_partitions: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The number of partitions. This value, along with <code>lowerBound</code> (inclusive) and <code>upperBound</code> (exclusive), form partition strides for generated <code>WHERE</code> clause expressions that are used to split the <code>partitionColumn</code>.</p>"""
    job_bookmark_keys: NotRequired[
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>The name of the job bookmark keys on which to sort.</p>"""
    job_bookmark_keys_sort_order: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies an ascending or descending sort order.</p>"""
    data_type_mapping: NotRequired[
        "capo_glue.types.jdbc_data_type_mapping.JDBCDataTypeMapping"
    ]
    """<p>Custom data type mapping that builds a mapping from a JDBC data type to an Glue data type. For example, the option <code>"dataTypeMapping":{"FLOAT":"STRING"}</code> maps data fields of JDBC type <code>FLOAT</code> into the Java <code>String</code> type by calling the <code>ResultSet.getString()</code> method of the driver, and uses it to build the Glue record. The <code>ResultSet</code> object is implemented by each driver, so the behavior is specific to the driver you use. Refer to the documentation for your JDBC driver to understand how the driver performs the conversions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JDBCConnectorOptions) -> dict:
    out: dict = {}
    if "filter_predicate" in value:
        out["FilterPredicate"] = value["filter_predicate"]
    if "partition_column" in value:
        out["PartitionColumn"] = value["partition_column"]
    if "lower_bound" in value:
        out["LowerBound"] = value["lower_bound"]
    if "upper_bound" in value:
        out["UpperBound"] = value["upper_bound"]
    if "num_partitions" in value:
        out["NumPartitions"] = value["num_partitions"]
    if "job_bookmark_keys" in value:
        import capo_glue.types.enclosed_in_string_properties

        out["JobBookmarkKeys"] = (
            capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["job_bookmark_keys"]
            )
        )
    if "job_bookmark_keys_sort_order" in value:
        out["JobBookmarkKeysSortOrder"] = value["job_bookmark_keys_sort_order"]
    if "data_type_mapping" in value:
        import capo_glue.types.jdbc_data_type_mapping

        out["DataTypeMapping"] = (
            capo_glue.types.jdbc_data_type_mapping.serialize_aws_json_1_1(
                value["data_type_mapping"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JDBCConnectorOptions:
    out: JDBCConnectorOptions = {}  # type: ignore[typeddict-item]
    if data.get("FilterPredicate") is not None:
        out["filter_predicate"] = data["FilterPredicate"]
    if data.get("PartitionColumn") is not None:
        out["partition_column"] = data["PartitionColumn"]
    if data.get("LowerBound") is not None:
        out["lower_bound"] = data["LowerBound"]
    if data.get("UpperBound") is not None:
        out["upper_bound"] = data["UpperBound"]
    if data.get("NumPartitions") is not None:
        out["num_partitions"] = data["NumPartitions"]
    if data.get("JobBookmarkKeys") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["job_bookmark_keys"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["JobBookmarkKeys"]
            )
        )
    if data.get("JobBookmarkKeysSortOrder") is not None:
        out["job_bookmark_keys_sort_order"] = data["JobBookmarkKeysSortOrder"]
    if data.get("DataTypeMapping") is not None:
        import capo_glue.types.jdbc_data_type_mapping

        out["data_type_mapping"] = (
            capo_glue.types.jdbc_data_type_mapping.deserialize_aws_json_1_1(
                data["DataTypeMapping"]
            )
        )
    return out
