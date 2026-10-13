"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCalculatedField``."""

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
    import capo_quicksight.types.expression
    import capo_quicksight.types.limited_sensitive_string
    import capo_quicksight.types.nullable_boolean
    import capo_quicksight.types.semantic_type
    import capo_quicksight.types.synonyms
    import capo_quicksight.types.topic_time_granularity


class TopicCalculatedField(TypedDict, closed=True):
    calculated_field_name: (
        "capo_quicksight.types.limited_sensitive_string.LimitedSensitiveString"
    )
    """<p>The calculated field name.</p>"""
    calculated_field_description: NotRequired[
        "capo_quicksight.types.description_sensitive_string.DescriptionSensitiveString"
    ]
    """<p>The calculated field description.</p>"""
    expression: "capo_quicksight.types.expression.Expression"
    """<p>The calculated field expression.</p>"""
    calculated_field_synonyms: NotRequired["capo_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the calculated field.</p>"""
    is_included_in_topic: "capo_quicksight.types.boolean.Boolean"
    """<p>A boolean value that indicates if a calculated field is included in the topic.</p>"""
    disable_indexing: NotRequired[
        "capo_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A Boolean value that indicates if a calculated field is visible in the autocomplete.</p>"""
    column_data_role: NotRequired[
        "capo_quicksight.types.column_data_role.ColumnDataRole"
    ]
    """<p>The column data role for a calculated field. Valid values for this structure are <code>DIMENSION</code> and <code>MEASURE</code>.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    default_formatting: NotRequired[
        "capo_quicksight.types.default_formatting.DefaultFormatting"
    ]
    """<p>The default formatting definition.</p>"""
    aggregation: NotRequired[
        "capo_quicksight.types.default_aggregation.DefaultAggregation"
    ]
    """<p>The default aggregation. Valid values for this structure are <code>SUM</code>, <code>MAX</code>, <code>MIN</code>, <code>COUNT</code>, <code>DISTINCT_COUNT</code>, and <code>AVERAGE</code>.</p>"""
    comparative_order: NotRequired[
        "capo_quicksight.types.comparative_order.ComparativeOrder"
    ]
    """<p>The order in which data is displayed for the calculated field when it's used in a comparative context.</p>"""
    semantic_type: NotRequired["capo_quicksight.types.semantic_type.SemanticType"]
    """<p>The semantic type.</p>"""
    allowed_aggregations: NotRequired[
        "capo_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are allowed for the calculated field. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    not_allowed_aggregations: NotRequired[
        "capo_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are not allowed for the calculated field. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    never_aggregate_in_filter: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to never aggregate calculated field in filters.</p>"""
    cell_value_synonyms: NotRequired[
        "capo_quicksight.types.cell_value_synonyms.CellValueSynonyms"
    ]
    """<p>The other names or aliases for the calculated field cell value.</p>"""
    non_additive: NotRequired["capo_quicksight.types.nullable_boolean.NullableBoolean"]
    """<p>The non additive for the table style target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicCalculatedField) -> dict:
    out: dict = {}
    out["CalculatedFieldName"] = value["calculated_field_name"]
    if "calculated_field_description" in value:
        out["CalculatedFieldDescription"] = value["calculated_field_description"]
    out["Expression"] = value["expression"]
    if "calculated_field_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["CalculatedFieldSynonyms"] = capo_quicksight.types.synonyms.serialize_json(
            value["calculated_field_synonyms"]
        )
    out["IsIncludedInTopic"] = value.get("is_included_in_topic", False)
    if "disable_indexing" in value:
        out["DisableIndexing"] = value["disable_indexing"]
    if "column_data_role" in value:
        import capo_quicksight.types.column_data_role

        out["ColumnDataRole"] = capo_quicksight.types.column_data_role.serialize_json(
            value["column_data_role"]
        )
    if "time_granularity" in value:
        import capo_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            capo_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "default_formatting" in value:
        import capo_quicksight.types.default_formatting

        out["DefaultFormatting"] = (
            capo_quicksight.types.default_formatting.serialize_json(
                value["default_formatting"]
            )
        )
    if "aggregation" in value:
        import capo_quicksight.types.default_aggregation

        out["Aggregation"] = capo_quicksight.types.default_aggregation.serialize_json(
            value["aggregation"]
        )
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


def deserialize_json(data: dict) -> TopicCalculatedField:
    out: TopicCalculatedField = {}  # type: ignore[typeddict-item]
    if data.get("CalculatedFieldName") is not None:
        out["calculated_field_name"] = data["CalculatedFieldName"]
    else:
        raise DeserializationError(
            "TopicCalculatedField.calculated_field_name required"
        )
    if data.get("CalculatedFieldDescription") is not None:
        out["calculated_field_description"] = data["CalculatedFieldDescription"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("TopicCalculatedField.expression required")
    if data.get("CalculatedFieldSynonyms") is not None:
        import capo_quicksight.types.synonyms

        out["calculated_field_synonyms"] = (
            capo_quicksight.types.synonyms.deserialize_json(
                data["CalculatedFieldSynonyms"]
            )
        )
    if data.get("IsIncludedInTopic") is not None:
        out["is_included_in_topic"] = data["IsIncludedInTopic"]
    else:
        out["is_included_in_topic"] = False
    if data.get("DisableIndexing") is not None:
        out["disable_indexing"] = data["DisableIndexing"]
    if data.get("ColumnDataRole") is not None:
        import capo_quicksight.types.column_data_role

        out["column_data_role"] = (
            capo_quicksight.types.column_data_role.deserialize_json(
                data["ColumnDataRole"]
            )
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("DefaultFormatting") is not None:
        import capo_quicksight.types.default_formatting

        out["default_formatting"] = (
            capo_quicksight.types.default_formatting.deserialize_json(
                data["DefaultFormatting"]
            )
        )
    if data.get("Aggregation") is not None:
        import capo_quicksight.types.default_aggregation

        out["aggregation"] = capo_quicksight.types.default_aggregation.deserialize_json(
            data["Aggregation"]
        )
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


def redact_sensitive(value: TopicCalculatedField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "calculated_field_name" in value:
        out["calculated_field_name"] = "*** Sensitive Data Redacted ***"
    if "calculated_field_description" in value:
        out["calculated_field_description"] = "*** Sensitive Data Redacted ***"
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    if "calculated_field_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["calculated_field_synonyms"] = (
            capo_quicksight.types.synonyms.redact_sensitive(
                value["calculated_field_synonyms"]
            )
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
