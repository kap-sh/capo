"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingConfigurationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_name_list
    import capo_gamelift.types.matchmaking_rule_set_name
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeMatchmakingConfigurationsInput(TypedDict, closed=True):
    names: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_name_list.MatchmakingConfigurationNameList"
    ]
    """<p>A unique identifier for the matchmaking configuration(s) to retrieve. You can use either the configuration name or ARN value. To request all existing configurations, leave this parameter empty.</p>"""
    rule_set_name: NotRequired[
        "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
    ]
    """<p>A unique identifier for the matchmaking rule set. You can use either the rule set name or ARN value. Use this parameter to retrieve all matchmaking configurations that use this rule set.</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is limited to 10.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingConfigurationsInput) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_gamelift.types.matchmaking_configuration_name_list

        out["Names"] = (
            capo_gamelift.types.matchmaking_configuration_name_list.serialize_aws_json_1_1(
                value["names"]
            )
        )
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingConfigurationsInput:
    out: DescribeMatchmakingConfigurationsInput = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_gamelift.types.matchmaking_configuration_name_list

        out["names"] = (
            capo_gamelift.types.matchmaking_configuration_name_list.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMatchmakingConfigurationsInput) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_gamelift.types.matchmaking_configuration_name_list

        out["Names"] = (
            capo_gamelift.types.matchmaking_configuration_name_list.serialize_cbor(
                value["names"]
            )
        )
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeMatchmakingConfigurationsInput:
    out: DescribeMatchmakingConfigurationsInput = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_gamelift.types.matchmaking_configuration_name_list

        out["names"] = (
            capo_gamelift.types.matchmaking_configuration_name_list.deserialize_cbor(
                data["Names"]
            )
        )
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
