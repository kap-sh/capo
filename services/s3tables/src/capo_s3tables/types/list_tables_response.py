"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_summary_list


class ListTablesResponse(TypedDict, closed=True):
    tables: "capo_s3tables.types.table_summary_list.TableSummaryList"
    """<p>A list of tables.</p>"""
    continuation_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p>You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTablesResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.table_summary_list

    out["tables"] = capo_s3tables.types.table_summary_list.serialize_json(
        value["tables"]
    )
    if "continuation_token" in value:
        out["continuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if data.get("tables") is not None:
        import capo_s3tables.types.table_summary_list

        out["tables"] = capo_s3tables.types.table_summary_list.deserialize_json(
            data["tables"]
        )
    else:
        out["tables"] = []
    if data.get("continuationToken") is not None:
        out["continuation_token"] = data["continuationToken"]
    return out
