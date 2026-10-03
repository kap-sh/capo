"""Generated from Smithy shape ``com.amazonaws.connect#CreateVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map
    import capo_connect.types.vocabulary_content
    import capo_connect.types.vocabulary_language_code
    import capo_connect.types.vocabulary_name


class CreateVocabularyRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>. If a create request is received more than once with same client token, subsequent requests return the previous response without creating a vocabulary again.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    vocabulary_name: "capo_connect.types.vocabulary_name.VocabularyName"
    """<p>A unique name of the custom vocabulary.</p>"""
    language_code: "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html">What is Amazon Transcribe?</a> </p>"""
    content: "capo_connect.types.vocabulary_content.VocabularyContent"
    """<p>The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with <code>Phrase</code>, <code>IPA</code>, <code>SoundsLike</code>, and <code>DisplayAs</code> fields. Separate the fields with TAB characters. The size limit is 50KB. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table">Create a custom vocabulary using a table</a>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVocabularyRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["VocabularyName"] = value["vocabulary_name"]
    import capo_connect.types.vocabulary_language_code

    out["LanguageCode"] = capo_connect.types.vocabulary_language_code.serialize_json(
        value["language_code"]
    )
    out["Content"] = value["content"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVocabularyRequest:
    out: CreateVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        raise DeserializationError("CreateVocabularyRequest.vocabulary_name required")
    if data.get("LanguageCode") is not None:
        import capo_connect.types.vocabulary_language_code

        out["language_code"] = (
            capo_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("CreateVocabularyRequest.language_code required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CreateVocabularyRequest.content required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
