"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassificationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_mode
    import capo_comprehend.types.labels_list


class DocumentClassificationConfig(TypedDict, closed=True):
    mode: "capo_comprehend.types.document_classifier_mode.DocumentClassifierMode"
    """<p>Classification mode indicates whether the documents are <code>MULTI_CLASS</code> or <code>MULTI_LABEL</code>.</p>"""
    labels: NotRequired["capo_comprehend.types.labels_list.LabelsList"]
    """<p>One or more labels to associate with the custom classifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassificationConfig) -> dict:
    out: dict = {}
    import capo_comprehend.types.document_classifier_mode

    out["Mode"] = capo_comprehend.types.document_classifier_mode.serialize_aws_json_1_1(
        value["mode"]
    )
    if "labels" in value:
        import capo_comprehend.types.labels_list

        out["Labels"] = capo_comprehend.types.labels_list.serialize_aws_json_1_1(
            value["labels"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassificationConfig:
    out: DocumentClassificationConfig = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_comprehend.types.document_classifier_mode

        out["mode"] = (
            capo_comprehend.types.document_classifier_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_comprehend.types.document_classifier_mode.DocumentClassifierMode", ""
        )
    if data.get("Labels") is not None:
        import capo_comprehend.types.labels_list

        out["labels"] = capo_comprehend.types.labels_list.deserialize_aws_json_1_1(
            data["Labels"]
        )
    return out
