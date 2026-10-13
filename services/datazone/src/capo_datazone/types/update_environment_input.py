"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_id
    import capo_datazone.types.environment_parameters_list
    import capo_datazone.types.glossary_terms


class UpdateEnvironmentInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which the environment is to be updated.</p>"""
    identifier: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment that is to be updated.</p>"""
    name: NotRequired["str"]
    """<p>The name to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    blueprint_version: NotRequired["str"]
    """<p>The blueprint version to which the environment should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of the environment.</p>"""
    environment_configuration_name: NotRequired[
        "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "user_parameters" in value:
        import capo_datazone.types.environment_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentInput:
    out: UpdateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("blueprintVersion") is not None:
        out["blueprint_version"] = data["blueprintVersion"]
    if data.get("userParameters") is not None:
        import capo_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("environmentConfigurationName") is not None:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out


def redact_sensitive(value: UpdateEnvironmentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_configuration_name" in value:
        out["environment_configuration_name"] = "*** Sensitive Data Redacted ***"
    return out
