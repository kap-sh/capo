"""Generated from Smithy shape ``com.amazonaws.connect#DeleteVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.vocabulary_id
    import capo_connect.types.vocabulary_state


class DeleteVocabularyResponse(TypedDict, closed=True):
    vocabulary_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the custom vocabulary.</p>"""
    vocabulary_id: "capo_connect.types.vocabulary_id.VocabularyId"
    """<p>The identifier of the custom vocabulary.</p>"""
    state: "capo_connect.types.vocabulary_state.VocabularyState"
    """<p>The current state of the custom vocabulary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVocabularyResponse) -> dict:
    out: dict = {}
    out["VocabularyArn"] = value["vocabulary_arn"]
    out["VocabularyId"] = value["vocabulary_id"]
    import capo_connect.types.vocabulary_state

    out["State"] = capo_connect.types.vocabulary_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> DeleteVocabularyResponse:
    out: DeleteVocabularyResponse = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyArn") is not None:
        out["vocabulary_arn"] = data["VocabularyArn"]
    else:
        out["vocabulary_arn"] = ""
    if data.get("VocabularyId") is not None:
        out["vocabulary_id"] = data["VocabularyId"]
    else:
        out["vocabulary_id"] = ""
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
    return out
