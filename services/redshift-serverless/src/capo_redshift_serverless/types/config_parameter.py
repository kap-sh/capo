"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ConfigParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.parameter_key
    import capo_redshift_serverless.types.parameter_value


class ConfigParameter(TypedDict, closed=True):
    parameter_key: NotRequired[
        "capo_redshift_serverless.types.parameter_key.ParameterKey"
    ]
    """<p>The key of the parameter. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless">Query monitoring metrics for Amazon Redshift Serverless</a>.</p>"""
    parameter_value: NotRequired[
        "capo_redshift_serverless.types.parameter_value.ParameterValue"
    ]
    """<p>The value of the parameter to set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigParameter) -> dict:
    out: dict = {}
    if "parameter_key" in value:
        out["parameterKey"] = value["parameter_key"]
    if "parameter_value" in value:
        out["parameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigParameter:
    out: ConfigParameter = {}  # type: ignore[typeddict-item]
    if data.get("parameterKey") is not None:
        out["parameter_key"] = data["parameterKey"]
    if data.get("parameterValue") is not None:
        out["parameter_value"] = data["parameterValue"]
    return out
