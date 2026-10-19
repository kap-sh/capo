"""Generated from Smithy shape ``com.amazonaws.transfer#ListAccessesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_accesses
    import capo_transfer.types.next_token
    import capo_transfer.types.server_id


class ListAccessesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListAccesses</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional accesses.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has users assigned to it.</p>"""
    accesses: "capo_transfer.types.listed_accesses.ListedAccesses"
    """<p>Returns the accesses and their properties for the <code>ServerId</code> value that you specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ServerId"] = value["server_id"]
    import capo_transfer.types.listed_accesses

    out["Accesses"] = capo_transfer.types.listed_accesses.serialize_aws_json_1_1(
        value["accesses"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessesResponse:
    out: ListAccessesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("Accesses") is not None:
        import capo_transfer.types.listed_accesses

        out["accesses"] = capo_transfer.types.listed_accesses.deserialize_aws_json_1_1(
            data["Accesses"]
        )
    else:
        out["accesses"] = []
    return out
