"""Generated from Smithy shape ``com.amazonaws.textract#HumanLoopDataAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.content_classifiers


class HumanLoopDataAttributes(TypedDict, closed=True):
    content_classifiers: NotRequired[
        "capo_textract.types.content_classifiers.ContentClassifiers"
    ]
    """<p>Sets whether the input image is free of personally identifiable information or adult content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopDataAttributes) -> dict:
    out: dict = {}
    if "content_classifiers" in value:
        import capo_textract.types.content_classifiers

        out["ContentClassifiers"] = (
            capo_textract.types.content_classifiers.serialize_aws_json_1_1(
                value["content_classifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopDataAttributes:
    out: HumanLoopDataAttributes = {}  # type: ignore[typeddict-item]
    if data.get("ContentClassifiers") is not None:
        import capo_textract.types.content_classifiers

        out["content_classifiers"] = (
            capo_textract.types.content_classifiers.deserialize_aws_json_1_1(
                data["ContentClassifiers"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HumanLoopDataAttributes) -> dict:
    out: dict = {}
    if "content_classifiers" in value:
        import capo_textract.types.content_classifiers

        out["ContentClassifiers"] = (
            capo_textract.types.content_classifiers.serialize_cbor(
                value["content_classifiers"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> HumanLoopDataAttributes:
    out: HumanLoopDataAttributes = {}  # type: ignore[typeddict-item]
    if data.get("ContentClassifiers") is not None:
        import capo_textract.types.content_classifiers

        out["content_classifiers"] = (
            capo_textract.types.content_classifiers.deserialize_cbor(
                data["ContentClassifiers"]
            )
        )
    return out
