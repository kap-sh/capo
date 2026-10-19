"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.attributes
    import capo_application_signals.types.composite_sli_config
    import capo_application_signals.types.dependency_config
    import capo_application_signals.types.evaluation_type
    import capo_application_signals.types.metric_source
    import capo_application_signals.types.metric_source_type
    import capo_application_signals.types.operation_name
    import capo_application_signals.types.service_level_objective_arn
    import capo_application_signals.types.service_level_objective_name


class ServiceLevelObjectiveSummary(TypedDict, closed=True):
    arn: "capo_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of this service level objective.</p>"""
    name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of the service level objective.</p>"""
    key_attributes: NotRequired["capo_application_signals.types.attributes.Attributes"]
    """<p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this service level objective is for.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    operation_name: NotRequired[
        "capo_application_signals.types.operation_name.OperationName"
    ]
    """<p>If this service level objective is specific to a single operation, this field displays the name of that operation.</p>"""
    dependency_config: NotRequired[
        "capo_application_signals.types.dependency_config.DependencyConfig"
    ]
    """<p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The date and time that this service level objective was created. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    evaluation_type: NotRequired[
        "capo_application_signals.types.evaluation_type.EvaluationType"
    ]
    """<p>Displays whether this is a period-based SLO or a request-based SLO.</p>"""
    metric_source_type: NotRequired[
        "capo_application_signals.types.metric_source_type.MetricSourceType"
    ]
    """<p>Displays the SLI metric source type for this SLO. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>"""
    metric_source: NotRequired[
        "capo_application_signals.types.metric_source.MetricSource"
    ]
    """<p>Identifies the metric source for SLOs on resources other than Application Signals services.</p>"""
    composite_sli_config: NotRequired[
        "capo_application_signals.types.composite_sli_config.CompositeSliConfig"
    ]
    """<p>The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "key_attributes" in value:
        import capo_application_signals.types.attributes

        out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
            value["key_attributes"]
        )
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    if "dependency_config" in value:
        import capo_application_signals.types.dependency_config

        out["DependencyConfig"] = (
            capo_application_signals.types.dependency_config.serialize_json(
                value["dependency_config"]
            )
        )
    if "created_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["CreatedTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["created_time"]
            )
        )
    if "evaluation_type" in value:
        import capo_application_signals.types.evaluation_type

        out["EvaluationType"] = (
            capo_application_signals.types.evaluation_type.serialize_json(
                value["evaluation_type"]
            )
        )
    if "metric_source_type" in value:
        import capo_application_signals.types.metric_source_type

        out["MetricSourceType"] = (
            capo_application_signals.types.metric_source_type.serialize_json(
                value["metric_source_type"]
            )
        )
    if "metric_source" in value:
        import capo_application_signals.types.metric_source

        out["MetricSource"] = (
            capo_application_signals.types.metric_source.serialize_json(
                value["metric_source"]
            )
        )
    if "composite_sli_config" in value:
        import capo_application_signals.types.composite_sli_config

        out["CompositeSliConfig"] = (
            capo_application_signals.types.composite_sli_config.serialize_json(
                value["composite_sli_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceLevelObjectiveSummary:
    out: ServiceLevelObjectiveSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    if data.get("OperationName") is not None:
        out["operation_name"] = data["OperationName"]
    if data.get("DependencyConfig") is not None:
        import capo_application_signals.types.dependency_config

        out["dependency_config"] = (
            capo_application_signals.types.dependency_config.deserialize_json(
                data["DependencyConfig"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["created_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["CreatedTime"]
            )
        )
    if data.get("EvaluationType") is not None:
        import capo_application_signals.types.evaluation_type

        out["evaluation_type"] = (
            capo_application_signals.types.evaluation_type.deserialize_json(
                data["EvaluationType"]
            )
        )
    if data.get("MetricSourceType") is not None:
        import capo_application_signals.types.metric_source_type

        out["metric_source_type"] = (
            capo_application_signals.types.metric_source_type.deserialize_json(
                data["MetricSourceType"]
            )
        )
    if data.get("MetricSource") is not None:
        import capo_application_signals.types.metric_source

        out["metric_source"] = (
            capo_application_signals.types.metric_source.deserialize_json(
                data["MetricSource"]
            )
        )
    if data.get("CompositeSliConfig") is not None:
        import capo_application_signals.types.composite_sli_config

        out["composite_sli_config"] = (
            capo_application_signals.types.composite_sli_config.deserialize_json(
                data["CompositeSliConfig"]
            )
        )
    return out
