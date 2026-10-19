"""Generated from Smithy shape ``com.amazonaws.connectcases#ListFieldsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_summary_list
    import capo_connectcases.types.next_token


class ListFieldsResponse(TypedDict, closed=True):
    fields: "capo_connectcases.types.field_summary_list.FieldSummaryList"
    """<p>List of detailed field information.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFieldsResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_summary_list

    out["fields"] = capo_connectcases.types.field_summary_list.serialize_json(
        value["fields"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFieldsResponse:
    out: ListFieldsResponse = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_summary_list

        out["fields"] = capo_connectcases.types.field_summary_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
