"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.next_token
    import capo_health.types.organization_tag_list


class DescribeTagsForOrganizationResponse(TypedDict, closed=True):
    tags: NotRequired["capo_health.types.organization_tag_list.OrganizationTagList"]
    """<p>The list of tags associated with Health events across the organization.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsForOrganizationResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_health.types.organization_tag_list

        out["tags"] = capo_health.types.organization_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsForOrganizationResponse:
    out: DescribeTagsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_health.types.organization_tag_list

        out["tags"] = capo_health.types.organization_tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
