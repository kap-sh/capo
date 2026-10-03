"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorMetricConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.composite_sli_config
    import capo_application_signals.types.dependency_config
    import capo_application_signals.types.metric_data_queries
    import capo_application_signals.types.metric_name
    import capo_application_signals.types.metric_source
    import capo_application_signals.types.operation_name
    import capo_application_signals.types.service_level_indicator_metric_type
    import capo_application_signals.types.service_level_indicator_statistic
    import capo_application_signals.types.sli_period_seconds


class ServiceLevelIndicatorMetricConfig(TypedDict, closed=True):
    key_attributes: NotRequired["capo_application_signals.types.attributes.Attributes"]
    """<p>If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    operation_name: NotRequired[
        "capo_application_signals.types.operation_name.OperationName"
    ]
    """<p>If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.</p>"""
    metric_type: NotRequired[
        "capo_application_signals.types.service_level_indicator_metric_type.ServiceLevelIndicatorMetricType"
    ]
    """<p>If the SLO is to monitor either the <code>LATENCY</code> or <code>AVAILABILITY</code> metric that Application Signals collects, use this field to specify which of those metrics is used.</p>"""
    metric_name: NotRequired["capo_application_signals.types.metric_name.MetricName"]
    """<p>The name of the CloudWatch metric to use for the SLO, when using a custom metric rather than Application Signals standard metrics.</p>"""
    statistic: NotRequired[
        "capo_application_signals.types.service_level_indicator_statistic.ServiceLevelIndicatorStatistic"
    ]
    """<p>The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html">CloudWatch statistics definitions</a>.</p>"""
    period_seconds: NotRequired[
        "capo_application_signals.types.sli_period_seconds.SLIPeriodSeconds"
    ]
    """<p>The number of seconds to use as the period for SLO evaluation. Your application's performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.</p>"""
    metric_source: NotRequired[
        "capo_application_signals.types.metric_source.MetricSource"
    ]
    """<p>Identifies the metric source for SLOs on resources other than Application Signals services.</p>"""
    metric_data_queries: NotRequired[
        "capo_application_signals.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression. </p>"""
    dependency_config: NotRequired[
        "capo_application_signals.types.dependency_config.DependencyConfig"
    ]
    """<p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>"""
    composite_sli_config: NotRequired[
        "capo_application_signals.types.composite_sli_config.CompositeSliConfig"
    ]
    """<p>The composite SLI configuration for service-level SLOs that monitor multiple operations of a service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelIndicatorMetricConfig) -> dict:
    out: dict = {}
    if "key_attributes" in value:
        import capo_application_signals.types.attributes

        out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
            value["key_attributes"]
        )
    if "operation_name" in value:
        out["OperationName"] = value["operation_name"]
    if "metric_type" in value:
        import capo_application_signals.types.service_level_indicator_metric_type

        out["MetricType"] = (
            capo_application_signals.types.service_level_indicator_metric_type.serialize_json(
                value["metric_type"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "statistic" in value:
        out["Statistic"] = value["statistic"]
    if "period_seconds" in value:
        out["PeriodSeconds"] = value["period_seconds"]
    if "metric_source" in value:
        import capo_application_signals.types.metric_source

        out["MetricSource"] = (
            capo_application_signals.types.metric_source.serialize_json(
                value["metric_source"]
            )
        )
    if "metric_data_queries" in value:
        import capo_application_signals.types.metric_data_queries

        out["MetricDataQueries"] = (
            capo_application_signals.types.metric_data_queries.serialize_json(
                value["metric_data_queries"]
            )
        )
    if "dependency_config" in value:
        import capo_application_signals.types.dependency_config

        out["DependencyConfig"] = (
            capo_application_signals.types.dependency_config.serialize_json(
                value["dependency_config"]
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


def deserialize_json(data: dict) -> ServiceLevelIndicatorMetricConfig:
    out: ServiceLevelIndicatorMetricConfig = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    if data.get("OperationName") is not None:
        out["operation_name"] = data["OperationName"]
    if data.get("MetricType") is not None:
        import capo_application_signals.types.service_level_indicator_metric_type

        out["metric_type"] = (
            capo_application_signals.types.service_level_indicator_metric_type.deserialize_json(
                data["MetricType"]
            )
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Statistic") is not None:
        out["statistic"] = data["Statistic"]
    if data.get("PeriodSeconds") is not None:
        out["period_seconds"] = data["PeriodSeconds"]
    if data.get("MetricSource") is not None:
        import capo_application_signals.types.metric_source

        out["metric_source"] = (
            capo_application_signals.types.metric_source.deserialize_json(
                data["MetricSource"]
            )
        )
    if data.get("MetricDataQueries") is not None:
        import capo_application_signals.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_application_signals.types.metric_data_queries.deserialize_json(
                data["MetricDataQueries"]
            )
        )
    if data.get("DependencyConfig") is not None:
        import capo_application_signals.types.dependency_config

        out["dependency_config"] = (
            capo_application_signals.types.dependency_config.deserialize_json(
                data["DependencyConfig"]
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
