"""Generated from Smithy shape ``com.amazonaws.transcribe#ListVocabularyFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.next_token
    import capo_transcribe.types.vocabulary_filters


class ListVocabularyFiltersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    vocabulary_filters: NotRequired[
        "capo_transcribe.types.vocabulary_filters.VocabularyFilters"
    ]
    """<p>Provides information about the custom vocabulary filters that match the criteria specified in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVocabularyFiltersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabulary_filters" in value:
        import capo_transcribe.types.vocabulary_filters

        out["VocabularyFilters"] = (
            capo_transcribe.types.vocabulary_filters.serialize_aws_json_1_1(
                value["vocabulary_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVocabularyFiltersResponse:
    out: ListVocabularyFiltersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("VocabularyFilters") is not None:
        import capo_transcribe.types.vocabulary_filters

        out["vocabulary_filters"] = (
            capo_transcribe.types.vocabulary_filters.deserialize_aws_json_1_1(
                data["VocabularyFilters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVocabularyFiltersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vocabulary_filters" in value:
        import capo_transcribe.types.vocabulary_filters

        out["VocabularyFilters"] = (
            capo_transcribe.types.vocabulary_filters.serialize_cbor(
                value["vocabulary_filters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListVocabularyFiltersResponse:
    out: ListVocabularyFiltersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("VocabularyFilters") is not None:
        import capo_transcribe.types.vocabulary_filters

        out["vocabulary_filters"] = (
            capo_transcribe.types.vocabulary_filters.deserialize_cbor(
                data["VocabularyFilters"]
            )
        )
    return out
