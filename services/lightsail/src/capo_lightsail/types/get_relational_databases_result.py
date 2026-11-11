"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabasesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_list
    import capo_lightsail.types.string


class GetRelationalDatabasesResult(TypedDict, closed=True):
    relational_databases: NotRequired[
        "capo_lightsail.types.relational_database_list.RelationalDatabaseList"
    ]
    """<p>An object describing the result of your get relational databases request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabases</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabasesResult) -> dict:
    out: dict = {}
    if "relational_databases" in value:
        import capo_lightsail.types.relational_database_list

        out["relationalDatabases"] = (
            capo_lightsail.types.relational_database_list.serialize_aws_json_1_1(
                value["relational_databases"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabasesResult:
    out: GetRelationalDatabasesResult = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabases") is not None:
        import capo_lightsail.types.relational_database_list

        out["relational_databases"] = (
            capo_lightsail.types.relational_database_list.deserialize_aws_json_1_1(
                data["relationalDatabases"]
            )
        )
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    return out


def redact_sensitive(value: GetRelationalDatabasesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "relational_databases" in value:
        import capo_lightsail.types.relational_database_list

        out["relational_databases"] = (
            capo_lightsail.types.relational_database_list.redact_sensitive(
                value["relational_databases"]
            )
        )
    return out
