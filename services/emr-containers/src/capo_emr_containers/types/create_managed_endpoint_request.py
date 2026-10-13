"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateManagedEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.acm_cert_arn
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.configuration_overrides
    import capo_emr_containers.types.endpoint_type
    import capo_emr_containers.types.iam_role_arn
    import capo_emr_containers.types.release_label
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.session_idle_timeout_in_minutes
    import capo_emr_containers.types.tag_map


class CreateManagedEndpointRequest(TypedDict, closed=True):
    name: "capo_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The name of the managed endpoint.</p>"""
    virtual_cluster_id: "capo_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the virtual cluster for which a managed endpoint is created.</p>"""
    type: "capo_emr_containers.types.endpoint_type.EndpointType"
    """<p>The type of the managed endpoint.</p>"""
    release_label: "capo_emr_containers.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release version.</p>"""
    execution_role_arn: "capo_emr_containers.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the execution role.</p>"""
    certificate_arn: NotRequired["capo_emr_containers.types.acm_cert_arn.ACMCertArn"]
    """<p>The certificate ARN provided by users for the managed endpoint. This field is under deprecation and will be removed in future releases.</p>"""
    configuration_overrides: NotRequired[
        "capo_emr_containers.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration settings that will be used to override existing configurations.</p>"""
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>The client idempotency token for this create call.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags of the managed endpoint. </p>"""
    session_idle_timeout_in_minutes: "capo_emr_containers.types.session_idle_timeout_in_minutes.SessionIdleTimeoutInMinutes"
    """<p>The number of idle minutes before the managed endpoint session times out.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateManagedEndpointRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["releaseLabel"] = value["release_label"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "configuration_overrides" in value:
        import capo_emr_containers.types.configuration_overrides

        out["configurationOverrides"] = (
            capo_emr_containers.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    out["sessionIdleTimeoutInMinutes"] = value.get("session_idle_timeout_in_minutes", 0)
    return out


def deserialize_json(data: dict) -> CreateManagedEndpointRequest:
    out: CreateManagedEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.type required")
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError(
            "CreateManagedEndpointRequest.release_label required"
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "CreateManagedEndpointRequest.execution_role_arn required"
        )
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("configurationOverrides") is not None:
        import capo_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateManagedEndpointRequest.client_token required")
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if data.get("sessionIdleTimeoutInMinutes") is not None:
        out["session_idle_timeout_in_minutes"] = data["sessionIdleTimeoutInMinutes"]
    else:
        out["session_idle_timeout_in_minutes"] = 0
    return out


def redact_sensitive(value: CreateManagedEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_overrides" in value:
        import capo_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            capo_emr_containers.types.configuration_overrides.redact_sensitive(
                value["configuration_overrides"]
            )
        )
    return out
