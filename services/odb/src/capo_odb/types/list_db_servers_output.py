"""Generated from Smithy shape ``com.amazonaws.odb#ListDbServersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_server_list


class ListDbServersOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    db_servers: "capo_odb.types.db_server_list.DbServerList"
    """<p>The list of database servers along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbServersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.db_server_list

    out["dbServers"] = capo_odb.types.db_server_list.serialize_aws_json_1_0(
        value["db_servers"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbServersOutput:
    out: ListDbServersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("dbServers") is not None:
        import capo_odb.types.db_server_list

        out["db_servers"] = capo_odb.types.db_server_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    else:
        out["db_servers"] = []
    return out
