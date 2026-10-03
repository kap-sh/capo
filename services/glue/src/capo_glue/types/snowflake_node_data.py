"""Generated from Smithy shape ``com.amazonaws.glue#SnowflakeNodeData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.boolean_value
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.generic_limited_string
    import capo_glue.types.generic_string
    import capo_glue.types.option
    import capo_glue.types.option_list


class SnowflakeNodeData(TypedDict, closed=True):
    source_type: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>Specifies how retrieved data is specified. Valid values: <code>"table"</code>, <code> "query"</code>.</p>"""
    connection: NotRequired["capo_glue.types.option.Option"]
    """<p>Specifies a Glue Data Catalog Connection to a Snowflake endpoint.</p>"""
    schema: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies a Snowflake database schema for your node to use.</p>"""
    table: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies a Snowflake table for your node to use.</p>"""
    database: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies a Snowflake database for your node to use.</p>"""
    temp_dir: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Not currently used.</p>"""
    iam_role: NotRequired["capo_glue.types.option.Option"]
    """<p>Not currently used.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional options passed to the Snowflake connector. If options are specified elsewhere in this node, this will take precedence.</p>"""
    sample_query: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A SQL string used to retrieve data with the <code>query</code> sourcetype.</p>"""
    pre_action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A SQL string run before the Snowflake connector performs its standard actions.</p>"""
    post_action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A SQL string run after the Snowflake connector performs its standard actions.</p>"""
    action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies what action to take when writing to a table with preexisting data. Valid values: <code> append</code>, <code>merge</code>, <code>truncate</code>, <code>drop</code>.</p>"""
    upsert: "capo_glue.types.boolean_value.BooleanValue"
    """<p>Used when Action is <code>append</code>. Specifies the resolution behavior when a row already exists. If true, preexisting rows will be updated. If false, those rows will be inserted.</p>"""
    merge_action: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>Specifies a merge action. Valid values: <code>simple</code>, <code>custom</code>. If simple, merge behavior is defined by <code>MergeWhenMatched</code> and <code> MergeWhenNotMatched</code>. If custom, defined by <code>MergeClause</code>.</p>"""
    merge_when_matched: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>Specifies how to resolve records that match preexisting data when merging. Valid values: <code> update</code>, <code>delete</code>.</p>"""
    merge_when_not_matched: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>Specifies how to process records that do not match preexisting data when merging. Valid values: <code>insert</code>, <code>none</code>.</p>"""
    merge_clause: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A SQL statement that specifies a custom merge behavior.</p>"""
    staging_table: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The name of a staging table used when performing <code>merge</code> or upsert <code>append</code> actions. Data is written to this table, then moved to <code>table</code> by a generated postaction.</p>"""
    selected_columns: NotRequired["capo_glue.types.option_list.OptionList"]
    """<p>Specifies the columns combined to identify a record when detecting matches for merges and upserts. A list of structures with <code>value</code>, <code>label</code> and <code> description</code> keys. Each structure describes a column.</p>"""
    auto_pushdown: "capo_glue.types.boolean_value.BooleanValue"
    """<p>Specifies whether automatic query pushdown is enabled. If pushdown is enabled, then when a query is run on Spark, if part of the query can be "pushed down" to the Snowflake server, it is pushed down. This improves performance of some queries.</p>"""
    table_schema: NotRequired["capo_glue.types.option_list.OptionList"]
    """<p>Manually defines the target schema for the node. A list of structures with <code>value</code> , <code>label</code> and <code>description</code> keys. Each structure defines a column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeNodeData) -> dict:
    out: dict = {}
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "connection" in value:
        import capo_glue.types.option

        out["Connection"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["connection"]
        )
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "table" in value:
        out["Table"] = value["table"]
    if "database" in value:
        out["Database"] = value["database"]
    if "temp_dir" in value:
        out["TempDir"] = value["temp_dir"]
    if "iam_role" in value:
        import capo_glue.types.option

        out["IamRole"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["iam_role"]
        )
    if "additional_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "sample_query" in value:
        out["SampleQuery"] = value["sample_query"]
    if "pre_action" in value:
        out["PreAction"] = value["pre_action"]
    if "post_action" in value:
        out["PostAction"] = value["post_action"]
    if "action" in value:
        out["Action"] = value["action"]
    out["Upsert"] = value.get("upsert", False)
    if "merge_action" in value:
        out["MergeAction"] = value["merge_action"]
    if "merge_when_matched" in value:
        out["MergeWhenMatched"] = value["merge_when_matched"]
    if "merge_when_not_matched" in value:
        out["MergeWhenNotMatched"] = value["merge_when_not_matched"]
    if "merge_clause" in value:
        out["MergeClause"] = value["merge_clause"]
    if "staging_table" in value:
        out["StagingTable"] = value["staging_table"]
    if "selected_columns" in value:
        import capo_glue.types.option_list

        out["SelectedColumns"] = capo_glue.types.option_list.serialize_aws_json_1_1(
            value["selected_columns"]
        )
    out["AutoPushdown"] = value.get("auto_pushdown", False)
    if "table_schema" in value:
        import capo_glue.types.option_list

        out["TableSchema"] = capo_glue.types.option_list.serialize_aws_json_1_1(
            value["table_schema"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeNodeData:
    out: SnowflakeNodeData = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    if data.get("Connection") is not None:
        import capo_glue.types.option

        out["connection"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["Connection"]
        )
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("Table") is not None:
        out["table"] = data["Table"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    if data.get("TempDir") is not None:
        out["temp_dir"] = data["TempDir"]
    if data.get("IamRole") is not None:
        import capo_glue.types.option

        out["iam_role"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["IamRole"]
        )
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.additional_options

        out["additional_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("SampleQuery") is not None:
        out["sample_query"] = data["SampleQuery"]
    if data.get("PreAction") is not None:
        out["pre_action"] = data["PreAction"]
    if data.get("PostAction") is not None:
        out["post_action"] = data["PostAction"]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    if data.get("Upsert") is not None:
        out["upsert"] = data["Upsert"]
    else:
        out["upsert"] = False
    if data.get("MergeAction") is not None:
        out["merge_action"] = data["MergeAction"]
    if data.get("MergeWhenMatched") is not None:
        out["merge_when_matched"] = data["MergeWhenMatched"]
    if data.get("MergeWhenNotMatched") is not None:
        out["merge_when_not_matched"] = data["MergeWhenNotMatched"]
    if data.get("MergeClause") is not None:
        out["merge_clause"] = data["MergeClause"]
    if data.get("StagingTable") is not None:
        out["staging_table"] = data["StagingTable"]
    if data.get("SelectedColumns") is not None:
        import capo_glue.types.option_list

        out["selected_columns"] = capo_glue.types.option_list.deserialize_aws_json_1_1(
            data["SelectedColumns"]
        )
    if data.get("AutoPushdown") is not None:
        out["auto_pushdown"] = data["AutoPushdown"]
    else:
        out["auto_pushdown"] = False
    if data.get("TableSchema") is not None:
        import capo_glue.types.option_list

        out["table_schema"] = capo_glue.types.option_list.deserialize_aws_json_1_1(
            data["TableSchema"]
        )
    return out
