"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateEnvironmentMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element
from capo_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_option_settings_list
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.dns_cname_prefix
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.environment_tier
    import capo_elastic_beanstalk.types.group_name
    import capo_elastic_beanstalk.types.operations_role
    import capo_elastic_beanstalk.types.options_specifier_list
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.tags
    import capo_elastic_beanstalk.types.version_label


class CreateEnvironmentMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application that is associated with this environment.</p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>A unique name for the environment.</p> <p>Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account. If the specified name already exists in the region, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p> <p>If you don't specify the <code>CNAMEPrefix</code> parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.</p>"""
    group_name: NotRequired["capo_elastic_beanstalk.types.group_name.GroupName"]
    """<p>The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>Your description for this environment.</p>"""
    cname_prefix: NotRequired[
        "capo_elastic_beanstalk.types.dns_cname_prefix.DNSCnamePrefix"
    ]
    """<p>If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.</p>"""
    tier: NotRequired["capo_elastic_beanstalk.types.environment_tier.EnvironmentTier"]
    """<p>Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources on Amazon EC2 instances or on an Amazon EKS cluster, and, for Amazon EC2, whether the environment serves HTTP(S) requests or processes background tasks from a queue.</p>"""
    tags: NotRequired["capo_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to resources in the environment.</p>"""
    version_label: NotRequired[
        "capo_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>The name of the application version to deploy.</p> <p>Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.</p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>The name of the Elastic Beanstalk configuration template to use with the environment.</p> <note> <p>If you specify <code>TemplateName</code>, then don't specify <code>SolutionStackName</code>.</p> </note>"""
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html">Elastic Beanstalk Supported Platforms</a> in the <i>Elastic Beanstalk Platforms</i> guide.</p> <note> <p>If you specify <code>SolutionStackName</code>, don't specify <code>PlatformArn</code> or <code>TemplateName</code>.</p> </note>"""
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html">Custom Platforms</a> in the <i>Elastic Beanstalk Developer Guide</i>.</p> <note> <p>If you specify <code>PlatformArn</code>, don't specify <code>SolutionStackName</code>.</p> </note>"""
    option_settings: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    """<p>If specified, Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.</p>"""
    options_to_remove: NotRequired[
        "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
    ]
    """<p>A list of custom user-defined configuration options to remove from the configuration set for this new environment.</p>"""
    operations_role: NotRequired[
        "capo_elastic_beanstalk.types.operations_role.OperationsRole"
    ]
    """<important> <p>The operations role feature of Elastic Beanstalk is in beta release and is subject to change.</p> </important> <p>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the <code>iam:PassRole</code> permission for the role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateEnvironmentMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "cname_prefix" in value:
        pairs.append((f"{key_prefix}CNAMEPrefix", str(value["cname_prefix"])))
    if "tier" in value:
        import capo_elastic_beanstalk.types.environment_tier

        capo_elastic_beanstalk.types.environment_tier.serialize_query(
            value["tier"], pairs, f"{key_prefix}Tier"
        )
    if "tags" in value:
        import capo_elastic_beanstalk.types.tags

        capo_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "version_label" in value:
        pairs.append((f"{key_prefix}VersionLabel", str(value["version_label"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))
    if "option_settings" in value:
        import capo_elastic_beanstalk.types.configuration_option_settings_list

        capo_elastic_beanstalk.types.configuration_option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{key_prefix}OptionSettings"
        )
    if "options_to_remove" in value:
        import capo_elastic_beanstalk.types.options_specifier_list

        capo_elastic_beanstalk.types.options_specifier_list.serialize_query(
            value["options_to_remove"], pairs, f"{key_prefix}OptionsToRemove"
        )
    if "operations_role" in value:
        pairs.append((f"{key_prefix}OperationsRole", str(value["operations_role"])))


def deserialize_query(el: Element) -> CreateEnvironmentMessage:
    out: CreateEnvironmentMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError("CreateEnvironmentMessage.application_name required")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_cname_prefix = el.find("CNAMEPrefix")
    if child_cname_prefix is not None:
        out["cname_prefix"] = str(child_cname_prefix.text or "")
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_elastic_beanstalk.types.environment_tier

        out["tier"] = capo_elastic_beanstalk.types.environment_tier.deserialize_query(
            child_tier
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_beanstalk.types.tags

        out["tags"] = capo_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import capo_elastic_beanstalk.types.configuration_option_settings_list

        out["option_settings"] = (
            capo_elastic_beanstalk.types.configuration_option_settings_list.deserialize_query(
                child_option_settings
            )
        )
    child_options_to_remove = el.find("OptionsToRemove")
    if child_options_to_remove is not None:
        import capo_elastic_beanstalk.types.options_specifier_list

        out["options_to_remove"] = (
            capo_elastic_beanstalk.types.options_specifier_list.deserialize_query(
                child_options_to_remove
            )
        )
    child_operations_role = el.find("OperationsRole")
    if child_operations_role is not None:
        out["operations_role"] = str(child_operations_role.text or "")
    return out
