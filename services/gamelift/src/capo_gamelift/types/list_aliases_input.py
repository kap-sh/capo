"""Generated from Smithy shape ``com.amazonaws.gamelift#ListAliasesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.routing_strategy_type


class ListAliasesInput(TypedDict, closed=True):
    routing_strategy_type: NotRequired[
        "capo_gamelift.types.routing_strategy_type.RoutingStrategyType"
    ]
    """<p>The routing type to filter results on. Use this parameter to retrieve only aliases with a certain routing type. To retrieve all aliases, leave this parameter empty.</p> <p>Possible routing types include the following:</p> <ul> <li> <p> <b>SIMPLE</b> -- The alias resolves to one specific fleet. Use this type when routing to active fleets.</p> </li> <li> <p> <b>TERMINAL</b> -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_RoutingStrategy.html">RoutingStrategy</a> message embedded.</p> </li> </ul>"""
    name: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesInput) -> dict:
    out: dict = {}
    if "routing_strategy_type" in value:
        import capo_gamelift.types.routing_strategy_type

        out["RoutingStrategyType"] = (
            capo_gamelift.types.routing_strategy_type.serialize_aws_json_1_1(
                value["routing_strategy_type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesInput:
    out: ListAliasesInput = {}  # type: ignore[typeddict-item]
    if data.get("RoutingStrategyType") is not None:
        import capo_gamelift.types.routing_strategy_type

        out["routing_strategy_type"] = (
            capo_gamelift.types.routing_strategy_type.deserialize_aws_json_1_1(
                data["RoutingStrategyType"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
