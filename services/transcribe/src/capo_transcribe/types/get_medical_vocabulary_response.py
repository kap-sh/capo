"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.language_code
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_name
    import capo_transcribe.types.vocabulary_state


class GetMedicalVocabularyResponse(TypedDict, closed=True):
    vocabulary_name: NotRequired["capo_transcribe.types.vocabulary_name.VocabularyName"]
    """<p>The name of the custom medical vocabulary you requested information about.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom medical vocabulary. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    vocabulary_state: NotRequired[
        "capo_transcribe.types.vocabulary_state.VocabularyState"
    ]
    """<p>The processing state of your custom medical vocabulary. If the state is <code>READY</code>, you can use the custom vocabulary in a <code>StartMedicalTranscriptionJob</code> request.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom medical vocabulary was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>VocabularyState</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the custom medical vocabulary request failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    download_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location where the specified custom medical vocabulary is stored; use this URI to view or download the custom vocabulary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalVocabularyResponse) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = (
            capo_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "vocabulary_state" in value:
        import capo_transcribe.types.vocabulary_state

        out["VocabularyState"] = (
            capo_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["vocabulary_state"]
            )
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = (
            capo_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "download_uri" in value:
        out["DownloadUri"] = value["download_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalVocabularyResponse:
    out: GetMedicalVocabularyResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("VocabularyState") is not None:
        import capo_transcribe.types.vocabulary_state

        out["vocabulary_state"] = (
            capo_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["VocabularyState"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("DownloadUri") is not None:
        out["download_uri"] = data["DownloadUri"]
    return out
