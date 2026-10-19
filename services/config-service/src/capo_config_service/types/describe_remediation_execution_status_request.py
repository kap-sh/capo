"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationExecutionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.limit
    import capo_config_service.types.resource_keys
    import capo_config_service.types.string


class DescribeRemediationExecutionStatusRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    resource_keys: NotRequired["capo_config_service.types.resource_keys.ResourceKeys"]
    """<p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID. </p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of RemediationExecutionStatuses returned on each page. The default is maximum. If you specify 0, Config uses the default. </p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationExecutionStatusRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    if "resource_keys" in value:
        import capo_config_service.types.resource_keys

        out["ResourceKeys"] = (
            capo_config_service.types.resource_keys.serialize_aws_json_1_1(
                value["resource_keys"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationExecutionStatusRequest:
    out: DescribeRemediationExecutionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "DescribeRemediationExecutionStatusRequest.config_rule_name required"
        )
    if data.get("ResourceKeys") is not None:
        import capo_config_service.types.resource_keys

        out["resource_keys"] = (
            capo_config_service.types.resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
