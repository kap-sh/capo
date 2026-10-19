"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CreateServiceLevelObjectiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.burn_rate_configurations
    import capo_application_signals.types.goal
    import capo_application_signals.types.request_based_service_level_indicator_config
    import capo_application_signals.types.service_level_indicator_config
    import capo_application_signals.types.service_level_objective_description
    import capo_application_signals.types.service_level_objective_name
    import capo_application_signals.types.tag_list


class CreateServiceLevelObjectiveInput(TypedDict, closed=True):
    name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>A name for this SLO.</p>"""
    description: NotRequired[
        "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
    ]
    """<p>An optional description for this SLO.</p>"""
    sli_config: NotRequired[
        "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
    ]
    """<p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>"""
    request_based_sli_config: NotRequired[
        "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
    ]
    """<p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>"""
    goal: NotRequired["capo_application_signals.types.goal.Goal"]
    """<p>This structure contains the attributes that determine the goal of the SLO.</p>"""
    tags: NotRequired["capo_application_signals.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>"""
    burn_rate_configurations: NotRequired[
        "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
    ]
    """<p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>"""
    create_recommended_slo: NotRequired["bool"]
    """<p>Set this to <code>true</code> to create a recommended SLO out of the box. When set to <code>true</code>, you don't need to specify the <code>MetricThreshold</code> or <code>ComparisonOperator</code> in the <code>SliConfig</code> or <code>RequestBasedSliConfig</code>. The default value is <code>false</code>.</p> <p>This is supported for SLOs on a service, service operation, or a dependency.</p>"""
    auto_investigation_enabled: NotRequired["bool"]
    """Indicates whether DevOps Agent will automatically investigate this SLO when it is breached"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceLevelObjectiveInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "sli_config" in value:
        import capo_application_signals.types.service_level_indicator_config

        out["SliConfig"] = (
            capo_application_signals.types.service_level_indicator_config.serialize_json(
                value["sli_config"]
            )
        )
    if "request_based_sli_config" in value:
        import capo_application_signals.types.request_based_service_level_indicator_config

        out["RequestBasedSliConfig"] = (
            capo_application_signals.types.request_based_service_level_indicator_config.serialize_json(
                value["request_based_sli_config"]
            )
        )
    if "goal" in value:
        import capo_application_signals.types.goal

        out["Goal"] = capo_application_signals.types.goal.serialize_json(value["goal"])
    if "tags" in value:
        import capo_application_signals.types.tag_list

        out["Tags"] = capo_application_signals.types.tag_list.serialize_json(
            value["tags"]
        )
    if "burn_rate_configurations" in value:
        import capo_application_signals.types.burn_rate_configurations

        out["BurnRateConfigurations"] = (
            capo_application_signals.types.burn_rate_configurations.serialize_json(
                value["burn_rate_configurations"]
            )
        )
    if "create_recommended_slo" in value:
        out["CreateRecommendedSlo"] = value["create_recommended_slo"]
    if "auto_investigation_enabled" in value:
        out["AutoInvestigationEnabled"] = value["auto_investigation_enabled"]
    return out


def deserialize_json(data: dict) -> CreateServiceLevelObjectiveInput:
    out: CreateServiceLevelObjectiveInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SliConfig") is not None:
        import capo_application_signals.types.service_level_indicator_config

        out["sli_config"] = (
            capo_application_signals.types.service_level_indicator_config.deserialize_json(
                data["SliConfig"]
            )
        )
    if data.get("RequestBasedSliConfig") is not None:
        import capo_application_signals.types.request_based_service_level_indicator_config

        out["request_based_sli_config"] = (
            capo_application_signals.types.request_based_service_level_indicator_config.deserialize_json(
                data["RequestBasedSliConfig"]
            )
        )
    if data.get("Goal") is not None:
        import capo_application_signals.types.goal

        out["goal"] = capo_application_signals.types.goal.deserialize_json(data["Goal"])
    if data.get("Tags") is not None:
        import capo_application_signals.types.tag_list

        out["tags"] = capo_application_signals.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("BurnRateConfigurations") is not None:
        import capo_application_signals.types.burn_rate_configurations

        out["burn_rate_configurations"] = (
            capo_application_signals.types.burn_rate_configurations.deserialize_json(
                data["BurnRateConfigurations"]
            )
        )
    if data.get("CreateRecommendedSlo") is not None:
        out["create_recommended_slo"] = data["CreateRecommendedSlo"]
    if data.get("AutoInvestigationEnabled") is not None:
        out["auto_investigation_enabled"] = data["AutoInvestigationEnabled"]
    return out
