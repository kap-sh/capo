"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.condition_operator
    import capo_kendra.types.document_attribute_key
    import capo_kendra.types.document_attribute_value


class DocumentAttributeCondition(TypedDict, closed=True):
    condition_document_attribute_key: (
        "capo_kendra.types.document_attribute_key.DocumentAttributeKey"
    )
    """<p>The identifier of the document attribute used for the condition.</p> <p>For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.</p> <p>Amazon Kendra currently does not support <code>_document_body</code> as an attribute key used for the condition.</p>"""
    operator: "capo_kendra.types.condition_operator.ConditionOperator"
    """<p>The condition operator.</p> <p>For example, you can use 'Contains' to partially match a string.</p>"""
    condition_on_value: NotRequired[
        "capo_kendra.types.document_attribute_value.DocumentAttributeValue"
    ]
    """<p>The value used by the operator.</p> <p>For example, you can specify the value 'financial' for strings in the 'Source_URI' field that partially match or contain this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeCondition) -> dict:
    out: dict = {}
    out["ConditionDocumentAttributeKey"] = value["condition_document_attribute_key"]
    import capo_kendra.types.condition_operator

    out["Operator"] = capo_kendra.types.condition_operator.serialize_aws_json_1_1(
        value["operator"]
    )
    if "condition_on_value" in value:
        import capo_kendra.types.document_attribute_value

        out["ConditionOnValue"] = (
            capo_kendra.types.document_attribute_value.serialize_aws_json_1_1(
                value["condition_on_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttributeCondition:
    out: DocumentAttributeCondition = {}  # type: ignore[typeddict-item]
    if data.get("ConditionDocumentAttributeKey") is not None:
        out["condition_document_attribute_key"] = data["ConditionDocumentAttributeKey"]
    else:
        out["condition_document_attribute_key"] = ""
    if data.get("Operator") is not None:
        import capo_kendra.types.condition_operator

        out["operator"] = capo_kendra.types.condition_operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_kendra.types.condition_operator.ConditionOperator", ""
        )
    if data.get("ConditionOnValue") is not None:
        import capo_kendra.types.document_attribute_value

        out["condition_on_value"] = (
            capo_kendra.types.document_attribute_value.deserialize_aws_json_1_1(
                data["ConditionOnValue"]
            )
        )
    return out
