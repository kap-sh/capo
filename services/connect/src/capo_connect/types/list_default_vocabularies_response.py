"""Generated from Smithy shape ``com.amazonaws.connect#ListDefaultVocabulariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.default_vocabulary_list
    import capo_connect.types.vocabulary_next_token


class ListDefaultVocabulariesResponse(TypedDict, closed=True):
    default_vocabulary_list: (
        "capo_connect.types.default_vocabulary_list.DefaultVocabularyList"
    )
    """<p>A list of default vocabularies.</p>"""
    next_token: NotRequired[
        "capo_connect.types.vocabulary_next_token.VocabularyNextToken"
    ]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDefaultVocabulariesResponse) -> dict:
    out: dict = {}
    import capo_connect.types.default_vocabulary_list

    out["DefaultVocabularyList"] = (
        capo_connect.types.default_vocabulary_list.serialize_json(
            value["default_vocabulary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDefaultVocabulariesResponse:
    out: ListDefaultVocabulariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DefaultVocabularyList") is not None:
        import capo_connect.types.default_vocabulary_list

        out["default_vocabulary_list"] = (
            capo_connect.types.default_vocabulary_list.deserialize_json(
                data["DefaultVocabularyList"]
            )
        )
    else:
        out["default_vocabulary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
