"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateConfigurationTemplateMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_option_settings_list
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.options_specifier_list


class UpdateConfigurationTemplateMessage(TypedDict, closed=True):
    application_name: "capo_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application associated with the configuration template to update.</p> <p> If no application is found with this name, <code>UpdateConfigurationTemplate</code> returns an <code>InvalidParameterValue</code> error. </p>"""
    template_name: "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    """<p>The name of the configuration template to update.</p> <p> If no configuration template is found with this name, <code>UpdateConfigurationTemplate</code> returns an <code>InvalidParameterValue</code> error. </p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>A new description for the configuration.</p>"""
    option_settings: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    """<p>A list of configuration option settings to update with the new specified option value.</p>"""
    options_to_remove: NotRequired[
        "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
    ]
    """<p>A list of configuration options to remove from the configuration set.</p> <p> Constraint: You can remove only <code>UserDefined</code> configuration options. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationTemplateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
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


def deserialize_query(el: Element) -> UpdateConfigurationTemplateMessage:
    out: UpdateConfigurationTemplateMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        out["application_name"] = ""
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        out["template_name"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
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
