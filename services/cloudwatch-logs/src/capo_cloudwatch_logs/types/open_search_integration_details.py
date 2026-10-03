"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchIntegrationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.open_search_application
    import capo_cloudwatch_logs.types.open_search_collection
    import capo_cloudwatch_logs.types.open_search_data_access_policy
    import capo_cloudwatch_logs.types.open_search_data_source
    import capo_cloudwatch_logs.types.open_search_encryption_policy
    import capo_cloudwatch_logs.types.open_search_lifecycle_policy
    import capo_cloudwatch_logs.types.open_search_network_policy
    import capo_cloudwatch_logs.types.open_search_workspace


class OpenSearchIntegrationDetails(TypedDict, closed=True):
    data_source: NotRequired[
        "capo_cloudwatch_logs.types.open_search_data_source.OpenSearchDataSource"
    ]
    """<p>This structure contains information about the OpenSearch Service data source used for this integration. This data source was created as part of the integration setup. An OpenSearch Service data source defines the source and destination for OpenSearch Service queries. It includes the role required to execute queries and write to collections.</p> <p>For more information about OpenSearch Service data sources , see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html">Creating OpenSearch Service data source integrations with Amazon S3.</a> </p>"""
    application: NotRequired[
        "capo_cloudwatch_logs.types.open_search_application.OpenSearchApplication"
    ]
    """<p>This structure contains information about the OpenSearch Service application used for this integration. An OpenSearch Service application is the web application that was created by the integration with CloudWatch Logs. It hosts the vended logs dashboards.</p>"""
    collection: NotRequired[
        "capo_cloudwatch_logs.types.open_search_collection.OpenSearchCollection"
    ]
    """<p>This structure contains information about the OpenSearch Service collection used for this integration. This collection was created as part of the integration setup. An OpenSearch Service collection is a logical grouping of one or more indexes that represent an analytics workload. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html">Creating and managing OpenSearch Service Serverless collections</a>.</p>"""
    workspace: NotRequired[
        "capo_cloudwatch_logs.types.open_search_workspace.OpenSearchWorkspace"
    ]
    """<p>This structure contains information about the OpenSearch Service workspace used for this integration. An OpenSearch Service workspace is the collection of dashboards along with other OpenSearch Service tools. This workspace was created automatically as part of the integration setup. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html">Centralized OpenSearch user interface (Dashboards) with OpenSearch Service</a>.</p>"""
    encryption_policy: NotRequired[
        "capo_cloudwatch_logs.types.open_search_encryption_policy.OpenSearchEncryptionPolicy"
    ]
    """<p>This structure contains information about the OpenSearch Service encryption policy used for this integration. The encryption policy was created automatically when you created the integration. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html#serverless-encryption-policies">Encryption policies</a> in the OpenSearch Service Developer Guide. </p>"""
    network_policy: NotRequired[
        "capo_cloudwatch_logs.types.open_search_network_policy.OpenSearchNetworkPolicy"
    ]
    """<p>This structure contains information about the OpenSearch Service network policy used for this integration. The network policy assigns network access settings to collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html#serverless-network-policies">Network policies</a> in the OpenSearch Service Developer Guide.</p>"""
    access_policy: NotRequired[
        "capo_cloudwatch_logs.types.open_search_data_access_policy.OpenSearchDataAccessPolicy"
    ]
    """<p>This structure contains information about the OpenSearch Service data access policy used for this integration. The access policy defines the access controls for the collection. This data access policy was automatically created as part of the integration setup. For more information about OpenSearch Service data access policies, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html">Data access control for Amazon OpenSearch Serverless</a> in the OpenSearch Service Developer Guide.</p>"""
    lifecycle_policy: NotRequired[
        "capo_cloudwatch_logs.types.open_search_lifecycle_policy.OpenSearchLifecyclePolicy"
    ]
    """<p>This structure contains information about the OpenSearch Service data lifecycle policy used for this integration. The lifecycle policy determines the lifespan of the data in the collection. It was automatically created as part of the integration setup.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html">Using data lifecycle policies with OpenSearch Service Serverless</a> in the OpenSearch Service Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchIntegrationDetails) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_cloudwatch_logs.types.open_search_data_source

        out["dataSource"] = (
            capo_cloudwatch_logs.types.open_search_data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "application" in value:
        import capo_cloudwatch_logs.types.open_search_application

        out["application"] = (
            capo_cloudwatch_logs.types.open_search_application.serialize_aws_json_1_1(
                value["application"]
            )
        )
    if "collection" in value:
        import capo_cloudwatch_logs.types.open_search_collection

        out["collection"] = (
            capo_cloudwatch_logs.types.open_search_collection.serialize_aws_json_1_1(
                value["collection"]
            )
        )
    if "workspace" in value:
        import capo_cloudwatch_logs.types.open_search_workspace

        out["workspace"] = (
            capo_cloudwatch_logs.types.open_search_workspace.serialize_aws_json_1_1(
                value["workspace"]
            )
        )
    if "encryption_policy" in value:
        import capo_cloudwatch_logs.types.open_search_encryption_policy

        out["encryptionPolicy"] = (
            capo_cloudwatch_logs.types.open_search_encryption_policy.serialize_aws_json_1_1(
                value["encryption_policy"]
            )
        )
    if "network_policy" in value:
        import capo_cloudwatch_logs.types.open_search_network_policy

        out["networkPolicy"] = (
            capo_cloudwatch_logs.types.open_search_network_policy.serialize_aws_json_1_1(
                value["network_policy"]
            )
        )
    if "access_policy" in value:
        import capo_cloudwatch_logs.types.open_search_data_access_policy

        out["accessPolicy"] = (
            capo_cloudwatch_logs.types.open_search_data_access_policy.serialize_aws_json_1_1(
                value["access_policy"]
            )
        )
    if "lifecycle_policy" in value:
        import capo_cloudwatch_logs.types.open_search_lifecycle_policy

        out["lifecyclePolicy"] = (
            capo_cloudwatch_logs.types.open_search_lifecycle_policy.serialize_aws_json_1_1(
                value["lifecycle_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchIntegrationDetails:
    out: OpenSearchIntegrationDetails = {}  # type: ignore[typeddict-item]
    if data.get("dataSource") is not None:
        import capo_cloudwatch_logs.types.open_search_data_source

        out["data_source"] = (
            capo_cloudwatch_logs.types.open_search_data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if data.get("application") is not None:
        import capo_cloudwatch_logs.types.open_search_application

        out["application"] = (
            capo_cloudwatch_logs.types.open_search_application.deserialize_aws_json_1_1(
                data["application"]
            )
        )
    if data.get("collection") is not None:
        import capo_cloudwatch_logs.types.open_search_collection

        out["collection"] = (
            capo_cloudwatch_logs.types.open_search_collection.deserialize_aws_json_1_1(
                data["collection"]
            )
        )
    if data.get("workspace") is not None:
        import capo_cloudwatch_logs.types.open_search_workspace

        out["workspace"] = (
            capo_cloudwatch_logs.types.open_search_workspace.deserialize_aws_json_1_1(
                data["workspace"]
            )
        )
    if data.get("encryptionPolicy") is not None:
        import capo_cloudwatch_logs.types.open_search_encryption_policy

        out["encryption_policy"] = (
            capo_cloudwatch_logs.types.open_search_encryption_policy.deserialize_aws_json_1_1(
                data["encryptionPolicy"]
            )
        )
    if data.get("networkPolicy") is not None:
        import capo_cloudwatch_logs.types.open_search_network_policy

        out["network_policy"] = (
            capo_cloudwatch_logs.types.open_search_network_policy.deserialize_aws_json_1_1(
                data["networkPolicy"]
            )
        )
    if data.get("accessPolicy") is not None:
        import capo_cloudwatch_logs.types.open_search_data_access_policy

        out["access_policy"] = (
            capo_cloudwatch_logs.types.open_search_data_access_policy.deserialize_aws_json_1_1(
                data["accessPolicy"]
            )
        )
    if data.get("lifecyclePolicy") is not None:
        import capo_cloudwatch_logs.types.open_search_lifecycle_policy

        out["lifecycle_policy"] = (
            capo_cloudwatch_logs.types.open_search_lifecycle_policy.deserialize_aws_json_1_1(
                data["lifecyclePolicy"]
            )
        )
    return out
