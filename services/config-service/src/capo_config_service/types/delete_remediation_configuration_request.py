"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRemediationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.string


class DeleteRemediationConfigurationRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want to delete remediation configuration.</p>"""
    resource_type: NotRequired["capo_config_service.types.string.String"]
    """<p>The type of a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRemediationConfigurationRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRemediationConfigurationRequest:
    out: DeleteRemediationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out
