"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateWorkloadIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import capo_bedrock_agentcore_control.types.workload_identity_name_type


class UpdateWorkloadIdentityRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity to update.</p>"""
    allowed_resource_oauth2_return_urls: NotRequired[
        "capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"
    ]
    """<p>The new list of allowed OAuth2 return URLs for resources associated with this workload identity. This list replaces the existing list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkloadIdentityRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "allowed_resource_oauth2_return_urls" in value:
        import capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type

        out["allowedResourceOauth2ReturnUrls"] = (
            capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.serialize_json(
                value["allowed_resource_oauth2_return_urls"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkloadIdentityRequest:
    out: UpdateWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("allowedResourceOauth2ReturnUrls") is not None:
        import capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type

        out["allowed_resource_oauth2_return_urls"] = (
            capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.deserialize_json(
                data["allowedResourceOauth2ReturnUrls"]
            )
        )
    return out
