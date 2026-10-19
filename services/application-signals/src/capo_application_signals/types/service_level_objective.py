"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjective``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.burn_rate_configurations
    import capo_application_signals.types.evaluation_type
    import capo_application_signals.types.goal
    import capo_application_signals.types.metric_source_type
    import capo_application_signals.types.request_based_service_level_indicator
    import capo_application_signals.types.service_level_indicator
    import capo_application_signals.types.service_level_objective_arn
    import capo_application_signals.types.service_level_objective_description
    import capo_application_signals.types.service_level_objective_name


class ServiceLevelObjective(TypedDict, closed=True):
    arn: "capo_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of this SLO.</p>"""
    name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of this SLO.</p>"""
    description: NotRequired[
        "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
    ]
    """<p>The description that you created for this SLO.</p>"""
    created_time: "datetime.datetime"
    """<p>The date and time that this SLO was created. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The time that this SLO was most recently updated. When used in a raw HTTP Query API, it is formatted as <code>yyyy-MM-dd'T'HH:mm:ss</code>. For example, <code>2019-07-01T23:59:59</code>.</p>"""
    sli: NotRequired[
        "capo_application_signals.types.service_level_indicator.ServiceLevelIndicator"
    ]
    """<p>A structure containing information about the performance metric that this SLO monitors, if this is a period-based SLO.</p>"""
    request_based_sli: NotRequired[
        "capo_application_signals.types.request_based_service_level_indicator.RequestBasedServiceLevelIndicator"
    ]
    """<p>A structure containing information about the performance metric that this SLO monitors, if this is a request-based SLO.</p>"""
    evaluation_type: NotRequired[
        "capo_application_signals.types.evaluation_type.EvaluationType"
    ]
    """<p>Displays whether this is a period-based SLO or a request-based SLO.</p>"""
    goal: "capo_application_signals.types.goal.Goal"
    burn_rate_configurations: NotRequired[
        "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
    ]
    """<p>Each object in this array defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>"""
    metric_source_type: NotRequired[
        "capo_application_signals.types.metric_source_type.MetricSourceType"
    ]
    """<p>Displays the SLI metric source type for this SLO. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>"""
    auto_investigation_enabled: NotRequired["bool"]
    """Indicates whether DevOps Agent will automatically investigate this SLO when it is breached"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjective) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_application_signals.types._prelude.timestamp

    out["CreatedTime"] = (
        capo_application_signals.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import capo_application_signals.types._prelude.timestamp

    out["LastUpdatedTime"] = (
        capo_application_signals.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    if "sli" in value:
        import capo_application_signals.types.service_level_indicator

        out["Sli"] = (
            capo_application_signals.types.service_level_indicator.serialize_json(
                value["sli"]
            )
        )
    if "request_based_sli" in value:
        import capo_application_signals.types.request_based_service_level_indicator

        out["RequestBasedSli"] = (
            capo_application_signals.types.request_based_service_level_indicator.serialize_json(
                value["request_based_sli"]
            )
        )
    if "evaluation_type" in value:
        import capo_application_signals.types.evaluation_type

        out["EvaluationType"] = (
            capo_application_signals.types.evaluation_type.serialize_json(
                value["evaluation_type"]
            )
        )
    import capo_application_signals.types.goal

    out["Goal"] = capo_application_signals.types.goal.serialize_json(value["goal"])
    if "burn_rate_configurations" in value:
        import capo_application_signals.types.burn_rate_configurations

        out["BurnRateConfigurations"] = (
            capo_application_signals.types.burn_rate_configurations.serialize_json(
                value["burn_rate_configurations"]
            )
        )
    if "metric_source_type" in value:
        import capo_application_signals.types.metric_source_type

        out["MetricSourceType"] = (
            capo_application_signals.types.metric_source_type.serialize_json(
                value["metric_source_type"]
            )
        )
    if "auto_investigation_enabled" in value:
        out["AutoInvestigationEnabled"] = value["auto_investigation_enabled"]
    return out


def deserialize_json(data: dict) -> ServiceLevelObjective:
    out: ServiceLevelObjective = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["created_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Sli") is not None:
        import capo_application_signals.types.service_level_indicator

        out["sli"] = (
            capo_application_signals.types.service_level_indicator.deserialize_json(
                data["Sli"]
            )
        )
    if data.get("RequestBasedSli") is not None:
        import capo_application_signals.types.request_based_service_level_indicator

        out["request_based_sli"] = (
            capo_application_signals.types.request_based_service_level_indicator.deserialize_json(
                data["RequestBasedSli"]
            )
        )
    if data.get("EvaluationType") is not None:
        import capo_application_signals.types.evaluation_type

        out["evaluation_type"] = (
            capo_application_signals.types.evaluation_type.deserialize_json(
                data["EvaluationType"]
            )
        )
    if data.get("Goal") is not None:
        import capo_application_signals.types.goal

        out["goal"] = capo_application_signals.types.goal.deserialize_json(data["Goal"])
    else:
        raise DeserializationError("ServiceLevelObjective.goal required")
    if data.get("BurnRateConfigurations") is not None:
        import capo_application_signals.types.burn_rate_configurations

        out["burn_rate_configurations"] = (
            capo_application_signals.types.burn_rate_configurations.deserialize_json(
                data["BurnRateConfigurations"]
            )
        )
    if data.get("MetricSourceType") is not None:
        import capo_application_signals.types.metric_source_type

        out["metric_source_type"] = (
            capo_application_signals.types.metric_source_type.deserialize_json(
                data["MetricSourceType"]
            )
        )
    if data.get("AutoInvestigationEnabled") is not None:
        out["auto_investigation_enabled"] = data["AutoInvestigationEnabled"]
    return out
