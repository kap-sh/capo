"""Generated from Smithy shape ``com.amazonaws.transcribe#DescribeLanguageModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.language_model


class DescribeLanguageModelResponse(TypedDict, closed=True):
    language_model: NotRequired["capo_transcribe.types.language_model.LanguageModel"]
    """<p>Provides information about the specified custom language model.</p> <p>This parameter also shows if the base language model you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.</p> <p>If you tried to create a new custom language model and the request wasn't successful, you can use this <code>DescribeLanguageModel</code> to help identify the reason for this failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLanguageModelResponse) -> dict:
    out: dict = {}
    if "language_model" in value:
        import capo_transcribe.types.language_model

        out["LanguageModel"] = (
            capo_transcribe.types.language_model.serialize_aws_json_1_1(
                value["language_model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLanguageModelResponse:
    out: DescribeLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("LanguageModel") is not None:
        import capo_transcribe.types.language_model

        out["language_model"] = (
            capo_transcribe.types.language_model.deserialize_aws_json_1_1(
                data["LanguageModel"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeLanguageModelResponse) -> dict:
    out: dict = {}
    if "language_model" in value:
        import capo_transcribe.types.language_model

        out["LanguageModel"] = capo_transcribe.types.language_model.serialize_cbor(
            value["language_model"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeLanguageModelResponse:
    out: DescribeLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("LanguageModel") is not None:
        import capo_transcribe.types.language_model

        out["language_model"] = capo_transcribe.types.language_model.deserialize_cbor(
            data["LanguageModel"]
        )
    return out
