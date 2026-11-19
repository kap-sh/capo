"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.next_token
    import capo_keyspaces.types.table_summary_list


class ListTablesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_keyspaces.types.next_token.NextToken"]
    """<p>A token to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response.</p>"""
    tables: NotRequired["capo_keyspaces.types.table_summary_list.TableSummaryList"]
    """<p>A list of tables.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTablesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tables" in value:
        import capo_keyspaces.types.table_summary_list

        out["tables"] = capo_keyspaces.types.table_summary_list.serialize_aws_json_1_0(
            value["tables"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("tables") is not None:
        import capo_keyspaces.types.table_summary_list

        out["tables"] = (
            capo_keyspaces.types.table_summary_list.deserialize_aws_json_1_0(
                data["tables"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTablesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tables" in value:
        import capo_keyspaces.types.table_summary_list

        out["tables"] = capo_keyspaces.types.table_summary_list.serialize_cbor(
            value["tables"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("tables") is not None:
        import capo_keyspaces.types.table_summary_list

        out["tables"] = capo_keyspaces.types.table_summary_list.deserialize_cbor(
            data["tables"]
        )
    return out
