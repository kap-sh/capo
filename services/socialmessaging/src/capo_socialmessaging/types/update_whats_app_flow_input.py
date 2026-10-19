"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppFlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_flow_application_id
    import capo_socialmessaging.types.meta_flow_category_list
    import capo_socialmessaging.types.meta_flow_endpoint_uri
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_name


class UpdateWhatsAppFlowInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to update.</p>"""
    flow_name: NotRequired["capo_socialmessaging.types.meta_flow_name.MetaFlowName"]
    """<p>The updated name for the Flow.</p>"""
    categories: NotRequired[
        "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    ]
    """<p>The updated categories for the Flow.</p>"""
    endpoint_uri: NotRequired[
        "capo_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
    ]
    """<p>The updated HTTPS endpoint for a data exchange Flow.</p>"""
    meta_app_id: NotRequired[
        "capo_socialmessaging.types.meta_flow_application_id.MetaFlowApplicationId"
    ]
    """<p>The ID of the Meta application to attach to the Flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppFlowInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    if "flow_name" in value:
        out["flowName"] = value["flow_name"]
    if "categories" in value:
        import capo_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.serialize_json(
                value["categories"]
            )
        )
    if "endpoint_uri" in value:
        out["endpointUri"] = value["endpoint_uri"]
    if "meta_app_id" in value:
        out["metaAppId"] = value["meta_app_id"]
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppFlowInput:
    out: UpdateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    if data.get("categories") is not None:
        import capo_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["categories"]
            )
        )
    if data.get("endpointUri") is not None:
        out["endpoint_uri"] = data["endpointUri"]
    if data.get("metaAppId") is not None:
        out["meta_app_id"] = data["metaAppId"]
    return out
