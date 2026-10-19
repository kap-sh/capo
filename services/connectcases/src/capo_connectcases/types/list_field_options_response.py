"""Generated from Smithy shape ``com.amazonaws.connectcases#ListFieldOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_options_list
    import capo_connectcases.types.next_token


class ListFieldOptionsResponse(TypedDict, closed=True):
    options: "capo_connectcases.types.field_options_list.FieldOptionsList"
    """<p>A list of <code>FieldOption</code> objects.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFieldOptionsResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_options_list

    out["options"] = capo_connectcases.types.field_options_list.serialize_json(
        value["options"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFieldOptionsResponse:
    out: ListFieldOptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("options") is not None:
        import capo_connectcases.types.field_options_list

        out["options"] = capo_connectcases.types.field_options_list.deserialize_json(
            data["options"]
        )
    else:
        out["options"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
