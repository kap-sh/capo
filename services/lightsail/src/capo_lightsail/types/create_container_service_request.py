"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_deployment_request
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.container_service_power_name
    import capo_lightsail.types.container_service_public_domains
    import capo_lightsail.types.container_service_scale
    import capo_lightsail.types.private_registry_access_request
    import capo_lightsail.types.tag_list


class CreateContainerServiceRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name for the container service.</p> <p>The name that you specify for your container service will make up part of its default domain. The default domain of a container service is typically <code>https://<ServiceName>.<RandomGUID>.<AWSRegion>.cs.amazonlightsail.com</code>. If the name of your container service is <code>container-service-1</code>, and it's located in the US East (Ohio) Amazon Web Services Region (<code>us-east-2</code>), then the domain for your container service will be like the following example: <code>https://container-service-1.ur4EXAMPLE2uq.us-east-2.cs.amazonlightsail.com</code> </p> <p>The following are the requirements for container service names:</p> <ul> <li> <p>Must be unique within each Amazon Web Services Region in your Lightsail account.</p> </li> <li> <p>Must contain 1 to 63 characters.</p> </li> <li> <p>Must contain only alphanumeric characters and hyphens.</p> </li> <li> <p>A hyphen (-) can separate words but cannot be at the start or end of the name.</p> </li> </ul>"""
    power: "capo_lightsail.types.container_service_power_name.ContainerServicePowerName"
    """<p>The power specification for the container service.</p> <p>The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p> <p>Use the <code>GetContainerServicePowers</code> action to get a list of power options that you can specify using this parameter, and their base monthly cost.</p>"""
    scale: "capo_lightsail.types.container_service_scale.ContainerServiceScale"
    """<p>The scale specification for the container service.</p> <p>The scale specifies the allocated compute nodes of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the container service during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p> <p>For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    public_domain_names: NotRequired[
        "capo_lightsail.types.container_service_public_domains.ContainerServicePublicDomains"
    ]
    """<p>The public domain names to use with the container service, such as <code>example.com</code> and <code>www.example.com</code>.</p> <p>You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.</p> <p>If you don't specify public domain names, then you can use the default domain of the container service.</p> <important> <p>You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the <code>CreateCertificate</code> action to create a certificate for the public domain names you want to use with your container service.</p> </important> <p>You can specify public domain names using a string to array map as shown in the example later on this page.</p>"""
    deployment: NotRequired[
        "capo_lightsail.types.container_service_deployment_request.ContainerServiceDeploymentRequest"
    ]
    """<p>An object that describes a deployment for the container service.</p> <p>A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.</p>"""
    private_registry_access: NotRequired[
        "capo_lightsail.types.private_registry_access_request.PrivateRegistryAccessRequest"
    ]
    """<p>An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access">Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    import capo_lightsail.types.container_service_power_name

    out["power"] = (
        capo_lightsail.types.container_service_power_name.serialize_aws_json_1_1(
            value["power"]
        )
    )
    out["scale"] = value["scale"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "public_domain_names" in value:
        import capo_lightsail.types.container_service_public_domains

        out["publicDomainNames"] = (
            capo_lightsail.types.container_service_public_domains.serialize_aws_json_1_1(
                value["public_domain_names"]
            )
        )
    if "deployment" in value:
        import capo_lightsail.types.container_service_deployment_request

        out["deployment"] = (
            capo_lightsail.types.container_service_deployment_request.serialize_aws_json_1_1(
                value["deployment"]
            )
        )
    if "private_registry_access" in value:
        import capo_lightsail.types.private_registry_access_request

        out["privateRegistryAccess"] = (
            capo_lightsail.types.private_registry_access_request.serialize_aws_json_1_1(
                value["private_registry_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceRequest:
    out: CreateContainerServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "CreateContainerServiceRequest.service_name required"
        )
    if data.get("power") is not None:
        import capo_lightsail.types.container_service_power_name

        out["power"] = (
            capo_lightsail.types.container_service_power_name.deserialize_aws_json_1_1(
                data["power"]
            )
        )
    else:
        raise DeserializationError("CreateContainerServiceRequest.power required")
    if data.get("scale") is not None:
        out["scale"] = data["scale"]
    else:
        raise DeserializationError("CreateContainerServiceRequest.scale required")
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("publicDomainNames") is not None:
        import capo_lightsail.types.container_service_public_domains

        out["public_domain_names"] = (
            capo_lightsail.types.container_service_public_domains.deserialize_aws_json_1_1(
                data["publicDomainNames"]
            )
        )
    if data.get("deployment") is not None:
        import capo_lightsail.types.container_service_deployment_request

        out["deployment"] = (
            capo_lightsail.types.container_service_deployment_request.deserialize_aws_json_1_1(
                data["deployment"]
            )
        )
    if data.get("privateRegistryAccess") is not None:
        import capo_lightsail.types.private_registry_access_request

        out["private_registry_access"] = (
            capo_lightsail.types.private_registry_access_request.deserialize_aws_json_1_1(
                data["privateRegistryAccess"]
            )
        )
    return out
