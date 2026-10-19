"""Generated from Smithy shape ``com.amazonaws.dsql#ListStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.next_token
    import capo_dsql.types.stream_list


class ListStreamsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_dsql.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    streams: "capo_dsql.types.stream_list.StreamList"
    """<p>An array of the returned streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_dsql.types.stream_list

    out["streams"] = capo_dsql.types.stream_list.serialize_json(value["streams"])
    return out


def deserialize_json(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("streams") is not None:
        import capo_dsql.types.stream_list

        out["streams"] = capo_dsql.types.stream_list.deserialize_json(data["streams"])
    else:
        out["streams"] = []
    return out
