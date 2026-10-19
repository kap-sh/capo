"""Generated from Smithy shape ``com.amazonaws.chatbot#ListAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.association_list
    import capo_chatbot.types.string


class ListAssociationsResult(TypedDict, closed=True):
    associations: "capo_chatbot.types.association_list.AssociationList"
    """<p>The resources associated with this channel configuration.</p>"""
    next_token: NotRequired["capo_chatbot.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociationsResult) -> dict:
    out: dict = {}
    import capo_chatbot.types.association_list

    out["Associations"] = capo_chatbot.types.association_list.serialize_json(
        value["associations"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociationsResult:
    out: ListAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Associations") is not None:
        import capo_chatbot.types.association_list

        out["associations"] = capo_chatbot.types.association_list.deserialize_json(
            data["Associations"]
        )
    else:
        out["associations"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
