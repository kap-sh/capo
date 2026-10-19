"""Generated from Smithy shape ``com.amazonaws.fms#BatchAssociateResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.failed_item_list
    import capo_fms.types.identifier


class BatchAssociateResourceResponse(TypedDict, closed=True):
    resource_set_identifier: "capo_fms.types.identifier.Identifier"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""
    failed_items: "capo_fms.types.failed_item_list.FailedItemList"
    """<p>The resources that failed to associate to the resource set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateResourceResponse) -> dict:
    out: dict = {}
    out["ResourceSetIdentifier"] = value["resource_set_identifier"]
    import capo_fms.types.failed_item_list

    out["FailedItems"] = capo_fms.types.failed_item_list.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateResourceResponse:
    out: BatchAssociateResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceSetIdentifier") is not None:
        out["resource_set_identifier"] = data["ResourceSetIdentifier"]
    else:
        out["resource_set_identifier"] = ""
    if data.get("FailedItems") is not None:
        import capo_fms.types.failed_item_list

        out["failed_items"] = capo_fms.types.failed_item_list.deserialize_aws_json_1_1(
            data["FailedItems"]
        )
    else:
        out["failed_items"] = []
    return out
