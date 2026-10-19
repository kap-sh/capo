"""Generated from Smithy shape ``com.amazonaws.configservice#StartRemediationExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.resource_keys


class StartRemediationExecutionRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The list of names of Config rules that you want to run remediation execution for.</p>"""
    resource_keys: "capo_config_service.types.resource_keys.ResourceKeys"
    """<p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemediationExecutionRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.resource_keys

    out["ResourceKeys"] = (
        capo_config_service.types.resource_keys.serialize_aws_json_1_1(
            value["resource_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemediationExecutionRequest:
    out: StartRemediationExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ResourceKeys") is not None:
        import capo_config_service.types.resource_keys

        out["resource_keys"] = (
            capo_config_service.types.resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    else:
        out["resource_keys"] = []
    return out
