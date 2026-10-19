"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateMedicalVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.language_code
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_name


class UpdateMedicalVocabularyRequest(TypedDict, closed=True):
    vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName"
    """<p>The name of the custom medical vocabulary you want to update. Custom medical vocabulary names are case sensitive.</p>"""
    language_code: "capo_transcribe.types.language_code.LanguageCode"
    """<p>The language code that represents the language of the entries in the custom vocabulary you want to update. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    vocabulary_file_uri: "capo_transcribe.types.uri.Uri"
    """<p>The Amazon S3 location of the text file that contains your custom medical vocabulary. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMedicalVocabularyRequest) -> dict:
    out: dict = {}
    out["VocabularyName"] = value["vocabulary_name"]
    import capo_transcribe.types.language_code

    out["LanguageCode"] = capo_transcribe.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    out["VocabularyFileUri"] = value["vocabulary_file_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMedicalVocabularyRequest:
    out: UpdateMedicalVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        out["vocabulary_name"] = ""
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_transcribe.types.language_code.LanguageCode", ""
        )
    if data.get("VocabularyFileUri") is not None:
        out["vocabulary_file_uri"] = data["VocabularyFileUri"]
    else:
        out["vocabulary_file_uri"] = ""
    return out
