"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.resource_type
    import capo_observabilityadmin.types.rule_name
    import capo_observabilityadmin.types.telemetry_source_types
    import capo_observabilityadmin.types.telemetry_type


class TelemetryRuleSummary(TypedDict, closed=True):
    rule_name: NotRequired["capo_observabilityadmin.types.rule_name.RuleName"]
    """<p> The name of the telemetry rule. </p>"""
    rule_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the telemetry rule. </p>"""
    created_time_stamp: NotRequired["int"]
    """<p> The timestamp when the telemetry rule was created. </p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p> The timestamp when the telemetry rule was last modified. </p>"""
    resource_type: NotRequired[
        "capo_observabilityadmin.types.resource_type.ResourceType"
    ]
    """<p> The type of Amazon Web Services resource the rule applies to. </p>"""
    telemetry_type: NotRequired[
        "capo_observabilityadmin.types.telemetry_type.TelemetryType"
    ]
    """<p> The type of telemetry (Logs, Metrics, Traces, or Insights) the rule configures. </p>"""
    telemetry_source_types: NotRequired[
        "capo_observabilityadmin.types.telemetry_source_types.TelemetrySourceTypes"
    ]
    """<p> The types of telemetry sources configured for this rule, such as VPC Flow Logs or EKS audit logs. TelemetrySourceTypes must be correlated with the specific resource type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRuleSummary) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "resource_type" in value:
        import capo_observabilityadmin.types.resource_type

        out["ResourceType"] = (
            capo_observabilityadmin.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "telemetry_type" in value:
        import capo_observabilityadmin.types.telemetry_type

        out["TelemetryType"] = (
            capo_observabilityadmin.types.telemetry_type.serialize_json(
                value["telemetry_type"]
            )
        )
    if "telemetry_source_types" in value:
        import capo_observabilityadmin.types.telemetry_source_types

        out["TelemetrySourceTypes"] = (
            capo_observabilityadmin.types.telemetry_source_types.serialize_json(
                value["telemetry_source_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryRuleSummary:
    out: TelemetryRuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    if data.get("CreatedTimeStamp") is not None:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if data.get("LastUpdateTimeStamp") is not None:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if data.get("ResourceType") is not None:
        import capo_observabilityadmin.types.resource_type

        out["resource_type"] = (
            capo_observabilityadmin.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if data.get("TelemetryType") is not None:
        import capo_observabilityadmin.types.telemetry_type

        out["telemetry_type"] = (
            capo_observabilityadmin.types.telemetry_type.deserialize_json(
                data["TelemetryType"]
            )
        )
    if data.get("TelemetrySourceTypes") is not None:
        import capo_observabilityadmin.types.telemetry_source_types

        out["telemetry_source_types"] = (
            capo_observabilityadmin.types.telemetry_source_types.deserialize_json(
                data["TelemetrySourceTypes"]
            )
        )
    return out
