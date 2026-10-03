"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateEnvironmentMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_option_settings_list
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.environment_tier
    import capo_elastic_beanstalk.types.group_name
    import capo_elastic_beanstalk.types.options_specifier_list
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.version_label


class UpdateEnvironmentMessage(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application with which the environment is associated.</p>"""
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment to update.</p> <p>If no environment with this ID exists, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error.</p> <p>Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment to update. If no environment with this name exists, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    group_name: NotRequired["capo_elastic_beanstalk.types.group_name.GroupName"]
    """<p>The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html">Environment Manifest (env.yaml)</a> for details.</p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>If this parameter is specified, Elastic Beanstalk updates the description of this environment.</p>"""
    tier: NotRequired["capo_elastic_beanstalk.types.environment_tier.EnvironmentTier"]
    """<p>This specifies the tier to use to update the environment.</p> <p>Condition: At this time, if you change the tier version, name, or type, Elastic Beanstalk returns <code>InvalidParameterValue</code> error. </p>"""
    version_label: NotRequired[
        "capo_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>If this parameter is specified, Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an <code>InvalidParameterValue</code> error. </p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>If this parameter is specified, Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p>"""
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>This specifies the platform version that the environment will run after the environment is updated.</p>"""
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the platform, if used.</p>"""
    option_settings: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    """<p>If specified, Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.</p>"""
    options_to_remove: NotRequired[
        "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
    ]
    """<p>A list of custom user-defined configuration options to remove from the configuration set for this environment.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateEnvironmentMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "environment_id" in value:
        pairs.append((f"{key_prefix}EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tier" in value:
        import capo_elastic_beanstalk.types.environment_tier

        capo_elastic_beanstalk.types.environment_tier.serialize_query(
            value["tier"], pairs, f"{key_prefix}Tier"
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


def deserialize_query(el: Element) -> UpdateEnvironmentMessage:
    out: UpdateEnvironmentMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_elastic_beanstalk.types.environment_tier

        out["tier"] = capo_elastic_beanstalk.types.environment_tier.deserialize_query(
            child_tier
        )
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
    return out
