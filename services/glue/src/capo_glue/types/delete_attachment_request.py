"""Generated from Smithy shape ``com.amazonaws.glue#DeleteAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.attachment_name
    import capo_glue.types.item_identifier
    import capo_glue.types.iterable_form_name


class DeleteAttachmentRequest(TypedDict, closed=True):
    asset_identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset from which to delete the attachment.</p>"""
    iterable_form_name: NotRequired[
        "capo_glue.types.iterable_form_name.IterableFormName"
    ]
    """<p>The name of the iterable form. When specified along with <code>itemIdentifier</code>, the attachment is deleted from an item within the iterable form rather than from the asset itself.</p>"""
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item within the iterable form. Required when <code>iterableFormName</code> is specified.</p>"""
    attachment_name: "capo_glue.types.attachment_name.AttachmentName"
    """<p>The name of the attachment to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAttachmentRequest) -> dict:
    out: dict = {}
    out["AssetIdentifier"] = value["asset_identifier"]
    if "iterable_form_name" in value:
        out["IterableFormName"] = value["iterable_form_name"]
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    out["AttachmentName"] = value["attachment_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAttachmentRequest:
    out: DeleteAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    else:
        out["asset_identifier"] = ""
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    if data.get("ItemIdentifier") is not None:
        out["item_identifier"] = data["ItemIdentifier"]
    if data.get("AttachmentName") is not None:
        out["attachment_name"] = data["AttachmentName"]
    else:
        out["attachment_name"] = ""
    return out
