"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalVocabulariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.max_results
    import capo_transcribe.types.next_token
    import capo_transcribe.types.vocabulary_name
    import capo_transcribe.types.vocabulary_state


class ListMedicalVocabulariesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListMedicalVocabularies</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["capo_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of custom medical vocabularies to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""
    state_equals: NotRequired["capo_transcribe.types.vocabulary_state.VocabularyState"]
    """<p>Returns only custom medical vocabularies with the specified state. Custom vocabularies are ordered by creation date, with the newest vocabulary first. If you do not include <code>StateEquals</code>, all custom medical vocabularies are returned.</p>"""
    name_contains: NotRequired["capo_transcribe.types.vocabulary_name.VocabularyName"]
    """<p>Returns only the custom medical vocabularies that contain the specified string. The search is not case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalVocabulariesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "state_equals" in value:
        import capo_transcribe.types.vocabulary_state

        out["StateEquals"] = (
            capo_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["state_equals"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalVocabulariesRequest:
    out: ListMedicalVocabulariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("StateEquals") is not None:
        import capo_transcribe.types.vocabulary_state

        out["state_equals"] = (
            capo_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["StateEquals"]
            )
        )
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMedicalVocabulariesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "state_equals" in value:
        import capo_transcribe.types.vocabulary_state

        out["StateEquals"] = capo_transcribe.types.vocabulary_state.serialize_cbor(
            value["state_equals"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    return out


def deserialize_cbor(data: dict) -> ListMedicalVocabulariesRequest:
    out: ListMedicalVocabulariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("StateEquals") is not None:
        import capo_transcribe.types.vocabulary_state

        out["state_equals"] = capo_transcribe.types.vocabulary_state.deserialize_cbor(
            data["StateEquals"]
        )
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    return out
