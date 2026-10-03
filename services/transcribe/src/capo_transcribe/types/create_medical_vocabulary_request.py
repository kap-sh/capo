"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateMedicalVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.language_code
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_name


class CreateMedicalVocabularyRequest(TypedDict, closed=True):
    vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName"
    """<p>A unique name, chosen by you, for your new custom medical vocabulary.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom medical vocabulary with the same name as an existing custom medical vocabulary, you get a <code>ConflictException</code> error.</p>"""
    language_code: "capo_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language of the entries in your custom vocabulary. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    vocabulary_file_uri: "capo_transcribe.types.uri.Uri"
    """<p>The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary. The URI must be in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom medical vocabulary at the time you create this new custom vocabulary.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMedicalVocabularyRequest) -> dict:
    out: dict = {}
    out["VocabularyName"] = value["vocabulary_name"]
    import capo_transcribe.types.language_code

    out["LanguageCode"] = capo_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    out["VocabularyFileUri"] = value["vocabulary_file_uri"]
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMedicalVocabularyRequest:
    out: CreateMedicalVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        raise DeserializationError(
            "CreateMedicalVocabularyRequest.vocabulary_name required"
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMedicalVocabularyRequest.language_code required"
        )
    if data.get("VocabularyFileUri") is not None:
        out["vocabulary_file_uri"] = data["VocabularyFileUri"]
    else:
        raise DeserializationError(
            "CreateMedicalVocabularyRequest.vocabulary_file_uri required"
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
