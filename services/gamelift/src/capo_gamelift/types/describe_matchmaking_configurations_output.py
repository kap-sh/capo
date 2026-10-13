"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingConfigurationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeMatchmakingConfigurationsOutput(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_list.MatchmakingConfigurationList"
    ]
    """<p>A collection of requested matchmaking configurations.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingConfigurationsOutput) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_gamelift.types.matchmaking_configuration_list

        out["Configurations"] = (
            capo_gamelift.types.matchmaking_configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingConfigurationsOutput:
    out: DescribeMatchmakingConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Configurations") is not None:
        import capo_gamelift.types.matchmaking_configuration_list

        out["configurations"] = (
            capo_gamelift.types.matchmaking_configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeMatchmakingConfigurationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configurations" in value:
        import capo_gamelift.types.matchmaking_configuration_list

        out["configurations"] = (
            capo_gamelift.types.matchmaking_configuration_list.redact_sensitive(
                value["configurations"]
            )
        )
    return out
