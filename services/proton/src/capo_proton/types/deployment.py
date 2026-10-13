"""Generated from Smithy shape ``com.amazonaws.proton#Deployment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.arn
    import capo_proton.types.deployment_arn
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_state
    import capo_proton.types.deployment_status
    import capo_proton.types.deployment_target_resource_type
    import capo_proton.types.resource_name
    import capo_proton.types.status_message


class Deployment(TypedDict, closed=True):
    id: "capo_proton.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    arn: "capo_proton.types.deployment_arn.DeploymentArn"
    """<p>The Amazon Resource Name (ARN) of the deployment.</p>"""
    target_arn: "capo_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the target of the deployment.</p>"""
    target_resource_created_at: "datetime.datetime"
    """<p>The date and time the depoyment target was created.</p>"""
    target_resource_type: (
        "capo_proton.types.deployment_target_resource_type.DeploymentTargetResourceType"
    )
    """<p>The resource type of the deployment target. It can be an environment, service, service instance, or component.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment associated with this deployment.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service in this deployment.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the deployment's service instance.</p>"""
    component_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the component associated with this deployment.</p>"""
    deployment_status: "capo_proton.types.deployment_status.DeploymentStatus"
    """<p>The status of the deployment.</p>"""
    deployment_status_message: NotRequired[
        "capo_proton.types.status_message.StatusMessage"
    ]
    """<p>The deployment status message.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the deployment was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The date and time the deployment was last modified.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The date and time the deployment was completed.</p>"""
    last_attempted_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment.</p>"""
    initial_state: NotRequired["capo_proton.types.deployment_state.DeploymentState"]
    """<p>The initial state of the target resource at the time of the deployment.</p>"""
    target_state: NotRequired["capo_proton.types.deployment_state.DeploymentState"]
    """<p>The target state of the target resource at the time of the deployment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Deployment) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["targetArn"] = value["target_arn"]
    import capo_proton.types._prelude.timestamp

    out["targetResourceCreatedAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["target_resource_created_at"]
        )
    )
    out["targetResourceType"] = value["target_resource_type"]
    out["environmentName"] = value["environment_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    out["deploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    if "completed_at" in value:
        import capo_proton.types._prelude.timestamp

        out["completedAt"] = (
            capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_at"]
            )
        )
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    if "initial_state" in value:
        import capo_proton.types.deployment_state

        out["initialState"] = capo_proton.types.deployment_state.serialize_aws_json_1_0(
            value["initial_state"]
        )
    if "target_state" in value:
        import capo_proton.types.deployment_state

        out["targetState"] = capo_proton.types.deployment_state.serialize_aws_json_1_0(
            value["target_state"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Deployment.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Deployment.arn required")
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("Deployment.target_arn required")
    if data.get("targetResourceCreatedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["target_resource_created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["targetResourceCreatedAt"]
            )
        )
    else:
        raise DeserializationError("Deployment.target_resource_created_at required")
    if data.get("targetResourceType") is not None:
        out["target_resource_type"] = data["targetResourceType"]
    else:
        raise DeserializationError("Deployment.target_resource_type required")
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("Deployment.environment_name required")
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("deploymentStatus") is not None:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("Deployment.deployment_status required")
    if data.get("deploymentStatusMessage") is not None:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Deployment.created_at required")
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("Deployment.last_modified_at required")
    if data.get("completedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["completed_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedAt"]
            )
        )
    if data.get("lastAttemptedDeploymentId") is not None:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if data.get("lastSucceededDeploymentId") is not None:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    if data.get("initialState") is not None:
        import capo_proton.types.deployment_state

        out["initial_state"] = (
            capo_proton.types.deployment_state.deserialize_aws_json_1_0(
                data["initialState"]
            )
        )
    if data.get("targetState") is not None:
        import capo_proton.types.deployment_state

        out["target_state"] = (
            capo_proton.types.deployment_state.deserialize_aws_json_1_0(
                data["targetState"]
            )
        )
    return out


def redact_sensitive(value: Deployment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_status_message" in value:
        out["deployment_status_message"] = "*** Sensitive Data Redacted ***"
    if "initial_state" in value:
        import capo_proton.types.deployment_state

        out["initial_state"] = capo_proton.types.deployment_state.redact_sensitive(
            value["initial_state"]
        )
    if "target_state" in value:
        import capo_proton.types.deployment_state

        out["target_state"] = capo_proton.types.deployment_state.redact_sensitive(
            value["target_state"]
        )
    return out
