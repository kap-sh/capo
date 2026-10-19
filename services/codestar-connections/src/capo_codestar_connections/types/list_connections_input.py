"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.host_arn
    import capo_codestar_connections.types.max_results
    import capo_codestar_connections.types.next_token
    import capo_codestar_connections.types.provider_type


class ListConnectionsInput(TypedDict, closed=True):
    provider_type_filter: NotRequired[
        "capo_codestar_connections.types.provider_type.ProviderType"
    ]
    """<p>Filters the list of connections to those associated with a specified provider, such as Bitbucket.</p>"""
    host_arn_filter: NotRequired["capo_codestar_connections.types.host_arn.HostArn"]
    """<p>Filters the list of connections to those associated with a specified host.</p>"""
    max_results: NotRequired["capo_codestar_connections.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_codestar_connections.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListConnections</code> call, which can be used to return the next set of connections in the list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsInput) -> dict:
    out: dict = {}
    if "provider_type_filter" in value:
        import capo_codestar_connections.types.provider_type

        out["ProviderTypeFilter"] = (
            capo_codestar_connections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type_filter"]
            )
        )
    if "host_arn_filter" in value:
        out["HostArnFilter"] = value["host_arn_filter"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsInput:
    out: ListConnectionsInput = {}  # type: ignore[typeddict-item]
    if data.get("ProviderTypeFilter") is not None:
        import capo_codestar_connections.types.provider_type

        out["provider_type_filter"] = (
            capo_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderTypeFilter"]
            )
        )
    if data.get("HostArnFilter") is not None:
        out["host_arn_filter"] = data["HostArnFilter"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
