"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageBuildVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.image_version_arn
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImageBuildVersionsRequest(TypedDict, closed=True):
    image_version_arn: NotRequired[
        "capo_imagebuilder.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image version whose build versions you want to retrieve. The ARN must specify an exact version (<code><major>.<minor>.<patch></code>) - wildcards aren't allowed. This parameter is optional. If you don't specify it, Image Builder returns build versions for all of the images in your account.</p> <p>If the ARN that you specify doesn't exist, Image Builder returns an empty list rather than a <code>ResourceNotFoundException</code> error.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>osVersion</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request. If you don't specify a value, Image Builder returns up to 25 items. The largest page size that you can request is 100 items. A page can contain fewer items than the maximum, with a <code>nextToken</code> to continue paging.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageBuildVersionsRequest) -> dict:
    out: dict = {}
    if "image_version_arn" in value:
        out["imageVersionArn"] = value["image_version_arn"]
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageBuildVersionsRequest:
    out: ListImageBuildVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("imageVersionArn") is not None:
        out["image_version_arn"] = data["imageVersionArn"]
    if data.get("filters") is not None:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
