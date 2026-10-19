"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteVocabularyFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_filter_name


class DeleteVocabularyFilterRequest(TypedDict, closed=True):
    vocabulary_filter_name: (
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    )
    """<p>The name of the custom vocabulary filter you want to delete. Custom vocabulary filter names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVocabularyFilterRequest) -> dict:
    out: dict = {}
    out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVocabularyFilterRequest:
    out: DeleteVocabularyFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    else:
        out["vocabulary_filter_name"] = ""
    return out
