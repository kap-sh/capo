"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.container_provider
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.security_configuration_data
    import capo_emr_containers.types.tag_map


class CreateSecurityConfigurationRequest(TypedDict, closed=True):
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>The client idempotency token to use when creating the security configuration.</p>"""
    name: "capo_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The name of the security configuration.</p>"""
    container_provider: NotRequired[
        "capo_emr_containers.types.container_provider.ContainerProvider"
    ]
    """<p>The container provider associated with the security configuration.</p>"""
    security_configuration_data: "capo_emr_containers.types.security_configuration_data.SecurityConfigurationData"
    """<p>Security configuration input for the request.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags to add to the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityConfigurationRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "container_provider" in value:
        import capo_emr_containers.types.container_provider

        out["containerProvider"] = (
            capo_emr_containers.types.container_provider.serialize_json(
                value["container_provider"]
            )
        )
    import capo_emr_containers.types.security_configuration_data

    out["securityConfigurationData"] = (
        capo_emr_containers.types.security_configuration_data.serialize_json(
            value["security_configuration_data"]
        )
    )
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSecurityConfigurationRequest:
    out: CreateSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("containerProvider") is not None:
        import capo_emr_containers.types.container_provider

        out["container_provider"] = (
            capo_emr_containers.types.container_provider.deserialize_json(
                data["containerProvider"]
            )
        )
    if data.get("securityConfigurationData") is not None:
        import capo_emr_containers.types.security_configuration_data

        out["security_configuration_data"] = (
            capo_emr_containers.types.security_configuration_data.deserialize_json(
                data["securityConfigurationData"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSecurityConfigurationRequest.security_configuration_data required"
        )
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    return out
