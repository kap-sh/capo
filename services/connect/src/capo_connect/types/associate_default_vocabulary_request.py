"""Generated from Smithy shape ``com.amazonaws.connect#AssociateDefaultVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.vocabulary_id
    import capo_connect.types.vocabulary_language_code


class AssociateDefaultVocabularyRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    language_code: "capo_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    """<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html">What is Amazon Transcribe?</a> </p>"""
    vocabulary_id: NotRequired["capo_connect.types.vocabulary_id.VocabularyId"]
    """<p>The identifier of the custom vocabulary. If this is empty, the default is set to none.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateDefaultVocabularyRequest) -> dict:
    out: dict = {}
    if "vocabulary_id" in value:
        out["VocabularyId"] = value["vocabulary_id"]
    return out


def deserialize_json(data: dict) -> AssociateDefaultVocabularyRequest:
    out: AssociateDefaultVocabularyRequest = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyId") is not None:
        out["vocabulary_id"] = data["VocabularyId"]
    return out
