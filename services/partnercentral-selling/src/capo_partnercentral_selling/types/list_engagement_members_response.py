"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementMembersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_members


class ListEngagementMembersResponse(TypedDict, closed=True):
    engagement_member_list: (
        "capo_partnercentral_selling.types.engagement_members.EngagementMembers"
    )
    """<p> Provides a list of engagement members. </p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results. If there are more results available than can be returned in a single response, this token will be present. Use this token in a subsequent request to retrieve the next page of results. If there are no more results, this value will be null. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementMembersResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.engagement_members

    out["EngagementMemberList"] = (
        capo_partnercentral_selling.types.engagement_members.serialize_aws_json_1_0(
            value["engagement_member_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementMembersResponse:
    out: ListEngagementMembersResponse = {}  # type: ignore[typeddict-item]
    if data.get("EngagementMemberList") is not None:
        import capo_partnercentral_selling.types.engagement_members

        out["engagement_member_list"] = (
            capo_partnercentral_selling.types.engagement_members.deserialize_aws_json_1_0(
                data["EngagementMemberList"]
            )
        )
    else:
        raise DeserializationError(
            "ListEngagementMembersResponse.engagement_member_list required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListEngagementMembersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "engagement_member_list" in value:
        import capo_partnercentral_selling.types.engagement_members

        out["engagement_member_list"] = (
            capo_partnercentral_selling.types.engagement_members.redact_sensitive(
                value["engagement_member_list"]
            )
        )
    return out
