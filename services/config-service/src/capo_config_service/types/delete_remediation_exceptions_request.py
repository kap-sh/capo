"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRemediationExceptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.remediation_exception_resource_keys


class DeleteRemediationExceptionsRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want to delete remediation exception configuration.</p>"""
    resource_keys: "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
    """<p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRemediationExceptionsRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.remediation_exception_resource_keys

    out["ResourceKeys"] = (
        capo_config_service.types.remediation_exception_resource_keys.serialize_aws_json_1_1(
            value["resource_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRemediationExceptionsRequest:
    out: DeleteRemediationExceptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("ResourceKeys") is not None:
        import capo_config_service.types.remediation_exception_resource_keys

        out["resource_keys"] = (
            capo_config_service.types.remediation_exception_resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    else:
        out["resource_keys"] = []
    return out
