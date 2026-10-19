"""Generated from Smithy shape ``com.amazonaws.connect#VocabularySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.vocabulary_failure_reason
    import capo_connect.types.vocabulary_id
    import capo_connect.types.vocabulary_language_code
    import capo_connect.types.vocabulary_last_modified_time
    import capo_connect.types.vocabulary_name
    import capo_connect.types.vocabulary_state


class VocabularySummary(TypedDict, closed=True):
    name: "capo_connect.types.vocabulary_name.VocabularyName"
    """<p>A unique name of the custom vocabulary.</p>"""
    id: "capo_connect.types.vocabulary_id.VocabularyId"
    """<p>The identifier of the custom vocabulary.</p>"""
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the custom vocabulary.</p>"""
    language_code: "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html">What is Amazon Transcribe?</a> </p>"""
    state: "capo_connect.types.vocabulary_state.VocabularyState"
    """<p>The current state of the custom vocabulary.</p>"""
    last_modified_time: (
        "capo_connect.types.vocabulary_last_modified_time.VocabularyLastModifiedTime"
    )
    """<p>The timestamp when the custom vocabulary was last modified.</p>"""
    failure_reason: NotRequired[
        "capo_connect.types.vocabulary_failure_reason.VocabularyFailureReason"
    ]
    """<p>The reason why the custom vocabulary was not created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VocabularySummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_connect.types.vocabulary_language_code

    out["LanguageCode"] = capo_connect.types.vocabulary_language_code.serialize_json(
        value["language_code"]
    )
    import capo_connect.types.vocabulary_state

    out["State"] = capo_connect.types.vocabulary_state.serialize_json(value["state"])
    import capo_connect.types.vocabulary_last_modified_time

    out["LastModifiedTime"] = (
        capo_connect.types.vocabulary_last_modified_time.serialize_json(
            value["last_modified_time"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> VocabularySummary:
    out: VocabularySummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("LanguageCode") is not None:
        import capo_connect.types.vocabulary_language_code

        out["language_code"] = (
            capo_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode", ""
        )
    if data.get("State") is not None:
        import capo_connect.types.vocabulary_state

        out["state"] = capo_connect.types.vocabulary_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_connect.types.vocabulary_state.VocabularyState", ""
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.vocabulary_last_modified_time

        out["last_modified_time"] = (
            capo_connect.types.vocabulary_last_modified_time.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
