"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateSpaceResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.failed_space_resource_operations
    import capo_quicksight.types.public_space_arn
    import capo_quicksight.types.public_space_id


class UpdateSpaceResourcesResponse(TypedDict, closed=True):
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["capo_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    failed_resource_operations: NotRequired[
        "capo_quicksight.types.failed_space_resource_operations.FailedSpaceResourceOperations"
    ]
    """<p>A list of resource operations that failed.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceResourcesResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    if "failed_resource_operations" in value:
        import capo_quicksight.types.failed_space_resource_operations

        out["FailedResourceOperations"] = (
            capo_quicksight.types.failed_space_resource_operations.serialize_json(
                value["failed_resource_operations"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceResourcesResponse:
    out: UpdateSpaceResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    if data.get("FailedResourceOperations") is not None:
        import capo_quicksight.types.failed_space_resource_operations

        out["failed_resource_operations"] = (
            capo_quicksight.types.failed_space_resource_operations.deserialize_json(
                data["FailedResourceOperations"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
