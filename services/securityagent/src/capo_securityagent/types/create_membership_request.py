"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.application_id
    import capo_securityagent.types.membership_config
    import capo_securityagent.types.membership_id
    import capo_securityagent.types.membership_type


class CreateMembershipRequest(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application that contains the agent space.</p>"""
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to grant access to.</p>"""
    membership_id: "capo_securityagent.types.membership_id.MembershipId"
    """<p>The unique identifier for the membership.</p>"""
    member_type: "capo_securityagent.types.membership_type.MembershipType"
    """<p>The type of member. Currently, only USER is supported.</p>"""
    config: NotRequired["capo_securityagent.types.membership_config.MembershipConfig"]
    """<p>The configuration for the membership, such as the user role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["membershipId"] = value["membership_id"]
    import capo_securityagent.types.membership_type

    out["memberType"] = capo_securityagent.types.membership_type.serialize_json(
        value["member_type"]
    )
    if "config" in value:
        import capo_securityagent.types.membership_config

        out["config"] = capo_securityagent.types.membership_config.serialize_json(
            value["config"]
        )
    return out


def deserialize_json(data: dict) -> CreateMembershipRequest:
    out: CreateMembershipRequest = {}  # type: ignore[typeddict-item]
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
    else:
        import typing

        out["member_type"] = typing.cast(
            "capo_securityagent.types.membership_type.MembershipType", ""
        )
    if data.get("config") is not None:
        import capo_securityagent.types.membership_config

        out["config"] = capo_securityagent.types.membership_config.deserialize_json(
            data["config"]
        )
    return out
