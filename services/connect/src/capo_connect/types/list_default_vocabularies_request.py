"""Generated from Smithy shape ``com.amazonaws.connect#ListDefaultVocabulariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.vocabulary_language_code
    import capo_connect.types.vocabulary_next_token


class ListDefaultVocabulariesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    language_code: NotRequired[
        "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    ]
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html">What is Amazon Transcribe?</a> </p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired[
        "capo_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDefaultVocabulariesRequest) -> dict:
    out: dict = {}
    if "language_code" in value:
        import capo_connect.types.vocabulary_language_code

        out["LanguageCode"] = (
            capo_connect.types.vocabulary_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDefaultVocabulariesRequest:
    out: ListDefaultVocabulariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_connect.types.vocabulary_language_code

        out["language_code"] = (
            capo_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
