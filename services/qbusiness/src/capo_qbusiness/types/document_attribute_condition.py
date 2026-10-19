"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_key
    import capo_qbusiness.types.document_attribute_value
    import capo_qbusiness.types.document_enrichment_condition_operator


class DocumentAttributeCondition(TypedDict, closed=True):
    key: "capo_qbusiness.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier of the document attribute used for the condition.</p> <p>For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.</p> <p>Amazon Q Business currently doesn't support <code>_document_body</code> as an attribute key used for the condition.</p>"""
    operator: "capo_qbusiness.types.document_enrichment_condition_operator.DocumentEnrichmentConditionOperator"
    """<p>The identifier of the document attribute used for the condition.</p> <p>For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.</p> <p>Amazon Q Business currently does not support <code>_document_body</code> as an attribute key used for the condition.</p>"""
    value: NotRequired[
        "capo_qbusiness.types.document_attribute_value.DocumentAttributeValue"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeCondition) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_qbusiness.types.document_enrichment_condition_operator

    out["operator"] = (
        capo_qbusiness.types.document_enrichment_condition_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import capo_qbusiness.types.document_attribute_value

        out["value"] = capo_qbusiness.types.document_attribute_value.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> DocumentAttributeCondition:
    out: DocumentAttributeCondition = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("operator") is not None:
        import capo_qbusiness.types.document_enrichment_condition_operator

        out["operator"] = (
            capo_qbusiness.types.document_enrichment_condition_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_qbusiness.types.document_enrichment_condition_operator.DocumentEnrichmentConditionOperator",
            "",
        )
    if data.get("value") is not None:
        import capo_qbusiness.types.document_attribute_value

        out["value"] = capo_qbusiness.types.document_attribute_value.deserialize_json(
            data["value"]
        )
    return out
