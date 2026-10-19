"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_name


class GetMedicalVocabularyRequest(TypedDict, closed=True):
    vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName"
    """<p>The name of the custom medical vocabulary you want information about. Custom medical vocabulary names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalVocabularyRequest) -> dict:
    out: dict = {}
    out["VocabularyName"] = value["vocabulary_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalVocabularyRequest:
    out: GetMedicalVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        out["vocabulary_name"] = ""
    return out
