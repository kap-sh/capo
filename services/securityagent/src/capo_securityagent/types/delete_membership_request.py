"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.application_id
    import capo_securityagent.types.membership_id
    import capo_securityagent.types.membership_type


class DeleteMembershipRequest(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application that contains the agent space.</p>"""
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to revoke access from.</p>"""
    membership_id: "capo_securityagent.types.membership_id.MembershipId"
    """<p>The unique identifier of the membership to delete.</p>"""
    member_type: NotRequired["capo_securityagent.types.membership_type.MembershipType"]
    """<p>The type of member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMembershipRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["membershipId"] = value["membership_id"]
    if "member_type" in value:
        import capo_securityagent.types.membership_type

        out["memberType"] = capo_securityagent.types.membership_type.serialize_json(
            value["member_type"]
        )
    return out


def deserialize_json(data: dict) -> DeleteMembershipRequest:
    out: DeleteMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("memberType") is not None:
        import capo_securityagent.types.membership_type

        out["member_type"] = capo_securityagent.types.membership_type.deserialize_json(
            data["memberType"]
        )
    return out
