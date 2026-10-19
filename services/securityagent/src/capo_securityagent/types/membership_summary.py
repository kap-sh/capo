"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.application_id
    import capo_securityagent.types.member_metadata
    import capo_securityagent.types.membership_config
    import capo_securityagent.types.membership_id
    import capo_securityagent.types.membership_type


class MembershipSummary(TypedDict, closed=True):
    membership_id: "capo_securityagent.types.membership_id.MembershipId"
    """<p>The unique identifier of the membership.</p>"""
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application.</p>"""
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space.</p>"""
    member_type: "capo_securityagent.types.membership_type.MembershipType"
    """<p>The type of member.</p>"""
    config: NotRequired["capo_securityagent.types.membership_config.MembershipConfig"]
    """<p>The configuration for the membership.</p>"""
    metadata: NotRequired["capo_securityagent.types.member_metadata.MemberMetadata"]
    """<p>The metadata for the member.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the membership was created, in UTC format.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the membership was last updated, in UTC format.</p>"""
    created_by: "str"
    """<p>The identifier of the entity that created the membership.</p>"""
    updated_by: "str"
    """<p>The identifier of the entity that last updated the membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummary) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_securityagent.types.membership_type

    out["memberType"] = capo_securityagent.types.membership_type.serialize_json(
        value["member_type"]
    )
    if "config" in value:
        import capo_securityagent.types.membership_config

        out["config"] = capo_securityagent.types.membership_config.serialize_json(
            value["config"]
        )
    if "metadata" in value:
        import capo_securityagent.types.member_metadata

        out["metadata"] = capo_securityagent.types.member_metadata.serialize_json(
            value["metadata"]
        )
    import capo_securityagent._protocol.serialize

    out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_securityagent._protocol.serialize

    out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    out["createdBy"] = value["created_by"]
    out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> MembershipSummary:
    out: MembershipSummary = {}  # type: ignore[typeddict-item]
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
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
    if data.get("metadata") is not None:
        import capo_securityagent.types.member_metadata

        out["metadata"] = capo_securityagent.types.member_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    else:
        out["updated_by"] = ""
    return out
