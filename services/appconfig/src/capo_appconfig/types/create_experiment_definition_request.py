"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateExperimentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.flag_key
    import capo_appconfig.types.identifier
    import capo_appconfig.types.name_with_reserved_aws_prefix
    import capo_appconfig.types.rule
    import capo_appconfig.types.tag_map
    import capo_appconfig.types.treatment_input
    import capo_appconfig.types.treatment_input_list


class CreateExperimentDefinitionRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    name: "capo_appconfig.types.name_with_reserved_aws_prefix.NameWithReservedAwsPrefix"
    """<p>A name for the experiment definition.</p>"""
    configuration_profile_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The configuration profile ID or name that stores the feature flag.</p>"""
    environment_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The environment ID or name where the experiment will run.</p>"""
    flag_key: "capo_appconfig.types.flag_key.FlagKey"
    """<p>The key of the existing feature flag to use with the experiment.</p>"""
    treatments: "capo_appconfig.types.treatment_input_list.TreatmentInputList"
    """<p>A list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.</p>"""
    control: "capo_appconfig.types.treatment_input.TreatmentInput"
    """<p>The control treatment that represents the baseline experience for comparison.</p>"""
    audience_rule: "capo_appconfig.types.rule.Rule"
    """<p>A rule that defines which users are eligible to be assigned to treatments during the experiment.</p>"""
    hypothesis: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the goal or hypothesis the experiment is designed to validate.</p>"""
    audience_description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the intended audience for the experiment.</p>"""
    launch_criteria: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Information about the conditions under which you would launch the winning treatment.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>The tags to assign to the experiment definition. Tags help organize and categorize your AppConfig resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentDefinitionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConfigurationProfileIdentifier"] = value["configuration_profile_identifier"]
    out["EnvironmentIdentifier"] = value["environment_identifier"]
    out["FlagKey"] = value["flag_key"]
    import capo_appconfig.types.treatment_input_list

    out["Treatments"] = capo_appconfig.types.treatment_input_list.serialize_json(
        value["treatments"]
    )
    import capo_appconfig.types.treatment_input

    out["Control"] = capo_appconfig.types.treatment_input.serialize_json(
        value["control"]
    )
    out["AudienceRule"] = value["audience_rule"]
    if "hypothesis" in value:
        out["Hypothesis"] = value["hypothesis"]
    if "audience_description" in value:
        out["AudienceDescription"] = value["audience_description"]
    if "launch_criteria" in value:
        out["LaunchCriteria"] = value["launch_criteria"]
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExperimentDefinitionRequest:
    out: CreateExperimentDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ConfigurationProfileIdentifier") is not None:
        out["configuration_profile_identifier"] = data["ConfigurationProfileIdentifier"]
    else:
        out["configuration_profile_identifier"] = ""
    if data.get("EnvironmentIdentifier") is not None:
        out["environment_identifier"] = data["EnvironmentIdentifier"]
    else:
        out["environment_identifier"] = ""
    if data.get("FlagKey") is not None:
        out["flag_key"] = data["FlagKey"]
    else:
        out["flag_key"] = ""
    if data.get("Treatments") is not None:
        import capo_appconfig.types.treatment_input_list

        out["treatments"] = capo_appconfig.types.treatment_input_list.deserialize_json(
            data["Treatments"]
        )
    else:
        out["treatments"] = []
    if data.get("Control") is not None:
        import capo_appconfig.types.treatment_input

        out["control"] = capo_appconfig.types.treatment_input.deserialize_json(
            data["Control"]
        )
    else:
        raise DeserializationError("CreateExperimentDefinitionRequest.control required")
    if data.get("AudienceRule") is not None:
        out["audience_rule"] = data["AudienceRule"]
    else:
        out["audience_rule"] = ""
    if data.get("Hypothesis") is not None:
        out["hypothesis"] = data["Hypothesis"]
    if data.get("AudienceDescription") is not None:
        out["audience_description"] = data["AudienceDescription"]
    if data.get("LaunchCriteria") is not None:
        out["launch_criteria"] = data["LaunchCriteria"]
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
