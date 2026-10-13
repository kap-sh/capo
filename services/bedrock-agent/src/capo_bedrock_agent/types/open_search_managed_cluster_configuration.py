"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OpenSearchManagedClusterConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.open_search_managed_cluster_domain_arn
    import capo_bedrock_agent.types.open_search_managed_cluster_domain_endpoint
    import capo_bedrock_agent.types.open_search_managed_cluster_field_mapping
    import capo_bedrock_agent.types.open_search_managed_cluster_index_name


class OpenSearchManagedClusterConfiguration(TypedDict, closed=True):
    domain_endpoint: "capo_bedrock_agent.types.open_search_managed_cluster_domain_endpoint.OpenSearchManagedClusterDomainEndpoint"
    """<p>The endpoint URL the OpenSearch domain.</p>"""
    domain_arn: "capo_bedrock_agent.types.open_search_managed_cluster_domain_arn.OpenSearchManagedClusterDomainArn"
    """<p>The Amazon Resource Name (ARN) of the OpenSearch domain.</p>"""
    vector_index_name: "capo_bedrock_agent.types.open_search_managed_cluster_index_name.OpenSearchManagedClusterIndexName"
    """<p>The name of the vector store.</p>"""
    field_mapping: "capo_bedrock_agent.types.open_search_managed_cluster_field_mapping.OpenSearchManagedClusterFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchManagedClusterConfiguration) -> dict:
    out: dict = {}
    out["domainEndpoint"] = value["domain_endpoint"]
    out["domainArn"] = value["domain_arn"]
    out["vectorIndexName"] = value["vector_index_name"]
    import capo_bedrock_agent.types.open_search_managed_cluster_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.open_search_managed_cluster_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> OpenSearchManagedClusterConfiguration:
    out: OpenSearchManagedClusterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("domainEndpoint") is not None:
        out["domain_endpoint"] = data["domainEndpoint"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterConfiguration.domain_endpoint required"
        )
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterConfiguration.domain_arn required"
        )
    if data.get("vectorIndexName") is not None:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterConfiguration.vector_index_name required"
        )
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.open_search_managed_cluster_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.open_search_managed_cluster_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "OpenSearchManagedClusterConfiguration.field_mapping required"
        )
    return out


def redact_sensitive(value: OpenSearchManagedClusterConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vector_index_name" in value:
        out["vector_index_name"] = "*** Sensitive Data Redacted ***"
    return out
