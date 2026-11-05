"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTableMigrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_summary_list
    import capo_s3tables.types.next_token


class ListTableMigrationsResponse(TypedDict, closed=True):
    migrations: "capo_s3tables.types.migration_summary_list.MigrationSummaryList"
    """<p>The migrations, newest first.</p>"""
    next_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p>A token to pass as <code>nextToken</code> to get the next page of results. If there are no more results, this value isn't returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableMigrationsResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.migration_summary_list

    out["migrations"] = capo_s3tables.types.migration_summary_list.serialize_json(
        value["migrations"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTableMigrationsResponse:
    out: ListTableMigrationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("migrations") is not None:
        import capo_s3tables.types.migration_summary_list

        out["migrations"] = capo_s3tables.types.migration_summary_list.deserialize_json(
            data["migrations"]
        )
    else:
        out["migrations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
