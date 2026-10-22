"""Generated from Smithy shape ``com.amazonaws.elasticache#PrepareMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.customer_node_endpoint_list
    import capo_elasticache.types.source_authentication_configuration
    import capo_elasticache.types.source_tls_configuration
    import capo_elasticache.types.string


class PrepareMigrationRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the serverless cache to prepare for migration.</p>"""
    customer_node_endpoint_list: NotRequired[
        "capo_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
    ]
    """<p>The list of endpoints from which to migrate data. For serverless cache migrations, the list should have only one element.</p>"""
    source_authentication_configuration: NotRequired[
        "capo_elasticache.types.source_authentication_configuration.SourceAuthenticationConfiguration"
    ]
    """<p>The authentication configuration for connecting to the source during migration.</p>"""
    source_tls_configuration: NotRequired[
        "capo_elasticache.types.source_tls_configuration.SourceTlsConfiguration"
    ]
    """<p>The TLS configuration for connecting to the source during migration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PrepareMigrationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "customer_node_endpoint_list" in value:
        import capo_elasticache.types.customer_node_endpoint_list

        capo_elasticache.types.customer_node_endpoint_list.serialize_query(
            value["customer_node_endpoint_list"],
            pairs,
            f"{key_prefix}CustomerNodeEndpointList",
        )
    if "source_authentication_configuration" in value:
        import capo_elasticache.types.source_authentication_configuration

        capo_elasticache.types.source_authentication_configuration.serialize_query(
            value["source_authentication_configuration"],
            pairs,
            f"{key_prefix}SourceAuthenticationConfiguration",
        )
    if "source_tls_configuration" in value:
        import capo_elasticache.types.source_tls_configuration

        capo_elasticache.types.source_tls_configuration.serialize_query(
            value["source_tls_configuration"],
            pairs,
            f"{key_prefix}SourceTlsConfiguration",
        )


def deserialize_query(el: Element) -> PrepareMigrationRequest:
    out: PrepareMigrationRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_customer_node_endpoint_list = el.find("CustomerNodeEndpointList")
    if child_customer_node_endpoint_list is not None:
        import capo_elasticache.types.customer_node_endpoint_list

        out["customer_node_endpoint_list"] = (
            capo_elasticache.types.customer_node_endpoint_list.deserialize_query(
                child_customer_node_endpoint_list
            )
        )
    child_source_authentication_configuration = el.find(
        "SourceAuthenticationConfiguration"
    )
    if child_source_authentication_configuration is not None:
        import capo_elasticache.types.source_authentication_configuration

        out["source_authentication_configuration"] = (
            capo_elasticache.types.source_authentication_configuration.deserialize_query(
                child_source_authentication_configuration
            )
        )
    child_source_tls_configuration = el.find("SourceTlsConfiguration")
    if child_source_tls_configuration is not None:
        import capo_elasticache.types.source_tls_configuration

        out["source_tls_configuration"] = (
            capo_elasticache.types.source_tls_configuration.deserialize_query(
                child_source_tls_configuration
            )
        )
    return out
