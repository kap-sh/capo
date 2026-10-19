"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppFlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_flow_category_list
    import capo_socialmessaging.types.meta_flow_endpoint_uri
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_json_blob
    import capo_socialmessaging.types.meta_flow_name


class CreateWhatsAppFlowInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to associate with this Flow.</p>"""
    flow_name: "capo_socialmessaging.types.meta_flow_name.MetaFlowName"
    """<p>The name of the Flow. Must be unique within the WhatsApp Business Account.</p>"""
    categories: (
        "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    )
    """<p>The categories that classify the business purpose of the Flow. At least one category is required.</p>"""
    flow_json: NotRequired[
        "capo_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
    ]
    """<p>The Flow JSON definition that describes the screens, components, and logic of the Flow. Maximum size is 10 MB.</p>"""
    publish: NotRequired["bool"]
    """<p>Set to <code>true</code> to publish the Flow immediately after creation. Requires a valid <code>flowJson</code> that passes Meta's validation.</p>"""
    clone_flow_id: NotRequired["capo_socialmessaging.types.meta_flow_id.MetaFlowId"]
    """<p>The ID of an existing Flow within the same WhatsApp Business Account to clone.</p>"""
    endpoint_uri: NotRequired[
        "capo_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
    ]
    """<p>The HTTPS endpoint that Meta calls for a data exchange Flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppFlowInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowName"] = value["flow_name"]
    import capo_socialmessaging.types.meta_flow_category_list

    out["categories"] = (
        capo_socialmessaging.types.meta_flow_category_list.serialize_json(
            value["categories"]
        )
    )
    if "flow_json" in value:
        import capo_socialmessaging.types.meta_flow_json_blob

        out["flowJson"] = capo_socialmessaging.types.meta_flow_json_blob.serialize_json(
            value["flow_json"]
        )
    if "publish" in value:
        out["publish"] = value["publish"]
    if "clone_flow_id" in value:
        out["cloneFlowId"] = value["clone_flow_id"]
    if "endpoint_uri" in value:
        out["endpointUri"] = value["endpoint_uri"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppFlowInput:
    out: CreateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("categories") is not None:
        import capo_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    if data.get("flowJson") is not None:
        import capo_socialmessaging.types.meta_flow_json_blob

        out["flow_json"] = (
            capo_socialmessaging.types.meta_flow_json_blob.deserialize_json(
                data["flowJson"]
            )
        )
    if data.get("publish") is not None:
        out["publish"] = data["publish"]
    if data.get("cloneFlowId") is not None:
        out["clone_flow_id"] = data["cloneFlowId"]
    if data.get("endpointUri") is not None:
        out["endpoint_uri"] = data["endpointUri"]
    return out
