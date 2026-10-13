"""Generated from Smithy shape ``com.amazonaws.proton#Component``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.component_arn
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_status
    import capo_proton.types.description
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.status_message


class Component(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the component.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the component.</p>"""
    arn: "capo_proton.types.component_arn.ComponentArn"
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
    environment_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the Proton environment that this component is associated with.</p>"""
    service_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service that <code>serviceInstanceName</code> is associated with. Provided when a component is attached to a service instance.</p>"""
    service_instance_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the component was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the component was last modified.</p>"""
    last_deployment_attempted_at: NotRequired["datetime.datetime"]
    """<p>The time when a deployment of the component was last attempted.</p>"""
    last_deployment_succeeded_at: NotRequired["datetime.datetime"]
    """<p>The time when the component was last deployed successfully.</p>"""
    deployment_status: "capo_proton.types.deployment_status.DeploymentStatus"
    """<p>The component deployment status.</p>"""
    deployment_status_message: NotRequired[
        "capo_proton.types.status_message.StatusMessage"
    ]
    """<p>The message associated with the component deployment status.</p>"""
    service_spec: NotRequired["capo_proton.types.spec_contents.SpecContents"]
    """<p>The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.</p>"""
    last_client_request_token: NotRequired["str"]
    """<p>The last token the client requested.</p>"""
    last_attempted_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last attempted deployment of this component.</p>"""
    last_succeeded_deployment_id: NotRequired[
        "capo_proton.types.deployment_id.DeploymentId"
    ]
    """<p>The ID of the last successful deployment of this component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Component) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    out["environmentName"] = value["environment_name"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    if "last_deployment_attempted_at" in value:
        import capo_proton.types._prelude.timestamp

        out["lastDeploymentAttemptedAt"] = (
            capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_deployment_attempted_at"]
            )
        )
    if "last_deployment_succeeded_at" in value:
        import capo_proton.types._prelude.timestamp

        out["lastDeploymentSucceededAt"] = (
            capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_deployment_succeeded_at"]
            )
        )
    out["deploymentStatus"] = value["deployment_status"]
    if "deployment_status_message" in value:
        out["deploymentStatusMessage"] = value["deployment_status_message"]
    if "service_spec" in value:
        out["serviceSpec"] = value["service_spec"]
    if "last_client_request_token" in value:
        out["lastClientRequestToken"] = value["last_client_request_token"]
    if "last_attempted_deployment_id" in value:
        out["lastAttemptedDeploymentId"] = value["last_attempted_deployment_id"]
    if "last_succeeded_deployment_id" in value:
        out["lastSucceededDeploymentId"] = value["last_succeeded_deployment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Component:
    out: Component = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Component.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Component.arn required")
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        raise DeserializationError("Component.environment_name required")
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("serviceInstanceName") is not None:
        out["service_instance_name"] = data["serviceInstanceName"]
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Component.created_at required")
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError("Component.last_modified_at required")
    if data.get("lastDeploymentAttemptedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_attempted_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentAttemptedAt"]
            )
        )
    if data.get("lastDeploymentSucceededAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_deployment_succeeded_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastDeploymentSucceededAt"]
            )
        )
    if data.get("deploymentStatus") is not None:
        out["deployment_status"] = data["deploymentStatus"]
    else:
        raise DeserializationError("Component.deployment_status required")
    if data.get("deploymentStatusMessage") is not None:
        out["deployment_status_message"] = data["deploymentStatusMessage"]
    if data.get("serviceSpec") is not None:
        out["service_spec"] = data["serviceSpec"]
    if data.get("lastClientRequestToken") is not None:
        out["last_client_request_token"] = data["lastClientRequestToken"]
    if data.get("lastAttemptedDeploymentId") is not None:
        out["last_attempted_deployment_id"] = data["lastAttemptedDeploymentId"]
    if data.get("lastSucceededDeploymentId") is not None:
        out["last_succeeded_deployment_id"] = data["lastSucceededDeploymentId"]
    return out


def redact_sensitive(value: Component) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "deployment_status_message" in value:
        out["deployment_status_message"] = "*** Sensitive Data Redacted ***"
    if "service_spec" in value:
        out["service_spec"] = "*** Sensitive Data Redacted ***"
    return out
