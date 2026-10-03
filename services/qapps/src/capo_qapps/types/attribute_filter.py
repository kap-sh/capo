"""Generated from Smithy shape ``com.amazonaws.qapps#AttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.attribute_filter
    import capo_qapps.types.attribute_filters
    import capo_qapps.types.document_attribute


class AttributeFilter(TypedDict, closed=True):
    and_all_filters: NotRequired["capo_qapps.types.attribute_filters.AttributeFilters"]
    """<p>Performs a logical <code>AND</code> operation on all supplied filters.</p>"""
    or_all_filters: NotRequired["capo_qapps.types.attribute_filters.AttributeFilters"]
    """<p> Performs a logical <code>OR</code> operation on all supplied filters. </p>"""
    not_filter: NotRequired["capo_qapps.types.attribute_filter.AttributeFilter"]
    """<p>Performs a logical <code>NOT</code> operation on all supplied filters. </p>"""
    equals_to: NotRequired["capo_qapps.types.document_attribute.DocumentAttribute"]
    """<p>Performs an <i>equals</i> operation on two document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>dateValue</code>, <code>longValue</code>, <code>stringListValue</code> and <code>stringValue</code>.</p>"""
    contains_all: NotRequired["capo_qapps.types.document_attribute.DocumentAttribute"]
    """<p>Returns <code>true</code> when a document contains all the specified document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>stringListValue</code>.</p>"""
    contains_any: NotRequired["capo_qapps.types.document_attribute.DocumentAttribute"]
    """<p>Returns <code>true</code> when a document contains any of the specified document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>stringListValue</code>.</p>"""
    greater_than: NotRequired["capo_qapps.types.document_attribute.DocumentAttribute"]
    """<p>Performs a <i>greater than</i> operation on two document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>.</p>"""
    greater_than_or_equals: NotRequired[
        "capo_qapps.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a <i>greater than or equals</i> operation on two document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>. </p>"""
    less_than: NotRequired["capo_qapps.types.document_attribute.DocumentAttribute"]
    """<p>Performs a <i>less than</i> operation on two document attributes or metadata fields. Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value types</a>: <code>dateValue</code> and <code>longValue</code>.</p>"""
    less_than_or_equals: NotRequired[
        "capo_qapps.types.document_attribute.DocumentAttribute"
    ]
    """<p>Performs a <i>less than or equals</i> operation on two document attributes or metadata fields.Supported for the following <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html">document attribute value type</a>: <code>dateValue</code> and <code>longValue</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeFilter) -> dict:
    out: dict = {}
    if "and_all_filters" in value:
        import capo_qapps.types.attribute_filters

        out["andAllFilters"] = capo_qapps.types.attribute_filters.serialize_json(
            value["and_all_filters"]
        )
    if "or_all_filters" in value:
        import capo_qapps.types.attribute_filters

        out["orAllFilters"] = capo_qapps.types.attribute_filters.serialize_json(
            value["or_all_filters"]
        )
    if "not_filter" in value:
        import capo_qapps.types.attribute_filter

        out["notFilter"] = capo_qapps.types.attribute_filter.serialize_json(
            value["not_filter"]
        )
    if "equals_to" in value:
        import capo_qapps.types.document_attribute

        out["equalsTo"] = capo_qapps.types.document_attribute.serialize_json(
            value["equals_to"]
        )
    if "contains_all" in value:
        import capo_qapps.types.document_attribute

        out["containsAll"] = capo_qapps.types.document_attribute.serialize_json(
            value["contains_all"]
        )
    if "contains_any" in value:
        import capo_qapps.types.document_attribute

        out["containsAny"] = capo_qapps.types.document_attribute.serialize_json(
            value["contains_any"]
        )
    if "greater_than" in value:
        import capo_qapps.types.document_attribute

        out["greaterThan"] = capo_qapps.types.document_attribute.serialize_json(
            value["greater_than"]
        )
    if "greater_than_or_equals" in value:
        import capo_qapps.types.document_attribute

        out["greaterThanOrEquals"] = capo_qapps.types.document_attribute.serialize_json(
            value["greater_than_or_equals"]
        )
    if "less_than" in value:
        import capo_qapps.types.document_attribute

        out["lessThan"] = capo_qapps.types.document_attribute.serialize_json(
            value["less_than"]
        )
    if "less_than_or_equals" in value:
        import capo_qapps.types.document_attribute

        out["lessThanOrEquals"] = capo_qapps.types.document_attribute.serialize_json(
            value["less_than_or_equals"]
        )
    return out


def deserialize_json(data: dict) -> AttributeFilter:
    out: AttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("andAllFilters") is not None:
        import capo_qapps.types.attribute_filters

        out["and_all_filters"] = capo_qapps.types.attribute_filters.deserialize_json(
            data["andAllFilters"]
        )
    if data.get("orAllFilters") is not None:
        import capo_qapps.types.attribute_filters

        out["or_all_filters"] = capo_qapps.types.attribute_filters.deserialize_json(
            data["orAllFilters"]
        )
    if data.get("notFilter") is not None:
        import capo_qapps.types.attribute_filter

        out["not_filter"] = capo_qapps.types.attribute_filter.deserialize_json(
            data["notFilter"]
        )
    if data.get("equalsTo") is not None:
        import capo_qapps.types.document_attribute

        out["equals_to"] = capo_qapps.types.document_attribute.deserialize_json(
            data["equalsTo"]
        )
    if data.get("containsAll") is not None:
        import capo_qapps.types.document_attribute

        out["contains_all"] = capo_qapps.types.document_attribute.deserialize_json(
            data["containsAll"]
        )
    if data.get("containsAny") is not None:
        import capo_qapps.types.document_attribute

        out["contains_any"] = capo_qapps.types.document_attribute.deserialize_json(
            data["containsAny"]
        )
    if data.get("greaterThan") is not None:
        import capo_qapps.types.document_attribute

        out["greater_than"] = capo_qapps.types.document_attribute.deserialize_json(
            data["greaterThan"]
        )
    if data.get("greaterThanOrEquals") is not None:
        import capo_qapps.types.document_attribute

        out["greater_than_or_equals"] = (
            capo_qapps.types.document_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        )
    if data.get("lessThan") is not None:
        import capo_qapps.types.document_attribute

        out["less_than"] = capo_qapps.types.document_attribute.deserialize_json(
            data["lessThan"]
        )
    if data.get("lessThanOrEquals") is not None:
        import capo_qapps.types.document_attribute

        out["less_than_or_equals"] = (
            capo_qapps.types.document_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        )
    return out
