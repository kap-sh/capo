"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.data_sets_summary_list
    import capo_m2.types.next_token


class ListDataSetsResponse(TypedDict, closed=True):
    data_sets: "capo_m2.types.data_sets_summary_list.DataSetsSummaryList"
    """<p>The list of data sets, containing information including the creation time, the data set name, the data set organization, the data set format, and the last time the data set was referenced or updated.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.data_sets_summary_list

    out["dataSets"] = capo_m2.types.data_sets_summary_list.serialize_json(
        value["data_sets"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetsResponse:
    out: ListDataSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSets") is not None:
        import capo_m2.types.data_sets_summary_list

        out["data_sets"] = capo_m2.types.data_sets_summary_list.deserialize_json(
            data["dataSets"]
        )
    else:
        out["data_sets"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
