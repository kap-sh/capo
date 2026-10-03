"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageScanFindingAggregationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_scan_finding_aggregations_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token


class ListImageScanFindingAggregationsResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    aggregation_type: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The aggregation type specifies what type of key is used to group the image scan findings. Image Builder returns results based on the request filter. If you didn't specify a filter in the request, the type defaults to <code>accountId</code>.</p> <p class="title"> <b>Aggregation types</b> </p> <ul> <li> <p>accountId</p> </li> <li> <p>imageBuildVersionArn</p> </li> <li> <p>imagePipelineArn</p> </li> <li> <p>vulnerabilityId</p> </li> </ul> <p>Each aggregation includes counts by severity level for medium severity and higher level findings, plus a total for all of the findings for each key value.</p>"""
    responses: NotRequired[
        "capo_imagebuilder.types.image_scan_finding_aggregations_list.ImageScanFindingAggregationsList"
    ]
    """<p>An array of image scan finding aggregations that match the filter criteria.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageScanFindingAggregationsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "aggregation_type" in value:
        out["aggregationType"] = value["aggregation_type"]
    if "responses" in value:
        import capo_imagebuilder.types.image_scan_finding_aggregations_list

        out["responses"] = (
            capo_imagebuilder.types.image_scan_finding_aggregations_list.serialize_json(
                value["responses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageScanFindingAggregationsResponse:
    out: ListImageScanFindingAggregationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("aggregationType") is not None:
        out["aggregation_type"] = data["aggregationType"]
    if data.get("responses") is not None:
        import capo_imagebuilder.types.image_scan_finding_aggregations_list

        out["responses"] = (
            capo_imagebuilder.types.image_scan_finding_aggregations_list.deserialize_json(
                data["responses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
