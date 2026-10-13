"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateIntegrationWorkflowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.integration_config
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.role_arn
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.type_name
    import capo_customer_profiles.types.workflow_type


class CreateIntegrationWorkflowRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    workflow_type: "capo_customer_profiles.types.workflow_type.WorkflowType"
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    integration_config: (
        "capo_customer_profiles.types.integration_config.IntegrationConfig"
    )
    """<p>Configuration data for integration workflow.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    role_arn: "capo_customer_profiles.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationWorkflowRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.workflow_type

    out["WorkflowType"] = capo_customer_profiles.types.workflow_type.serialize_json(
        value["workflow_type"]
    )
    import capo_customer_profiles.types.integration_config

    out["IntegrationConfig"] = (
        capo_customer_profiles.types.integration_config.serialize_json(
            value["integration_config"]
        )
    )
    out["ObjectTypeName"] = value["object_type_name"]
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIntegrationWorkflowRequest:
    out: CreateIntegrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowType") is not None:
        import capo_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            capo_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIntegrationWorkflowRequest.workflow_type required"
        )
    if data.get("IntegrationConfig") is not None:
        import capo_customer_profiles.types.integration_config

        out["integration_config"] = (
            capo_customer_profiles.types.integration_config.deserialize_json(
                data["IntegrationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIntegrationWorkflowRequest.integration_config required"
        )
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "CreateIntegrationWorkflowRequest.object_type_name required"
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateIntegrationWorkflowRequest.role_arn required")
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateIntegrationWorkflowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "integration_config" in value:
        import capo_customer_profiles.types.integration_config

        out["integration_config"] = (
            capo_customer_profiles.types.integration_config.redact_sensitive(
                value["integration_config"]
            )
        )
    return out
