"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateVocabularyFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.language_code
    import capo_transcribe.types.vocabulary_filter_name


class CreateVocabularyFilterResponse(TypedDict, closed=True):
    vocabulary_filter_name: NotRequired[
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name you chose for your custom vocabulary filter.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom vocabulary filter.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time you created your custom vocabulary filter.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVocabularyFilterResponse) -> dict:
    out: dict = {}
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVocabularyFilterResponse:
    out: CreateVocabularyFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateVocabularyFilterResponse) -> dict:
    out: dict = {}
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
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
    return out


def deserialize_cbor(data: dict) -> CreateVocabularyFilterResponse:
    out: CreateVocabularyFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
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
    return out
