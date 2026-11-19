"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectClientAddInsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.connect_client_add_in_list
    import capo_workspaces.types.pagination_token


class DescribeConnectClientAddInsResult(TypedDict, closed=True):
    add_ins: NotRequired[
        "capo_workspaces.types.connect_client_add_in_list.ConnectClientAddInList"
    ]
    """<p>Information about client add-ins.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectClientAddInsResult) -> dict:
    out: dict = {}
    if "add_ins" in value:
        import capo_workspaces.types.connect_client_add_in_list

        out["AddIns"] = (
            capo_workspaces.types.connect_client_add_in_list.serialize_aws_json_1_1(
                value["add_ins"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectClientAddInsResult:
    out: DescribeConnectClientAddInsResult = {}  # type: ignore[typeddict-item]
    if data.get("AddIns") is not None:
        import capo_workspaces.types.connect_client_add_in_list

        out["add_ins"] = (
            capo_workspaces.types.connect_client_add_in_list.deserialize_aws_json_1_1(
                data["AddIns"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeConnectClientAddInsResult) -> dict:
    out: dict = {}
    if "add_ins" in value:
        import capo_workspaces.types.connect_client_add_in_list

        out["AddIns"] = capo_workspaces.types.connect_client_add_in_list.serialize_cbor(
            value["add_ins"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeConnectClientAddInsResult:
    out: DescribeConnectClientAddInsResult = {}  # type: ignore[typeddict-item]
    if data.get("AddIns") is not None:
        import capo_workspaces.types.connect_client_add_in_list

        out["add_ins"] = (
            capo_workspaces.types.connect_client_add_in_list.deserialize_cbor(
                data["AddIns"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
