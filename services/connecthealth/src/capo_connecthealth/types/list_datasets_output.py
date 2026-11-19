"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDatasetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_summary_list


class ListDatasetsOutput(TypedDict, closed=True):
    items: "capo_connecthealth.types.dataset_summary_list.DatasetSummaryList"
    """<p>A list of dataset summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next page of results. Not returned if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsOutput) -> dict:
    out: dict = {}
    import capo_connecthealth.types.dataset_summary_list

    out["items"] = capo_connecthealth.types.dataset_summary_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsOutput:
    out: ListDatasetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_connecthealth.types.dataset_summary_list

        out["items"] = capo_connecthealth.types.dataset_summary_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
