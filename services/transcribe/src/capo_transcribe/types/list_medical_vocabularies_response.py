"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalVocabulariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.next_token
    import capo_transcribe.types.vocabularies
    import capo_transcribe.types.vocabulary_state


class ListMedicalVocabulariesResponse(TypedDict, closed=True):
    status: NotRequired["capo_transcribe.types.vocabulary_state.VocabularyState"]
    """<p>Lists all custom medical vocabularies that have the status specified in your request. Custom vocabularies are ordered by creation date, with the newest vocabulary first.</p>"""
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    vocabularies: NotRequired["capo_transcribe.types.vocabularies.Vocabularies"]
    """<p>Provides information about the custom medical vocabularies that match the criteria specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalVocabulariesResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.vocabulary_state

        out["Status"] = capo_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
            value["status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabularies" in value:
        import capo_transcribe.types.vocabularies

        out["Vocabularies"] = capo_transcribe.types.vocabularies.serialize_aws_json_1_1(
            value["vocabularies"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalVocabulariesResponse:
    out: ListMedicalVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.vocabulary_state

        out["status"] = capo_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Vocabularies") is not None:
        import capo_transcribe.types.vocabularies

        out["vocabularies"] = (
            capo_transcribe.types.vocabularies.deserialize_aws_json_1_1(
                data["Vocabularies"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMedicalVocabulariesResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.vocabulary_state

        out["Status"] = capo_transcribe.types.vocabulary_state.serialize_cbor(
            value["status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabularies" in value:
        import capo_transcribe.types.vocabularies

        out["Vocabularies"] = capo_transcribe.types.vocabularies.serialize_cbor(
            value["vocabularies"]
        )
    return out


def deserialize_cbor(data: dict) -> ListMedicalVocabulariesResponse:
    out: ListMedicalVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.vocabulary_state

        out["status"] = capo_transcribe.types.vocabulary_state.deserialize_cbor(
            data["Status"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Vocabularies") is not None:
        import capo_transcribe.types.vocabularies

        out["vocabularies"] = capo_transcribe.types.vocabularies.deserialize_cbor(
            data["Vocabularies"]
        )
    return out
