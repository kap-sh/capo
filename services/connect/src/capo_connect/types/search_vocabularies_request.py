"""Generated from Smithy shape ``com.amazonaws.connect#SearchVocabulariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.vocabulary_language_code
    import capo_connect.types.vocabulary_name
    import capo_connect.types.vocabulary_next_token
    import capo_connect.types.vocabulary_state


class SearchVocabulariesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired[
        "capo_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    state: NotRequired["capo_connect.types.vocabulary_state.VocabularyState"]
    """<p>The current state of the custom vocabulary.</p>"""
    name_starts_with: NotRequired["capo_connect.types.vocabulary_name.VocabularyName"]
    """<p>The starting pattern of the name of the vocabulary.</p>"""
    language_code: NotRequired[
        "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    ]
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html">What is Amazon Transcribe?</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVocabulariesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "state" in value:
        import capo_connect.types.vocabulary_state

        out["State"] = capo_connect.types.vocabulary_state.serialize_json(
            value["state"]
        )
    if "name_starts_with" in value:
        out["NameStartsWith"] = value["name_starts_with"]
    if "language_code" in value:
        import capo_connect.types.vocabulary_language_code

        out["LanguageCode"] = (
            capo_connect.types.vocabulary_language_code.serialize_json(
                value["language_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchVocabulariesRequest:
    out: SearchVocabulariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("State") is not None:
        import capo_connect.types.vocabulary_state

        out["state"] = capo_connect.types.vocabulary_state.deserialize_json(
            data["State"]
        )
    if data.get("NameStartsWith") is not None:
        out["name_starts_with"] = data["NameStartsWith"]
    if data.get("LanguageCode") is not None:
        import capo_connect.types.vocabulary_language_code

        out["language_code"] = (
            capo_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    return out
