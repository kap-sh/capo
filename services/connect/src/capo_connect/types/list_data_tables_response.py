"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_summary_list
    import capo_connect.types.next_token


class ListDataTablesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    data_table_summary_list: (
        "capo_connect.types.data_table_summary_list.DataTableSummaryList"
    )
    """<p>A list of data table summaries containing basic information about each table including ID, ARN, name, and modification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTablesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.data_table_summary_list

    out["DataTableSummaryList"] = (
        capo_connect.types.data_table_summary_list.serialize_json(
            value["data_table_summary_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListDataTablesResponse:
    out: ListDataTablesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("DataTableSummaryList") is not None:
        import capo_connect.types.data_table_summary_list

        out["data_table_summary_list"] = (
            capo_connect.types.data_table_summary_list.deserialize_json(
                data["DataTableSummaryList"]
            )
        )
    else:
        out["data_table_summary_list"] = []
    return out
