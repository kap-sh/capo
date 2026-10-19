"""Generated from Smithy shape ``com.amazonaws.glue#PutAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.attachment_name
    import capo_glue.types.form_content
    import capo_glue.types.form_type_id
    import capo_glue.types.hash_string
    import capo_glue.types.item_identifier
    import capo_glue.types.iterable_form_name


class PutAttachmentRequest(TypedDict, closed=True):
    asset_identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset to attach the form to.</p>"""
    iterable_form_name: NotRequired[
        "capo_glue.types.iterable_form_name.IterableFormName"
    ]
    """<p>The name of the iterable form. When specified along with <code>itemIdentifier</code>, the attachment targets an item within the iterable form rather than the asset itself.</p>"""
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item within the iterable form. Required when <code>iterableFormName</code> is specified.</p>"""
    attachment_name: "capo_glue.types.attachment_name.AttachmentName"
    """<p>The name of the attachment.</p>"""
    content: "capo_glue.types.form_content.FormContent"
    """<p>The JSON content of the form, conforming to the schema of the specified form type.</p>"""
    form_type_id: "capo_glue.types.form_type_id.FormTypeId"
    """<p>The identifier of the form type for this attachment.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAttachmentRequest) -> dict:
    out: dict = {}
    out["AssetIdentifier"] = value["asset_identifier"]
    if "iterable_form_name" in value:
        out["IterableFormName"] = value["iterable_form_name"]
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    out["AttachmentName"] = value["attachment_name"]
    out["Content"] = value["content"]
    out["FormTypeId"] = value["form_type_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAttachmentRequest:
    out: PutAttachmentRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("FormTypeId") is not None:
        out["form_type_id"] = data["FormTypeId"]
    else:
        out["form_type_id"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
