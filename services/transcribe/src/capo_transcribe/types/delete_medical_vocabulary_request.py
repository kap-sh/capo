"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteMedicalVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_name


class DeleteMedicalVocabularyRequest(TypedDict, closed=True):
    vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName"
    """<p>The name of the custom medical vocabulary you want to delete. Custom medical vocabulary names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMedicalVocabularyRequest) -> dict:
    out: dict = {}
    out["VocabularyName"] = value["vocabulary_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMedicalVocabularyRequest:
    out: DeleteMedicalVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        out["vocabulary_name"] = ""
    return out
