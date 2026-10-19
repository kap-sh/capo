"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetWorkUnitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.query_id_string
    import capo_lakeformation.types.token
    import capo_lakeformation.types.work_unit_range_list


class GetWorkUnitsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""
    query_id: "capo_lakeformation.types.query_id_string.QueryIdString"
    """<p>The ID of the plan query operation.</p>"""
    work_unit_ranges: "capo_lakeformation.types.work_unit_range_list.WorkUnitRangeList"
    """<p>A <code>WorkUnitRangeList</code> object that specifies the valid range of work unit IDs for querying the execution service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkUnitsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["QueryId"] = value["query_id"]
    import capo_lakeformation.types.work_unit_range_list

    out["WorkUnitRanges"] = (
        capo_lakeformation.types.work_unit_range_list.serialize_json(
            value["work_unit_ranges"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetWorkUnitsResponse:
    out: GetWorkUnitsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    if data.get("WorkUnitRanges") is not None:
        import capo_lakeformation.types.work_unit_range_list

        out["work_unit_ranges"] = (
            capo_lakeformation.types.work_unit_range_list.deserialize_json(
                data["WorkUnitRanges"]
            )
        )
    else:
        out["work_unit_ranges"] = []
    return out
