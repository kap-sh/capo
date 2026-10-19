"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_names


class DescribeRemediationConfigurationsRequest(TypedDict, closed=True):
    config_rule_names: "capo_config_service.types.config_rule_names.ConfigRuleNames"
    """<p>A list of Config rule names of remediation configurations for which you want details. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.config_rule_names

    out["ConfigRuleNames"] = (
        capo_config_service.types.config_rule_names.serialize_aws_json_1_1(
            value["config_rule_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationConfigurationsRequest:
    out: DescribeRemediationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleNames") is not None:
        import capo_config_service.types.config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    else:
        out["config_rule_names"] = []
    return out
