"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicColumn``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.author_specified_aggregations
    import capo_quicksight.types.boolean
    import capo_quicksight.types.cell_value_synonyms
    import capo_quicksight.types.column_data_role
    import capo_quicksight.types.comparative_order
    import capo_quicksight.types.default_aggregation
    import capo_quicksight.types.default_formatting
    import capo_quicksight.types.description_sensitive_string
    import capo_quicksight.types.limited_sensitive_string
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.nullable_boolean
    import capo_quicksight.types.semantic_type
    import capo_quicksight.types.synonyms
    import capo_quicksight.types.topic_time_granularity


class TopicColumn(TypedDict, closed=True):
    column_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the column.</p>"""
    column_friendly_name: NotRequired[
        "capo_quicksight.types.limited_sensitive_string.LimitedSensitiveString"
    ]
    """<p>A user-friendly name for the column.</p>"""
    column_description: NotRequired[
        "capo_quicksight.types.description_sensitive_string.DescriptionSensitiveString"
    ]
    """<p>A description of the column and its contents.</p>"""
    column_synonyms: NotRequired["capo_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the column.</p>"""
    column_data_role: NotRequired[
        "capo_quicksight.types.column_data_role.ColumnDataRole"
    ]
    """<p>The role of the column in the data. Valid values are <code>DIMENSION</code> and <code>MEASURE</code>.</p>"""
    aggregation: NotRequired[
        "capo_quicksight.types.default_aggregation.DefaultAggregation"
    ]
    """<p>The type of aggregation that is performed on the column data when it's queried.</p>"""
    is_included_in_topic: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the column is included in the query results.</p>"""
    disable_indexing: NotRequired[
        "capo_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A Boolean value that indicates whether the column shows in the autocomplete functionality.</p>"""
    comparative_order: NotRequired[
        "capo_quicksight.types.comparative_order.ComparativeOrder"
    ]
    """<p>The order in which data is displayed for the column when it's used in a comparative context.</p>"""
    semantic_type: NotRequired["capo_quicksight.types.semantic_type.SemanticType"]
    """<p>The semantic type of data contained in the column.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    allowed_aggregations: NotRequired[
        "capo_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are allowed for the column. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    not_allowed_aggregations: NotRequired[
        "capo_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are not allowed for the column. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    default_formatting: NotRequired[
        "capo_quicksight.types.default_formatting.DefaultFormatting"
    ]
    """<p>The default formatting used for values in the column.</p>"""
    never_aggregate_in_filter: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to aggregate the column data when it's used in a filter context.</p>"""
    cell_value_synonyms: NotRequired[
        "capo_quicksight.types.cell_value_synonyms.CellValueSynonyms"
    ]
    """<p>The other names or aliases for the column cell value.</p>"""
    non_additive: NotRequired["capo_quicksight.types.nullable_boolean.NullableBoolean"]
    """<p>The non additive value for the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicColumn) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    if "column_friendly_name" in value:
        out["ColumnFriendlyName"] = value["column_friendly_name"]
    if "column_description" in value:
        out["ColumnDescription"] = value["column_description"]
    if "column_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["ColumnSynonyms"] = capo_quicksight.types.synonyms.serialize_json(
            value["column_synonyms"]
        )
    if "column_data_role" in value:
        import capo_quicksight.types.column_data_role

        out["ColumnDataRole"] = capo_quicksight.types.column_data_role.serialize_json(
            value["column_data_role"]
        )
    if "aggregation" in value:
        import capo_quicksight.types.default_aggregation

        out["Aggregation"] = capo_quicksight.types.default_aggregation.serialize_json(
            value["aggregation"]
        )
    out["IsIncludedInTopic"] = value.get("is_included_in_topic", False)
    if "disable_indexing" in value:
        out["DisableIndexing"] = value["disable_indexing"]
    if "comparative_order" in value:
        import capo_quicksight.types.comparative_order

        out["ComparativeOrder"] = (
            capo_quicksight.types.comparative_order.serialize_json(
                value["comparative_order"]
            )
        )
    if "semantic_type" in value:
        import capo_quicksight.types.semantic_type

        out["SemanticType"] = capo_quicksight.types.semantic_type.serialize_json(
            value["semantic_type"]
        )
    if "time_granularity" in value:
        import capo_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            capo_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "allowed_aggregations" in value:
        import capo_quicksight.types.author_specified_aggregations

        out["AllowedAggregations"] = (
            capo_quicksight.types.author_specified_aggregations.serialize_json(
                value["allowed_aggregations"]
            )
        )
    if "not_allowed_aggregations" in value:
        import capo_quicksight.types.author_specified_aggregations

        out["NotAllowedAggregations"] = (
            capo_quicksight.types.author_specified_aggregations.serialize_json(
                value["not_allowed_aggregations"]
            )
        )
    if "default_formatting" in value:
        import capo_quicksight.types.default_formatting

        out["DefaultFormatting"] = (
            capo_quicksight.types.default_formatting.serialize_json(
                value["default_formatting"]
            )
        )
    out["NeverAggregateInFilter"] = value.get("never_aggregate_in_filter", False)
    if "cell_value_synonyms" in value:
        import capo_quicksight.types.cell_value_synonyms

        out["CellValueSynonyms"] = (
            capo_quicksight.types.cell_value_synonyms.serialize_json(
                value["cell_value_synonyms"]
            )
        )
    if "non_additive" in value:
        out["NonAdditive"] = value["non_additive"]
    return out


def deserialize_json(data: dict) -> TopicColumn:
    out: TopicColumn = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("TopicColumn.column_name required")
    if data.get("ColumnFriendlyName") is not None:
        out["column_friendly_name"] = data["ColumnFriendlyName"]
    if data.get("ColumnDescription") is not None:
        out["column_description"] = data["ColumnDescription"]
    if data.get("ColumnSynonyms") is not None:
        import capo_quicksight.types.synonyms

        out["column_synonyms"] = capo_quicksight.types.synonyms.deserialize_json(
            data["ColumnSynonyms"]
        )
    if data.get("ColumnDataRole") is not None:
        import capo_quicksight.types.column_data_role

        out["column_data_role"] = (
            capo_quicksight.types.column_data_role.deserialize_json(
                data["ColumnDataRole"]
            )
        )
    if data.get("Aggregation") is not None:
        import capo_quicksight.types.default_aggregation

        out["aggregation"] = capo_quicksight.types.default_aggregation.deserialize_json(
            data["Aggregation"]
        )
    if data.get("IsIncludedInTopic") is not None:
        out["is_included_in_topic"] = data["IsIncludedInTopic"]
    else:
        out["is_included_in_topic"] = False
    if data.get("DisableIndexing") is not None:
        out["disable_indexing"] = data["DisableIndexing"]
    if data.get("ComparativeOrder") is not None:
        import capo_quicksight.types.comparative_order

        out["comparative_order"] = (
            capo_quicksight.types.comparative_order.deserialize_json(
                data["ComparativeOrder"]
            )
        )
    if data.get("SemanticType") is not None:
        import capo_quicksight.types.semantic_type

        out["semantic_type"] = capo_quicksight.types.semantic_type.deserialize_json(
            data["SemanticType"]
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("AllowedAggregations") is not None:
        import capo_quicksight.types.author_specified_aggregations

        out["allowed_aggregations"] = (
            capo_quicksight.types.author_specified_aggregations.deserialize_json(
                data["AllowedAggregations"]
            )
        )
    if data.get("NotAllowedAggregations") is not None:
        import capo_quicksight.types.author_specified_aggregations

        out["not_allowed_aggregations"] = (
            capo_quicksight.types.author_specified_aggregations.deserialize_json(
                data["NotAllowedAggregations"]
            )
        )
    if data.get("DefaultFormatting") is not None:
        import capo_quicksight.types.default_formatting

        out["default_formatting"] = (
            capo_quicksight.types.default_formatting.deserialize_json(
                data["DefaultFormatting"]
            )
        )
    if data.get("NeverAggregateInFilter") is not None:
        out["never_aggregate_in_filter"] = data["NeverAggregateInFilter"]
    else:
        out["never_aggregate_in_filter"] = False
    if data.get("CellValueSynonyms") is not None:
        import capo_quicksight.types.cell_value_synonyms

        out["cell_value_synonyms"] = (
            capo_quicksight.types.cell_value_synonyms.deserialize_json(
                data["CellValueSynonyms"]
            )
        )
    if data.get("NonAdditive") is not None:
        out["non_additive"] = data["NonAdditive"]
    return out


def redact_sensitive(value: TopicColumn) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "column_friendly_name" in value:
        out["column_friendly_name"] = "*** Sensitive Data Redacted ***"
    if "column_description" in value:
        out["column_description"] = "*** Sensitive Data Redacted ***"
    if "column_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["column_synonyms"] = capo_quicksight.types.synonyms.redact_sensitive(
            value["column_synonyms"]
        )
    if "semantic_type" in value:
        import capo_quicksight.types.semantic_type

        out["semantic_type"] = capo_quicksight.types.semantic_type.redact_sensitive(
            value["semantic_type"]
        )
    if "cell_value_synonyms" in value:
        import capo_quicksight.types.cell_value_synonyms

        out["cell_value_synonyms"] = (
            capo_quicksight.types.cell_value_synonyms.redact_sensitive(
                value["cell_value_synonyms"]
            )
        )
    return out
