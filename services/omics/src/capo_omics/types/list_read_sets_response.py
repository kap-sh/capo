"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.next_token
    import capo_omics.types.read_set_list


class ListReadSetsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    read_sets: "capo_omics.types.read_set_list.ReadSetList"
    """<p>A list of read sets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_omics.types.read_set_list

    out["readSets"] = capo_omics.types.read_set_list.serialize_json(value["read_sets"])
    return out


def deserialize_json(data: dict) -> ListReadSetsResponse:
    out: ListReadSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("readSets") is not None:
        import capo_omics.types.read_set_list

        out["read_sets"] = capo_omics.types.read_set_list.deserialize_json(
            data["readSets"]
        )
    else:
        out["read_sets"] = []
    return out
