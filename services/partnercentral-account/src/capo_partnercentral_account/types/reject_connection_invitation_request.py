"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#RejectConnectionInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.connection_invitation_id


class RejectConnectionInvitationRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation exists.</p>"""
    identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the connection invitation to reject.</p>"""
    client_token: "capo_partnercentral_account.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    reason: NotRequired["str"]
    """<p>The reason for rejecting the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectConnectionInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    out["ClientToken"] = value["client_token"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectConnectionInvitationRequest:
    out: RejectConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
