"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.container_service_deployment
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.container_service_power_name
    import capo_lightsail.types.container_service_public_domains
    import capo_lightsail.types.container_service_scale
    import capo_lightsail.types.container_service_state
    import capo_lightsail.types.container_service_state_detail
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.private_registry_access
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class ContainerService(TypedDict, closed=True):
    container_service_name: NotRequired[
        "capo_lightsail.types.container_service_name.ContainerServiceName"
    ]
    """<p>The name of the container service.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the container service.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the container service was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that describes the location of the container service, such as the Amazon Web Services Region and Availability Zone.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type of the container service.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    power: NotRequired[
        "capo_lightsail.types.container_service_power_name.ContainerServicePowerName"
    ]
    """<p>The power specification of the container service.</p> <p>The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.</p>"""
    power_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The ID of the power of the container service.</p>"""
    state: NotRequired[
        "capo_lightsail.types.container_service_state.ContainerServiceState"
    ]
    """<p>The current state of the container service.</p> <p>The following container service states are possible:</p> <ul> <li> <p> <code>PENDING</code> - The container service is being created.</p> </li> <li> <p> <code>READY</code> - The container service is running but it does not have an active container deployment.</p> </li> <li> <p> <code>DEPLOYING</code> - The container service is launching a container deployment.</p> </li> <li> <p> <code>RUNNING</code> - The container service is running and it has an active container deployment.</p> </li> <li> <p> <code>UPDATING</code> - The container service capacity or its custom domains are being updated.</p> </li> <li> <p> <code>DELETING</code> - The container service is being deleted.</p> </li> <li> <p> <code>DISABLED</code> - The container service is disabled, and its active deployment and containers, if any, are shut down.</p> </li> </ul>"""
    state_detail: NotRequired[
        "capo_lightsail.types.container_service_state_detail.ContainerServiceStateDetail"
    ]
    """<p>An object that describes the current state of the container service.</p> <note> <p>The state detail is populated only when a container service is in a <code>PENDING</code>, <code>DEPLOYING</code>, or <code>UPDATING</code> state.</p> </note>"""
    scale: NotRequired[
        "capo_lightsail.types.container_service_scale.ContainerServiceScale"
    ]
    """<p>The scale specification of the container service.</p> <p>The scale specifies the allocated compute nodes of the container service.</p>"""
    current_deployment: NotRequired[
        "capo_lightsail.types.container_service_deployment.ContainerServiceDeployment"
    ]
    """<p>An object that describes the current container deployment of the container service.</p>"""
    next_deployment: NotRequired[
        "capo_lightsail.types.container_service_deployment.ContainerServiceDeployment"
    ]
    """<p>An object that describes the next deployment of the container service.</p> <p>This value is <code>null</code> when there is no deployment in a <code>pending</code> state.</p>"""
    is_disabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the container service is disabled.</p>"""
    principal_arn: NotRequired["capo_lightsail.types.string.string"]
    """<p>The principal ARN of the container service.</p> <p>The principal ARN can be used to create a trust relationship between your standard Amazon Web Services account and your Lightsail container service. This allows you to give your service permission to access resources in your standard Amazon Web Services account.</p>"""
    private_domain_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The private domain name of the container service.</p> <p>The private domain name is accessible only by other resources within the default virtual private cloud (VPC) of your Lightsail account.</p>"""
    public_domain_names: NotRequired[
        "capo_lightsail.types.container_service_public_domains.ContainerServicePublicDomains"
    ]
    """<p>The public domain name of the container service, such as <code>example.com</code> and <code>www.example.com</code>.</p> <p>You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.</p> <p>If you don't specify public domain names, then you can use the default domain of the container service.</p> <important> <p>You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the <code>CreateCertificate</code> action to create a certificate for the public domain names you want to use with your container service.</p> </important> <p>See <code>CreateContainerService</code> or <code>UpdateContainerService</code> for information about how to specify public domain names for your Lightsail container service.</p>"""
    url: NotRequired["capo_lightsail.types.string.string"]
    """<p>The publicly accessible URL of the container service.</p> <p>If no public endpoint is specified in the <code>currentDeployment</code>, this URL returns a 404 response.</p>"""
    private_registry_access: NotRequired[
        "capo_lightsail.types.private_registry_access.PrivateRegistryAccess"
    ]
    """<p>An object that describes the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access">Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerService) -> dict:
    out: dict = {}
    if "container_service_name" in value:
        out["containerServiceName"] = value["container_service_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "power" in value:
        import capo_lightsail.types.container_service_power_name

        out["power"] = (
            capo_lightsail.types.container_service_power_name.serialize_aws_json_1_1(
                value["power"]
            )
        )
    if "power_id" in value:
        out["powerId"] = value["power_id"]
    if "state" in value:
        import capo_lightsail.types.container_service_state

        out["state"] = (
            capo_lightsail.types.container_service_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_detail" in value:
        import capo_lightsail.types.container_service_state_detail

        out["stateDetail"] = (
            capo_lightsail.types.container_service_state_detail.serialize_aws_json_1_1(
                value["state_detail"]
            )
        )
    if "scale" in value:
        out["scale"] = value["scale"]
    if "current_deployment" in value:
        import capo_lightsail.types.container_service_deployment

        out["currentDeployment"] = (
            capo_lightsail.types.container_service_deployment.serialize_aws_json_1_1(
                value["current_deployment"]
            )
        )
    if "next_deployment" in value:
        import capo_lightsail.types.container_service_deployment

        out["nextDeployment"] = (
            capo_lightsail.types.container_service_deployment.serialize_aws_json_1_1(
                value["next_deployment"]
            )
        )
    if "is_disabled" in value:
        out["isDisabled"] = value["is_disabled"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "private_domain_name" in value:
        out["privateDomainName"] = value["private_domain_name"]
    if "public_domain_names" in value:
        import capo_lightsail.types.container_service_public_domains

        out["publicDomainNames"] = (
            capo_lightsail.types.container_service_public_domains.serialize_aws_json_1_1(
                value["public_domain_names"]
            )
        )
    if "url" in value:
        out["url"] = value["url"]
    if "private_registry_access" in value:
        import capo_lightsail.types.private_registry_access

        out["privateRegistryAccess"] = (
            capo_lightsail.types.private_registry_access.serialize_aws_json_1_1(
                value["private_registry_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerService:
    out: ContainerService = {}  # type: ignore[typeddict-item]
    if data.get("containerServiceName") is not None:
        out["container_service_name"] = data["containerServiceName"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("power") is not None:
        import capo_lightsail.types.container_service_power_name

        out["power"] = (
            capo_lightsail.types.container_service_power_name.deserialize_aws_json_1_1(
                data["power"]
            )
        )
    if data.get("powerId") is not None:
        out["power_id"] = data["powerId"]
    if data.get("state") is not None:
        import capo_lightsail.types.container_service_state

        out["state"] = (
            capo_lightsail.types.container_service_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if data.get("stateDetail") is not None:
        import capo_lightsail.types.container_service_state_detail

        out["state_detail"] = (
            capo_lightsail.types.container_service_state_detail.deserialize_aws_json_1_1(
                data["stateDetail"]
            )
        )
    if data.get("scale") is not None:
        out["scale"] = data["scale"]
    if data.get("currentDeployment") is not None:
        import capo_lightsail.types.container_service_deployment

        out["current_deployment"] = (
            capo_lightsail.types.container_service_deployment.deserialize_aws_json_1_1(
                data["currentDeployment"]
            )
        )
    if data.get("nextDeployment") is not None:
        import capo_lightsail.types.container_service_deployment

        out["next_deployment"] = (
            capo_lightsail.types.container_service_deployment.deserialize_aws_json_1_1(
                data["nextDeployment"]
            )
        )
    if data.get("isDisabled") is not None:
        out["is_disabled"] = data["isDisabled"]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    if data.get("privateDomainName") is not None:
        out["private_domain_name"] = data["privateDomainName"]
    if data.get("publicDomainNames") is not None:
        import capo_lightsail.types.container_service_public_domains

        out["public_domain_names"] = (
            capo_lightsail.types.container_service_public_domains.deserialize_aws_json_1_1(
                data["publicDomainNames"]
            )
        )
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("privateRegistryAccess") is not None:
        import capo_lightsail.types.private_registry_access

        out["private_registry_access"] = (
            capo_lightsail.types.private_registry_access.deserialize_aws_json_1_1(
                data["privateRegistryAccess"]
            )
        )
    return out
