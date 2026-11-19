"""Generated from Smithy shape ``com.amazonaws.transcribe#ListLanguageModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.models
    import capo_transcribe.types.next_token


class ListLanguageModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    models: NotRequired["capo_transcribe.types.models.Models"]
    """<p>Provides information about the custom language models that match the criteria specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLanguageModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "models" in value:
        import capo_transcribe.types.models

        out["Models"] = capo_transcribe.types.models.serialize_aws_json_1_1(
            value["models"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLanguageModelsResponse:
    out: ListLanguageModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Models") is not None:
        import capo_transcribe.types.models

        out["models"] = capo_transcribe.types.models.deserialize_aws_json_1_1(
            data["Models"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLanguageModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "models" in value:
        import capo_transcribe.types.models

        out["Models"] = capo_transcribe.types.models.serialize_cbor(value["models"])
    return out


def deserialize_cbor(data: dict) -> ListLanguageModelsResponse:
    out: ListLanguageModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Models") is not None:
        import capo_transcribe.types.models

        out["models"] = capo_transcribe.types.models.deserialize_cbor(data["Models"])
    return out
