"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateVirtualClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.boolean
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.container_provider
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.scheduler_configuration
    import capo_emr_containers.types.tag_map


class CreateVirtualClusterRequest(TypedDict, closed=True):
    name: "capo_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The specified name of the virtual cluster.</p>"""
    container_provider: "capo_emr_containers.types.container_provider.ContainerProvider"
    """<p>The container provider of the virtual cluster.</p>"""
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>The client token of the virtual cluster.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to the virtual cluster.</p>"""
    security_configuration_id: NotRequired[
        "capo_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The ID of the security configuration.</p>"""
    session_enabled: NotRequired["capo_emr_containers.types.boolean.Boolean"]
    """<p>Indicates whether the virtual cluster has session support enabled.</p>"""
    scheduler_configuration: NotRequired[
        "capo_emr_containers.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration (concurrency and queue limits) to apply to the virtual cluster at creation time. When omitted, no limits are applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualClusterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_emr_containers.types.container_provider

    out["containerProvider"] = (
        capo_emr_containers.types.container_provider.serialize_json(
            value["container_provider"]
        )
    )
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "security_configuration_id" in value:
        out["securityConfigurationId"] = value["security_configuration_id"]
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    if "scheduler_configuration" in value:
        import capo_emr_containers.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            capo_emr_containers.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVirtualClusterRequest:
    out: CreateVirtualClusterRequest = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError(
            "CreateVirtualClusterRequest.container_provider required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("securityConfigurationId") is not None:
        out["security_configuration_id"] = data["securityConfigurationId"]
    if data.get("sessionEnabled") is not None:
        out["session_enabled"] = data["sessionEnabled"]
    if data.get("schedulerConfiguration") is not None:
        import capo_emr_containers.types.scheduler_configuration

        out["scheduler_configuration"] = (
            capo_emr_containers.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    return out
