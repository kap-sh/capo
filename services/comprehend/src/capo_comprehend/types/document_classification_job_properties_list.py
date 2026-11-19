"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassificationJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.document_classification_job_properties

DocumentClassificationJobPropertiesList: TypeAlias = list[
    "capo_comprehend.types.document_classification_job_properties.DocumentClassificationJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassificationJobPropertiesList) -> list:
    import capo_comprehend.types.document_classification_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.document_classification_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassificationJobPropertiesList:
    import capo_comprehend.types.document_classification_job_properties

    out: DocumentClassificationJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.document_classification_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassificationJobPropertiesList) -> list:
    import capo_comprehend.types.document_classification_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.document_classification_job_properties.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> DocumentClassificationJobPropertiesList:
    import capo_comprehend.types.document_classification_job_properties

    out: DocumentClassificationJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.document_classification_job_properties.deserialize_cbor(
                item
            )
        )
    return out
