"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListSchemasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.schema_summary_list


class ListSchemasOutput(TypedDict, closed=True):
    schema_summaries: "capo_cleanrooms.types.schema_summary_list.SchemaSummaryList"
    """<p>The retrieved list of schemas.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemasOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_summary_list

    out["schemaSummaries"] = capo_cleanrooms.types.schema_summary_list.serialize_json(
        value["schema_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchemasOutput:
    out: ListSchemasOutput = {}  # type: ignore[typeddict-item]
    if data.get("schemaSummaries") is not None:
        import capo_cleanrooms.types.schema_summary_list

        out["schema_summaries"] = (
            capo_cleanrooms.types.schema_summary_list.deserialize_json(
                data["schemaSummaries"]
            )
        )
    else:
        out["schema_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
