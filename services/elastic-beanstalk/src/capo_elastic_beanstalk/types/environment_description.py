"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.abortable_operation_in_progress
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.creation_date
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.dns_cname
    import capo_elastic_beanstalk.types.endpoint_url
    import capo_elastic_beanstalk.types.environment_arn
    import capo_elastic_beanstalk.types.environment_health
    import capo_elastic_beanstalk.types.environment_health_status
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_links
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.environment_resources_description
    import capo_elastic_beanstalk.types.environment_status
    import capo_elastic_beanstalk.types.environment_tier
    import capo_elastic_beanstalk.types.operations_role
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.update_date
    import capo_elastic_beanstalk.types.version_label


class EnvironmentDescription(TypedDict, closed=True):
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of this environment.</p>"""
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of this environment.</p>"""
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application associated with this environment.</p>"""
    version_label: NotRequired[
        "capo_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>The application version deployed in this environment.</p>"""
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p> The name of the <code>SolutionStack</code> deployed with this environment. </p>"""
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the platform version.</p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>The name of the configuration template used to originally launch this environment.</p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>Describes this environment.</p>"""
    endpoint_url: NotRequired["capo_elastic_beanstalk.types.endpoint_url.EndpointURL"]
    """<p>For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.</p>"""
    cname: NotRequired["capo_elastic_beanstalk.types.dns_cname.DNSCname"]
    """<p>The URL to the CNAME for this environment.</p>"""
    date_created: NotRequired["capo_elastic_beanstalk.types.creation_date.CreationDate"]
    """<p>The creation date for this environment.</p>"""
    date_updated: NotRequired["capo_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The last modified date for this environment.</p>"""
    status: NotRequired[
        "capo_elastic_beanstalk.types.environment_status.EnvironmentStatus"
    ]
    """<p>The current operational status of the environment:</p> <ul> <li> <p> <code>Aborting</code>: Environment is in the process of aborting a deployment.</p> </li> <li> <p> <code>Launching</code>: Environment is in the process of initial deployment.</p> </li> <li> <p> <code>LinkingFrom</code>: Environment is in the process of being linked to by another environment. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html">Environment links</a> for details.</p> </li> <li> <p> <code>LinkingTo</code>: Environment is in the process of linking to another environment. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html">Environment links</a> for details.</p> </li> <li> <p> <code>Updating</code>: Environment is in the process of updating its configuration settings or application version.</p> </li> <li> <p> <code>Ready</code>: Environment is available to have an action performed on it, such as update or terminate.</p> </li> <li> <p> <code>Terminating</code>: Environment is in the shut-down process.</p> </li> <li> <p> <code>Terminated</code>: Environment is not running.</p> </li> </ul>"""
    abortable_operation_in_progress: NotRequired[
        "capo_elastic_beanstalk.types.abortable_operation_in_progress.AbortableOperationInProgress"
    ]
    """<p>Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.</p> <p> <code>true:</code> There is an update in progress. </p> <p> <code>false:</code> There are no updates currently in progress. </p>"""
    health: NotRequired[
        "capo_elastic_beanstalk.types.environment_health.EnvironmentHealth"
    ]
    """<p>Describes the health status of the environment. Elastic Beanstalk indicates the failure levels for a running environment:</p> <ul> <li> <p> <code>Red</code>: Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment.</p> </li> <li> <p> <code>Yellow</code>: Indicates that something is wrong. Occurs when two consecutive failures occur for an environment.</p> </li> <li> <p> <code>Green</code>: Indicates the environment is healthy and fully functional.</p> </li> <li> <p> <code>Grey</code>: Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an <code>UpdateEnvironment</code> or <code>RestartEnvironment</code> request.</p> </li> </ul> <p> Default: <code>Grey</code> </p>"""
    health_status: NotRequired[
        "capo_elastic_beanstalk.types.environment_health_status.EnvironmentHealthStatus"
    ]
    """<p>Returns the health status of the application running in your environment. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html">Health Colors and Statuses</a>.</p>"""
    resources: NotRequired[
        "capo_elastic_beanstalk.types.environment_resources_description.EnvironmentResourcesDescription"
    ]
    """<p>The description of the Amazon Web Services resources used by this environment.</p>"""
    tier: NotRequired["capo_elastic_beanstalk.types.environment_tier.EnvironmentTier"]
    """<p>Describes the current tier of this environment.</p>"""
    environment_links: NotRequired[
        "capo_elastic_beanstalk.types.environment_links.EnvironmentLinks"
    ]
    """<p>A list of links to other environments in the same group.</p>"""
    environment_arn: NotRequired[
        "capo_elastic_beanstalk.types.environment_arn.EnvironmentArn"
    ]
    """<p>The environment's Amazon Resource Name (ARN), which can be used in other API requests that require an ARN.</p>"""
    operations_role: NotRequired[
        "capo_elastic_beanstalk.types.operations_role.OperationsRole"
    ]
    """<important> <p>The operations role feature of Elastic Beanstalk is in beta release and is subject to change.</p> </important> <p>The Amazon Resource Name (ARN) of the environment's operations role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{key_prefix}EnvironmentId", str(value["environment_id"])))
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "version_label" in value:
        pairs.append((f"{key_prefix}VersionLabel", str(value["version_label"])))
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "endpoint_url" in value:
        pairs.append((f"{key_prefix}EndpointURL", str(value["endpoint_url"])))
    if "cname" in value:
        pairs.append((f"{key_prefix}CNAME", str(value["cname"])))
    if "date_created" in value:
        import capo_elastic_beanstalk.types.creation_date

        capo_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{key_prefix}DateCreated"
        )
    if "date_updated" in value:
        import capo_elastic_beanstalk.types.update_date

        capo_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{key_prefix}DateUpdated"
        )
    if "status" in value:
        import capo_elastic_beanstalk.types.environment_status

        capo_elastic_beanstalk.types.environment_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "abortable_operation_in_progress" in value:
        pairs.append(
            (
                f"{key_prefix}AbortableOperationInProgress",
                "true" if value["abortable_operation_in_progress"] else "false",
            )
        )
    if "health" in value:
        import capo_elastic_beanstalk.types.environment_health

        capo_elastic_beanstalk.types.environment_health.serialize_query(
            value["health"], pairs, f"{key_prefix}Health"
        )
    if "health_status" in value:
        import capo_elastic_beanstalk.types.environment_health_status

        capo_elastic_beanstalk.types.environment_health_status.serialize_query(
            value["health_status"], pairs, f"{key_prefix}HealthStatus"
        )
    if "resources" in value:
        import capo_elastic_beanstalk.types.environment_resources_description

        capo_elastic_beanstalk.types.environment_resources_description.serialize_query(
            value["resources"], pairs, f"{key_prefix}Resources"
        )
    if "tier" in value:
        import capo_elastic_beanstalk.types.environment_tier

        capo_elastic_beanstalk.types.environment_tier.serialize_query(
            value["tier"], pairs, f"{key_prefix}Tier"
        )
    if "environment_links" in value:
        import capo_elastic_beanstalk.types.environment_links

        capo_elastic_beanstalk.types.environment_links.serialize_query(
            value["environment_links"], pairs, f"{key_prefix}EnvironmentLinks"
        )
    if "environment_arn" in value:
        pairs.append((f"{key_prefix}EnvironmentArn", str(value["environment_arn"])))
    if "operations_role" in value:
        pairs.append((f"{key_prefix}OperationsRole", str(value["operations_role"])))


def deserialize_query(el: Element) -> EnvironmentDescription:
    out: EnvironmentDescription = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_endpoint_url = el.find("EndpointURL")
    if child_endpoint_url is not None:
        out["endpoint_url"] = str(child_endpoint_url.text or "")
    child_cname = el.find("CNAME")
    if child_cname is not None:
        out["cname"] = str(child_cname.text or "")
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import capo_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            capo_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import capo_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            capo_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_elastic_beanstalk.types.environment_status

        out["status"] = (
            capo_elastic_beanstalk.types.environment_status.deserialize_query(
                child_status
            )
        )
    child_abortable_operation_in_progress = el.find("AbortableOperationInProgress")
    if child_abortable_operation_in_progress is not None:
        out["abortable_operation_in_progress"] = (
            child_abortable_operation_in_progress.text or ""
        ).lower() == "true"
    child_health = el.find("Health")
    if child_health is not None:
        import capo_elastic_beanstalk.types.environment_health

        out["health"] = (
            capo_elastic_beanstalk.types.environment_health.deserialize_query(
                child_health
            )
        )
    child_health_status = el.find("HealthStatus")
    if child_health_status is not None:
        import capo_elastic_beanstalk.types.environment_health_status

        out["health_status"] = (
            capo_elastic_beanstalk.types.environment_health_status.deserialize_query(
                child_health_status
            )
        )
    child_resources = el.find("Resources")
    if child_resources is not None:
        import capo_elastic_beanstalk.types.environment_resources_description

        out["resources"] = (
            capo_elastic_beanstalk.types.environment_resources_description.deserialize_query(
                child_resources
            )
        )
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_elastic_beanstalk.types.environment_tier

        out["tier"] = capo_elastic_beanstalk.types.environment_tier.deserialize_query(
            child_tier
        )
    child_environment_links = el.find("EnvironmentLinks")
    if child_environment_links is not None:
        import capo_elastic_beanstalk.types.environment_links

        out["environment_links"] = (
            capo_elastic_beanstalk.types.environment_links.deserialize_query(
                child_environment_links
            )
        )
    child_environment_arn = el.find("EnvironmentArn")
    if child_environment_arn is not None:
        out["environment_arn"] = str(child_environment_arn.text or "")
    child_operations_role = el.find("OperationsRole")
    if child_operations_role is not None:
        out["operations_role"] = str(child_operations_role.text or "")
    return out
