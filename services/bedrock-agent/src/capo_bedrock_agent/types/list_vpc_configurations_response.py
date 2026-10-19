"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListVpcConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.vpc_configuration_summary_list


class ListVpcConfigurationsResponse(TypedDict, closed=True):
    items: "capo_bedrock_agent.types.vpc_configuration_summary_list.VpcConfigurationSummaryList"
    """<p>A list of VPC configuration summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next page of results, present when the total number of results exceeds the maximum number of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.vpc_configuration_summary_list

    out["items"] = (
        capo_bedrock_agent.types.vpc_configuration_summary_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcConfigurationsResponse:
    out: ListVpcConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_bedrock_agent.types.vpc_configuration_summary_list

        out["items"] = (
            capo_bedrock_agent.types.vpc_configuration_summary_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
