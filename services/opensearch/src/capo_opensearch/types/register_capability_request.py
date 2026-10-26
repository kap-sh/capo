"""Generated from Smithy shape ``com.amazonaws.opensearch#RegisterCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.capability_base_request_config
    import capo_opensearch.types.capability_name


class RegisterCapabilityRequest(TypedDict, closed=True):
    application_id: "capo_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch UI application to register the capability for.</p>"""
    capability_name: "capo_opensearch.types.capability_name.CapabilityName"
    """<p>The name of the capability to register. Must be between 3 and 30 characters and contain only alphanumeric characters and hyphens. This identifies the type of capability being enabled for the application. For registering AI Assistant capability, use <code>ai-capability</code> </p>"""
    capability_config: "capo_opensearch.types.capability_base_request_config.CapabilityBaseRequestConfig"
    """<p>The configuration settings for the capability being registered. This includes capability-specific settings such as AI configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCapabilityRequest) -> dict:
    out: dict = {}
    out["capabilityName"] = value["capability_name"]
    import capo_opensearch.types.capability_base_request_config

    out["capabilityConfig"] = (
        capo_opensearch.types.capability_base_request_config.serialize_json(
            value["capability_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisterCapabilityRequest:
    out: RegisterCapabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilityName") is not None:
        out["capability_name"] = data["capabilityName"]
    else:
        out["capability_name"] = ""
    if data.get("capabilityConfig") is not None:
        import capo_opensearch.types.capability_base_request_config

        out["capability_config"] = (
            capo_opensearch.types.capability_base_request_config.deserialize_json(
                data["capabilityConfig"]
            )
        )
    else:
        out["capability_config"] = {"$unknown": {"name": ""}}
    return out
