"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.description_sensitive_string
    import capo_quicksight.types.filter_class
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.named_filter_type
    import capo_quicksight.types.synonyms
    import capo_quicksight.types.topic_category_filter
    import capo_quicksight.types.topic_date_range_filter
    import capo_quicksight.types.topic_null_filter
    import capo_quicksight.types.topic_numeric_equality_filter
    import capo_quicksight.types.topic_numeric_range_filter
    import capo_quicksight.types.topic_relative_date_filter


class TopicFilter(TypedDict, closed=True):
    filter_description: NotRequired[
        "capo_quicksight.types.description_sensitive_string.DescriptionSensitiveString"
    ]
    """<p>A description of the filter used to select items for a topic.</p>"""
    filter_class: NotRequired["capo_quicksight.types.filter_class.FilterClass"]
    """<p>The class of the filter. Valid values for this structure are <code>ENFORCED_VALUE_FILTER</code>, <code>CONDITIONAL_VALUE_FILTER</code>, and <code>NAMED_VALUE_FILTER</code>.</p>"""
    filter_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the filter.</p>"""
    filter_synonyms: NotRequired["capo_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the filter.</p>"""
    operand_field_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the field that the filter operates on.</p>"""
    filter_type: NotRequired["capo_quicksight.types.named_filter_type.NamedFilterType"]
    """<p>The type of the filter. Valid values for this structure are <code>CATEGORY_FILTER</code>, <code>NUMERIC_EQUALITY_FILTER</code>, <code>NUMERIC_RANGE_FILTER</code>, <code>DATE_RANGE_FILTER</code>, and <code>RELATIVE_DATE_FILTER</code>.</p>"""
    category_filter: NotRequired[
        "capo_quicksight.types.topic_category_filter.TopicCategoryFilter"
    ]
    """<p>The category filter that is associated with this filter.</p>"""
    numeric_equality_filter: NotRequired[
        "capo_quicksight.types.topic_numeric_equality_filter.TopicNumericEqualityFilter"
    ]
    """<p>The numeric equality filter.</p>"""
    numeric_range_filter: NotRequired[
        "capo_quicksight.types.topic_numeric_range_filter.TopicNumericRangeFilter"
    ]
    """<p>The numeric range filter.</p>"""
    date_range_filter: NotRequired[
        "capo_quicksight.types.topic_date_range_filter.TopicDateRangeFilter"
    ]
    """<p>The date range filter.</p>"""
    relative_date_filter: NotRequired[
        "capo_quicksight.types.topic_relative_date_filter.TopicRelativeDateFilter"
    ]
    """<p>The relative date filter.</p>"""
    null_filter: NotRequired["capo_quicksight.types.topic_null_filter.TopicNullFilter"]
    """<p>The null filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilter) -> dict:
    out: dict = {}
    if "filter_description" in value:
        out["FilterDescription"] = value["filter_description"]
    if "filter_class" in value:
        import capo_quicksight.types.filter_class

        out["FilterClass"] = capo_quicksight.types.filter_class.serialize_json(
            value["filter_class"]
        )
    out["FilterName"] = value["filter_name"]
    if "filter_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["FilterSynonyms"] = capo_quicksight.types.synonyms.serialize_json(
            value["filter_synonyms"]
        )
    out["OperandFieldName"] = value["operand_field_name"]
    if "filter_type" in value:
        import capo_quicksight.types.named_filter_type

        out["FilterType"] = capo_quicksight.types.named_filter_type.serialize_json(
            value["filter_type"]
        )
    if "category_filter" in value:
        import capo_quicksight.types.topic_category_filter

        out["CategoryFilter"] = (
            capo_quicksight.types.topic_category_filter.serialize_json(
                value["category_filter"]
            )
        )
    if "numeric_equality_filter" in value:
        import capo_quicksight.types.topic_numeric_equality_filter

        out["NumericEqualityFilter"] = (
            capo_quicksight.types.topic_numeric_equality_filter.serialize_json(
                value["numeric_equality_filter"]
            )
        )
    if "numeric_range_filter" in value:
        import capo_quicksight.types.topic_numeric_range_filter

        out["NumericRangeFilter"] = (
            capo_quicksight.types.topic_numeric_range_filter.serialize_json(
                value["numeric_range_filter"]
            )
        )
    if "date_range_filter" in value:
        import capo_quicksight.types.topic_date_range_filter

        out["DateRangeFilter"] = (
            capo_quicksight.types.topic_date_range_filter.serialize_json(
                value["date_range_filter"]
            )
        )
    if "relative_date_filter" in value:
        import capo_quicksight.types.topic_relative_date_filter

        out["RelativeDateFilter"] = (
            capo_quicksight.types.topic_relative_date_filter.serialize_json(
                value["relative_date_filter"]
            )
        )
    if "null_filter" in value:
        import capo_quicksight.types.topic_null_filter

        out["NullFilter"] = capo_quicksight.types.topic_null_filter.serialize_json(
            value["null_filter"]
        )
    return out


def deserialize_json(data: dict) -> TopicFilter:
    out: TopicFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterDescription") is not None:
        out["filter_description"] = data["FilterDescription"]
    if data.get("FilterClass") is not None:
        import capo_quicksight.types.filter_class

        out["filter_class"] = capo_quicksight.types.filter_class.deserialize_json(
            data["FilterClass"]
        )
    if data.get("FilterName") is not None:
        out["filter_name"] = data["FilterName"]
    else:
        out["filter_name"] = ""
    if data.get("FilterSynonyms") is not None:
        import capo_quicksight.types.synonyms

        out["filter_synonyms"] = capo_quicksight.types.synonyms.deserialize_json(
            data["FilterSynonyms"]
        )
    if data.get("OperandFieldName") is not None:
        out["operand_field_name"] = data["OperandFieldName"]
    else:
        out["operand_field_name"] = ""
    if data.get("FilterType") is not None:
        import capo_quicksight.types.named_filter_type

        out["filter_type"] = capo_quicksight.types.named_filter_type.deserialize_json(
            data["FilterType"]
        )
    if data.get("CategoryFilter") is not None:
        import capo_quicksight.types.topic_category_filter

        out["category_filter"] = (
            capo_quicksight.types.topic_category_filter.deserialize_json(
                data["CategoryFilter"]
            )
        )
    if data.get("NumericEqualityFilter") is not None:
        import capo_quicksight.types.topic_numeric_equality_filter

        out["numeric_equality_filter"] = (
            capo_quicksight.types.topic_numeric_equality_filter.deserialize_json(
                data["NumericEqualityFilter"]
            )
        )
    if data.get("NumericRangeFilter") is not None:
        import capo_quicksight.types.topic_numeric_range_filter

        out["numeric_range_filter"] = (
            capo_quicksight.types.topic_numeric_range_filter.deserialize_json(
                data["NumericRangeFilter"]
            )
        )
    if data.get("DateRangeFilter") is not None:
        import capo_quicksight.types.topic_date_range_filter

        out["date_range_filter"] = (
            capo_quicksight.types.topic_date_range_filter.deserialize_json(
                data["DateRangeFilter"]
            )
        )
    if data.get("RelativeDateFilter") is not None:
        import capo_quicksight.types.topic_relative_date_filter

        out["relative_date_filter"] = (
            capo_quicksight.types.topic_relative_date_filter.deserialize_json(
                data["RelativeDateFilter"]
            )
        )
    if data.get("NullFilter") is not None:
        import capo_quicksight.types.topic_null_filter

        out["null_filter"] = capo_quicksight.types.topic_null_filter.deserialize_json(
            data["NullFilter"]
        )
    return out


def redact_sensitive(value: TopicFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_description" in value:
        out["filter_description"] = "*** Sensitive Data Redacted ***"
    if "filter_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["filter_synonyms"] = capo_quicksight.types.synonyms.redact_sensitive(
            value["filter_synonyms"]
        )
    if "category_filter" in value:
        import capo_quicksight.types.topic_category_filter

        out["category_filter"] = (
            capo_quicksight.types.topic_category_filter.redact_sensitive(
                value["category_filter"]
            )
        )
    if "numeric_equality_filter" in value:
        import capo_quicksight.types.topic_numeric_equality_filter

        out["numeric_equality_filter"] = (
            capo_quicksight.types.topic_numeric_equality_filter.redact_sensitive(
                value["numeric_equality_filter"]
            )
        )
    if "numeric_range_filter" in value:
        import capo_quicksight.types.topic_numeric_range_filter

        out["numeric_range_filter"] = (
            capo_quicksight.types.topic_numeric_range_filter.redact_sensitive(
                value["numeric_range_filter"]
            )
        )
    if "date_range_filter" in value:
        import capo_quicksight.types.topic_date_range_filter

        out["date_range_filter"] = (
            capo_quicksight.types.topic_date_range_filter.redact_sensitive(
                value["date_range_filter"]
            )
        )
    if "relative_date_filter" in value:
        import capo_quicksight.types.topic_relative_date_filter

        out["relative_date_filter"] = (
            capo_quicksight.types.topic_relative_date_filter.redact_sensitive(
                value["relative_date_filter"]
            )
        )
    if "null_filter" in value:
        import capo_quicksight.types.topic_null_filter

        out["null_filter"] = capo_quicksight.types.topic_null_filter.redact_sensitive(
            value["null_filter"]
        )
    return out
