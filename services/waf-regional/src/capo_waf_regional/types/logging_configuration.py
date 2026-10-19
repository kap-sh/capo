"""Generated from Smithy shape ``com.amazonaws.wafregional#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.log_destination_configs
    import capo_waf_regional.types.redacted_fields
    import capo_waf_regional.types.resource_arn


class LoggingConfiguration(TypedDict, closed=True):
    resource_arn: "capo_waf_regional.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with <code>LogDestinationConfigs</code>.</p>"""
    log_destination_configs: (
        "capo_waf_regional.types.log_destination_configs.LogDestinationConfigs"
    )
    """<p>An array of Amazon Kinesis Data Firehose ARNs.</p>"""
    redacted_fields: NotRequired[
        "capo_waf_regional.types.redacted_fields.RedactedFields"
    ]
    """<p>The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be <code>xxx</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfiguration) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_waf_regional.types.log_destination_configs

    out["LogDestinationConfigs"] = (
        capo_waf_regional.types.log_destination_configs.serialize_aws_json_1_1(
            value["log_destination_configs"]
        )
    )
    if "redacted_fields" in value:
        import capo_waf_regional.types.redacted_fields

        out["RedactedFields"] = (
            capo_waf_regional.types.redacted_fields.serialize_aws_json_1_1(
                value["redacted_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("LogDestinationConfigs") is not None:
        import capo_waf_regional.types.log_destination_configs

        out["log_destination_configs"] = (
            capo_waf_regional.types.log_destination_configs.deserialize_aws_json_1_1(
                data["LogDestinationConfigs"]
            )
        )
    else:
        out["log_destination_configs"] = []
    if data.get("RedactedFields") is not None:
        import capo_waf_regional.types.redacted_fields

        out["redacted_fields"] = (
            capo_waf_regional.types.redacted_fields.deserialize_aws_json_1_1(
                data["RedactedFields"]
            )
        )
    return out
