"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListRepositorySyncDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.repository_sync_definition_list
    import capo_codestar_connections.types.sharp_next_token


class ListRepositorySyncDefinitionsOutput(TypedDict, closed=True):
    repository_sync_definitions: "capo_codestar_connections.types.repository_sync_definition_list.RepositorySyncDefinitionList"
    """<p>The list of repository sync definitions returned by the request. A <code>RepositorySyncDefinition</code> is a mapping from a repository branch to all the Amazon Web Services resources that are being synced from that branch.</p>"""
    next_token: NotRequired[
        "capo_codestar_connections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositorySyncDefinitionsOutput) -> dict:
    out: dict = {}
    import capo_codestar_connections.types.repository_sync_definition_list

    out["RepositorySyncDefinitions"] = (
        capo_codestar_connections.types.repository_sync_definition_list.serialize_aws_json_1_0(
            value["repository_sync_definitions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositorySyncDefinitionsOutput:
    out: ListRepositorySyncDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RepositorySyncDefinitions") is not None:
        import capo_codestar_connections.types.repository_sync_definition_list

        out["repository_sync_definitions"] = (
            capo_codestar_connections.types.repository_sync_definition_list.deserialize_aws_json_1_0(
                data["RepositorySyncDefinitions"]
            )
        )
    else:
        out["repository_sync_definitions"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
