"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.language_code
    import capo_transcribe.types.vocabulary_name
    import capo_transcribe.types.vocabulary_state


class UpdateVocabularyResponse(TypedDict, closed=True):
    vocabulary_name: NotRequired["capo_transcribe.types.vocabulary_name.VocabularyName"]
    """<p>The name of the updated custom vocabulary.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom vocabulary.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom vocabulary was last updated.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    vocabulary_state: NotRequired[
        "capo_transcribe.types.vocabulary_state.VocabularyState"
    ]
    """<p>The processing state of your custom vocabulary. If the state is <code>READY</code>, you can use the custom vocabulary in a <code>StartTranscriptionJob</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVocabularyResponse) -> dict:
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
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = (
            capo_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "vocabulary_state" in value:
        import capo_transcribe.types.vocabulary_state

        out["VocabularyState"] = (
            capo_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["vocabulary_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVocabularyResponse:
    out: UpdateVocabularyResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("VocabularyState") is not None:
        import capo_transcribe.types.vocabulary_state

        out["vocabulary_state"] = (
            capo_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["VocabularyState"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateVocabularyResponse) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = capo_transcribe.types.language_code.serialize_cbor(
            value["language_code"]
        )
    if "last_modified_time" in value:
        import capo_transcribe.types.date_time

        out["LastModifiedTime"] = capo_transcribe.types.date_time.serialize_cbor(
            value["last_modified_time"]
        )
    if "vocabulary_state" in value:
        import capo_transcribe.types.vocabulary_state

        out["VocabularyState"] = capo_transcribe.types.vocabulary_state.serialize_cbor(
            value["vocabulary_state"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateVocabularyResponse:
    out: UpdateVocabularyResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = capo_transcribe.types.language_code.deserialize_cbor(
            data["LanguageCode"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_transcribe.types.date_time

        out["last_modified_time"] = capo_transcribe.types.date_time.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("VocabularyState") is not None:
        import capo_transcribe.types.vocabulary_state

        out["vocabulary_state"] = (
            capo_transcribe.types.vocabulary_state.deserialize_cbor(
                data["VocabularyState"]
            )
        )
    return out
