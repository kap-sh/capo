"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyFilterInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.language_code
    import capo_transcribe.types.vocabulary_filter_name


class VocabularyFilterInfo(TypedDict, closed=True):
    vocabulary_filter_name: NotRequired[
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>A unique name, chosen by you, for your custom vocabulary filter. This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code that represents the language of the entries in your vocabulary filter. Each custom vocabulary filter must contain terms in only one language.</p> <p>A custom vocabulary filter can only be used to transcribe files in the same language as the filter. For example, if you create a custom vocabulary filter using US English (<code>en-US</code>), you can only apply this filter to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>"""
    last_modified_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom vocabulary filter was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VocabularyFilterInfo) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> VocabularyFilterInfo:
    out: VocabularyFilterInfo = {}  # type: ignore[typeddict-item]
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
