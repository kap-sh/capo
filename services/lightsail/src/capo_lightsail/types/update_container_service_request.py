"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateContainerServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.container_service_power_name
    import capo_lightsail.types.container_service_public_domains
    import capo_lightsail.types.container_service_scale
    import capo_lightsail.types.private_registry_access_request


class UpdateContainerServiceRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service to update.</p>"""
    power: NotRequired[
        "capo_lightsail.types.container_service_power_name.ContainerServicePowerName"
    ]
    """<p>The power for the container service.</p> <p>The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p> <p>Use the <code>GetContainerServicePowers</code> action to view the specifications of each power option.</p>"""
    scale: NotRequired[
        "capo_lightsail.types.container_service_scale.ContainerServiceScale"
    ]
    """<p>The scale for the container service.</p> <p>The scale specifies the allocated compute nodes of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p>"""
    is_disabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value to indicate whether the container service is disabled.</p>"""
    public_domain_names: NotRequired[
        "capo_lightsail.types.container_service_public_domains.ContainerServicePublicDomains"
    ]
    """<p>The public domain names to use with the container service, such as <code>example.com</code> and <code>www.example.com</code>.</p> <p>You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.</p> <p>If you don't specify public domain names, then you can use the default domain of the container service.</p> <important> <p>You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the <code>CreateCertificate</code> action to create a certificate for the public domain names you want to use with your container service.</p> </important> <p>You can specify public domain names using a string to array map as shown in the example later on this page.</p>"""
    private_registry_access: NotRequired[
        "capo_lightsail.types.private_registry_access_request.PrivateRegistryAccessRequest"
    ]
    """<p>An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access">Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerServiceRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "power" in value:
        import capo_lightsail.types.container_service_power_name

        out["power"] = (
            capo_lightsail.types.container_service_power_name.serialize_aws_json_1_1(
                value["power"]
            )
        )
    if "scale" in value:
        out["scale"] = value["scale"]
    if "is_disabled" in value:
        out["isDisabled"] = value["is_disabled"]
    if "public_domain_names" in value:
        import capo_lightsail.types.container_service_public_domains

        out["publicDomainNames"] = (
            capo_lightsail.types.container_service_public_domains.serialize_aws_json_1_1(
                value["public_domain_names"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerServiceRequest:
    out: UpdateContainerServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "UpdateContainerServiceRequest.service_name required"
        )
    if data.get("power") is not None:
        import capo_lightsail.types.container_service_power_name

        out["power"] = (
            capo_lightsail.types.container_service_power_name.deserialize_aws_json_1_1(
                data["power"]
            )
        )
    if data.get("scale") is not None:
        out["scale"] = data["scale"]
    if data.get("isDisabled") is not None:
        out["is_disabled"] = data["isDisabled"]
    if data.get("publicDomainNames") is not None:
        import capo_lightsail.types.container_service_public_domains

        out["public_domain_names"] = (
            capo_lightsail.types.container_service_public_domains.deserialize_aws_json_1_1(
                data["publicDomainNames"]
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
