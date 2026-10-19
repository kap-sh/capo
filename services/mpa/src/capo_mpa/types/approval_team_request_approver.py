"""Generated from Smithy shape ``com.amazonaws.mpa#ApprovalTeamRequestApprover``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.identity_id
    import capo_mpa.types.string


class ApprovalTeamRequestApprover(TypedDict, closed=True):
    primary_identity_id: "capo_mpa.types.identity_id.IdentityId"
    """<p>ID for the user.</p>"""
    primary_identity_source_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalTeamRequestApprover) -> dict:
    out: dict = {}
    out["PrimaryIdentityId"] = value["primary_identity_id"]
    out["PrimaryIdentitySourceArn"] = value["primary_identity_source_arn"]
    return out


def deserialize_json(data: dict) -> ApprovalTeamRequestApprover:
    out: ApprovalTeamRequestApprover = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryIdentityId") is not None:
        out["primary_identity_id"] = data["PrimaryIdentityId"]
    else:
        out["primary_identity_id"] = ""
    if data.get("PrimaryIdentitySourceArn") is not None:
        out["primary_identity_source_arn"] = data["PrimaryIdentitySourceArn"]
    else:
        out["primary_identity_source_arn"] = ""
    return out
