"""Generated from Smithy shape ``com.amazonaws.proton#ServiceInstance``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_status
    import capo_proton.types.resource_name
    import capo_proton.types.service_instance_arn
    import capo_proton.types.spec_contents
    import capo_proton.types.status_message
    import capo_proton.types.template_version_part


class ServiceInstance(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance.</p>"""
    arn: "capo_proton.types.service_instance_arn.ServiceInstanceArn"
    """<p>The Amazon Resource Name (ARN) of the service instance.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the service instance was created.</p>"""
    last_deployment_attempted_at: "datetime.datetime"
    """<p>The time when a deployment of the service instance was last attempted.</p>"""
    last_deployment_succeeded_at: "datetime.datetime"
    """<p>The time when the service instance was last deployed successfully.</p>"""
    service_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service that the service instance belongs to.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment that the service instance was deployed into.</p>"""
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the service template that was used to create the service instance.</p>"""
    template_major_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The major version of the service template that was used to create the service instance.</p>"""
    template_minor_version: (
        "capo_proton.types.template_version_part.TemplateVersionPart"
    )
    """<p>The minor version of the service template that was used to create the service instance.</p>"""
    deployment_status: "capo_proton.types.deployment_status.DeploymentStatus"
    """<p>The service instance deployment status.</p>"""
    deployment_status_message: NotRequired[
        "capo_proton.types.status_message.StatusMessage"
    ]
    """<p>The message associated with the service instance deployment status.</p>"""
    spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that was used to create the service instance.</p>"""
    last_client_request_token: NotRequired["str"]
    """<p>The last client request token received.</p>"""
    last_attempted_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment of this service instance.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment of this service instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInstance) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastDeploymentAttemptedAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_attempted_at"]
        )
    )
    import capo_proton.types._prelude.timestamp

    out["lastDeploymentSucceededAt"] = (
        capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_deployment_succeeded_at"]
        )
    )
    out["serviceName"] = value["service_name"]
    out["environmentName"] = value["environment_name"]
    out["templateName"] = value["template_name"]
    out["templateMajorVersion"] = value["template_major_version"]
    out["templateMinorVersion"] = value["template_minor_version"]
    out["deploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    if "spec" in value:
        out["spec"] = value["spec"]
    if "last_client_request_token" in value:
        out["lastClientRequestToken"] = value["last_client_request_token"]
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceInstance:
    out: ServiceInstance = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceInstance.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ServiceInstance.arn required")
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ServiceInstance.created_at required")
    if data.get("lastDeploymentAttemptedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_attempted_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentAttemptedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceInstance.last_deployment_attempted_at required"
        )
    if data.get("lastDeploymentSucceededAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_succeeded_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentSucceededAt"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceInstance.last_deployment_succeeded_at required"
        )
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("ServiceInstance.service_name required")
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("ServiceInstance.environment_name required")
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("ServiceInstance.template_name required")
    if data.get("templateMajorVersion") is not None:
        out["template_major_version"] = data["templateMajorVersion"]
    else:
        raise DeserializationError("ServiceInstance.template_major_version required")
    if data.get("templateMinorVersion") is not None:
        out["template_minor_version"] = data["templateMinorVersion"]
    else:
        raise DeserializationError("ServiceInstance.template_minor_version required")
    if data.get("deploymentStatus") is not None:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("ServiceInstance.deployment_status required")
    if data.get("deploymentStatusMessage") is not None:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if data.get("spec") is not None:
        out["spec"] = data["spec"]
    if data.get("lastClientRequestToken") is not None:
        out["last_client_request_token"] = data["lastClientRequestToken"]
    if data.get("lastAttemptedDeploymentId") is not None:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if data.get("lastSucceededDeploymentId") is not None:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    return out


def redact_sensitive(value: ServiceInstance) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "deployment_status_message" in value:
        out["deployment_status_message"] = "*** Sensitive Data Redacted ***"
    if "spec" in value:
        out["spec"] = "*** Sensitive Data Redacted ***"
    return out
