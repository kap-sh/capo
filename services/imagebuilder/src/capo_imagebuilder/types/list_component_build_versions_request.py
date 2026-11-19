"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListComponentBuildVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_version_arn
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListComponentBuildVersionsRequest(TypedDict, closed=True):
    component_version_arn: NotRequired[
        "capo_imagebuilder.types.component_version_arn.ComponentVersionArn"
    ]
    """<p>The component version ARN whose build versions you want to list. The ARN must specify an exact version, without a build number suffix. If you don't specify an ARN, Image Builder returns build versions for the components that your account owns.</p> <p>If the ARN that you specify doesn't exist, Image Builder returns an empty list rather than a <code>ResourceNotFoundException</code> error.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request. If you don't specify a value, Image Builder returns up to 25 items. The largest page size that you can request is 100 items. A page can contain fewer items than the maximum, with a <code>nextToken</code> to continue paging.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentBuildVersionsRequest) -> dict:
    out: dict = {}
    if "component_version_arn" in value:
        out["componentVersionArn"] = value["component_version_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentBuildVersionsRequest:
    out: ListComponentBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("componentVersionArn") is not None:
        out["component_version_arn"] = data["componentVersionArn"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
