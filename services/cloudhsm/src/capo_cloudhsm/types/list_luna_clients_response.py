"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListLunaClientsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.client_list
    import capo_cloudhsm.types.pagination_token


class ListLunaClientsResponse(TypedDict, closed=True):
    client_list: "capo_cloudhsm.types.client_list.ClientList"
    """<p>The list of clients.</p>"""
    next_token: NotRequired["capo_cloudhsm.types.pagination_token.PaginationToken"]
    """<p>If not null, more results are available. Pass this to <code>ListLunaClients</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLunaClientsResponse) -> dict:
    out: dict = {}
    import capo_cloudhsm.types.client_list

    out["ClientList"] = capo_cloudhsm.types.client_list.serialize_aws_json_1_1(
        value["client_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLunaClientsResponse:
    out: ListLunaClientsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ClientList") is not None:
        import capo_cloudhsm.types.client_list

        out["client_list"] = capo_cloudhsm.types.client_list.deserialize_aws_json_1_1(
            data["ClientList"]
        )
    else:
        out["client_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
