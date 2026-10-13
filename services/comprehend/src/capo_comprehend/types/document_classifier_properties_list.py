"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierPropertiesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_properties

DocumentClassifierPropertiesList: TypeAlias = list[
    "capo_comprehend.types.document_classifier_properties.DocumentClassifierProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierPropertiesList) -> list:
    import capo_comprehend.types.document_classifier_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.document_classifier_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassifierPropertiesList:
    import capo_comprehend.types.document_classifier_properties

    out: DocumentClassifierPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.document_classifier_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: DocumentClassifierPropertiesList) -> list[Any]:
    import capo_comprehend.types.document_classifier_properties

    return [
        capo_comprehend.types.document_classifier_properties.redact_sensitive(item)
        for item in value
    ]
