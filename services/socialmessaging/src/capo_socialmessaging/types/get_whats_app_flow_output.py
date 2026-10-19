"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppFlowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_application_info
    import capo_socialmessaging.types.meta_flow_category_list
    import capo_socialmessaging.types.meta_flow_data_api_version
    import capo_socialmessaging.types.meta_flow_endpoint_uri
    import capo_socialmessaging.types.meta_flow_health_status
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.meta_flow_json_version
    import capo_socialmessaging.types.meta_flow_name
    import capo_socialmessaging.types.meta_flow_preview_info
    import capo_socialmessaging.types.meta_flow_status
    import capo_socialmessaging.types.meta_flow_whats_app_business_account_info
    import capo_socialmessaging.types.validation_error_list


class GetWhatsAppFlowOutput(TypedDict, closed=True):
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow.</p>"""
    flow_name: "capo_socialmessaging.types.meta_flow_name.MetaFlowName"
    """<p>The name of the Flow.</p>"""
    flow_status: "capo_socialmessaging.types.meta_flow_status.MetaFlowStatus"
    """<p>The lifecycle status of the Flow. Valid values are DRAFT, PUBLISHED, DEPRECATED, BLOCKED, and THROTTLED.</p>"""
    categories: NotRequired[
        "capo_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    ]
    """<p>The categories that classify the business purpose of the Flow.</p>"""
    validation_errors: NotRequired[
        "capo_socialmessaging.types.validation_error_list.ValidationErrorList"
    ]
    """<p>A list of validation errors from Meta, if any.</p>"""
    json_version: NotRequired[
        "capo_socialmessaging.types.meta_flow_json_version.MetaFlowJsonVersion"
    ]
    """<p>The version of the Flow JSON schema used by this Flow (for example, 7.3).</p>"""
    data_api_version: NotRequired[
        "capo_socialmessaging.types.meta_flow_data_api_version.MetaFlowDataApiVersion"
    ]
    """<p>The data API version for data exchange endpoint Flows.</p>"""
    endpoint_uri: NotRequired[
        "capo_socialmessaging.types.meta_flow_endpoint_uri.MetaFlowEndpointUri"
    ]
    """<p>The HTTPS endpoint that Meta calls for a data exchange Flow.</p>"""
    preview: NotRequired[
        "capo_socialmessaging.types.meta_flow_preview_info.MetaFlowPreviewInfo"
    ]
    """<p>The preview URL and its expiration timestamp for testing the Flow.</p>"""
    whats_app_business_account: NotRequired[
        "capo_socialmessaging.types.meta_flow_whats_app_business_account_info.MetaFlowWhatsAppBusinessAccountInfo"
    ]
    """<p>The WhatsApp Business Account information from Meta associated with this Flow.</p>"""
    application: NotRequired[
        "capo_socialmessaging.types.meta_flow_application_info.MetaFlowApplicationInfo"
    ]
    """<p>The Meta application information associated with this Flow.</p>"""
    health_status: NotRequired[
        "capo_socialmessaging.types.meta_flow_health_status.MetaFlowHealthStatus"
    ]
    """<p>The health status information for this Flow from Meta.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppFlowOutput) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    out["flowName"] = value["flow_name"]
    out["flowStatus"] = value["flow_status"]
    if "categories" in value:
        import capo_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.serialize_json(
                value["categories"]
            )
        )
    if "validation_errors" in value:
        import capo_socialmessaging.types.validation_error_list

        out["validationErrors"] = (
            capo_socialmessaging.types.validation_error_list.serialize_json(
                value["validation_errors"]
            )
        )
    if "json_version" in value:
        out["jsonVersion"] = value["json_version"]
    if "data_api_version" in value:
        out["dataApiVersion"] = value["data_api_version"]
    if "endpoint_uri" in value:
        out["endpointUri"] = value["endpoint_uri"]
    if "preview" in value:
        import capo_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            capo_socialmessaging.types.meta_flow_preview_info.serialize_json(
                value["preview"]
            )
        )
    if "whats_app_business_account" in value:
        import capo_socialmessaging.types.meta_flow_whats_app_business_account_info

        out["whatsAppBusinessAccount"] = (
            capo_socialmessaging.types.meta_flow_whats_app_business_account_info.serialize_json(
                value["whats_app_business_account"]
            )
        )
    if "application" in value:
        import capo_socialmessaging.types.meta_flow_application_info

        out["application"] = (
            capo_socialmessaging.types.meta_flow_application_info.serialize_json(
                value["application"]
            )
        )
    if "health_status" in value:
        import capo_socialmessaging.types.meta_flow_health_status

        out["healthStatus"] = (
            capo_socialmessaging.types.meta_flow_health_status.serialize_json(
                value["health_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWhatsAppFlowOutput:
    out: GetWhatsAppFlowOutput = {}  # type: ignore[typeddict-item]
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("flowStatus") is not None:
        out["flow_status"] = data["flowStatus"]
    else:
        out["flow_status"] = ""
    if data.get("categories") is not None:
        import capo_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            capo_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["categories"]
            )
        )
    if data.get("validationErrors") is not None:
        import capo_socialmessaging.types.validation_error_list

        out["validation_errors"] = (
            capo_socialmessaging.types.validation_error_list.deserialize_json(
                data["validationErrors"]
            )
        )
    if data.get("jsonVersion") is not None:
        out["json_version"] = data["jsonVersion"]
    if data.get("dataApiVersion") is not None:
        out["data_api_version"] = data["dataApiVersion"]
    if data.get("endpointUri") is not None:
        out["endpoint_uri"] = data["endpointUri"]
    if data.get("preview") is not None:
        import capo_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            capo_socialmessaging.types.meta_flow_preview_info.deserialize_json(
                data["preview"]
            )
        )
    if data.get("whatsAppBusinessAccount") is not None:
        import capo_socialmessaging.types.meta_flow_whats_app_business_account_info

        out["whats_app_business_account"] = (
            capo_socialmessaging.types.meta_flow_whats_app_business_account_info.deserialize_json(
                data["whatsAppBusinessAccount"]
            )
        )
    if data.get("application") is not None:
        import capo_socialmessaging.types.meta_flow_application_info

        out["application"] = (
            capo_socialmessaging.types.meta_flow_application_info.deserialize_json(
                data["application"]
            )
        )
    if data.get("healthStatus") is not None:
        import capo_socialmessaging.types.meta_flow_health_status

        out["health_status"] = (
            capo_socialmessaging.types.meta_flow_health_status.deserialize_json(
                data["healthStatus"]
            )
        )
    return out
