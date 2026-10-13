"""Generated from Smithy shape ``com.amazonaws.datazone#ListAccountsInAccountPoolOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_info_list
    import capo_datazone.types.pagination_token


class ListAccountsInAccountPoolOutput(TypedDict, closed=True):
    items: NotRequired["capo_datazone.types.account_info_list.AccountInfoList"]
    """<p>The results of the ListAccountsInAccountPool operation.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountsInAccountPoolOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.account_info_list

        out["items"] = capo_datazone.types.account_info_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountsInAccountPoolOutput:
    out: ListAccountsInAccountPoolOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.account_info_list

        out["items"] = capo_datazone.types.account_info_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAccountsInAccountPoolOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.account_info_list

        out["items"] = capo_datazone.types.account_info_list.redact_sensitive(
            value["items"]
        )
    return out
