"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImagePipelineImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImagePipelineImagesRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline whose images you want to view.</p> <p>If the ARN that you specify doesn't exist, Image Builder returns an empty list rather than a <code>ResourceNotFoundException</code> error.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request. If you don't specify a value, Image Builder returns up to 25 items. The largest page size that you can request is 100 items. A page can contain fewer items than the maximum, with a <code>nextToken</code> to continue paging.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImagePipelineImagesRequest) -> dict:
    out: dict = {}
    out["imagePipelineArn"] = value["image_pipeline_arn"]
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


def deserialize_json(data: dict) -> ListImagePipelineImagesRequest:
    out: ListImagePipelineImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("imagePipelineArn") is not None:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    else:
        out["image_pipeline_arn"] = ""
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
