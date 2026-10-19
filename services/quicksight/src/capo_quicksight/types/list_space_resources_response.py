"""Generated from Smithy shape ``com.amazonaws.quicksight#ListSpaceResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.public_space_arn
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_resource_summaries


class ListSpaceResourcesResponse(TypedDict, closed=True):
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["capo_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    space_resources: (
        "capo_quicksight.types.space_resource_summaries.SpaceResourceSummaries"
    )
    """<p>A list of resource summaries in the space.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpaceResourcesResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    import capo_quicksight.types.space_resource_summaries

    out["SpaceResources"] = (
        capo_quicksight.types.space_resource_summaries.serialize_json(
            value["space_resources"]
        )
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListSpaceResourcesResponse:
    out: ListSpaceResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    if data.get("SpaceResources") is not None:
        import capo_quicksight.types.space_resource_summaries

        out["space_resources"] = (
            capo_quicksight.types.space_resource_summaries.deserialize_json(
                data["SpaceResources"]
            )
        )
    else:
        out["space_resources"] = []
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
