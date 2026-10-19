"""Generated from Smithy shape ``com.amazonaws.securityagent#ListMembershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.application_id
    import capo_securityagent.types.max_results
    import capo_securityagent.types.membership_type_filter
    import capo_securityagent.types.next_token


class ListMembershipsRequest(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application that contains the agent space.</p>"""
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to list memberships for.</p>"""
    member_type: NotRequired[
        "capo_securityagent.types.membership_type_filter.MembershipTypeFilter"
    ]
    """<p>Filter memberships by member type.</p>"""
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "member_type" in value:
        import capo_securityagent.types.membership_type_filter

        out["memberType"] = (
            capo_securityagent.types.membership_type_filter.serialize_json(
                value["member_type"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembershipsRequest:
    out: ListMembershipsRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("memberType") is not None:
        import capo_securityagent.types.membership_type_filter

        out["member_type"] = (
            capo_securityagent.types.membership_type_filter.deserialize_json(
                data["memberType"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
