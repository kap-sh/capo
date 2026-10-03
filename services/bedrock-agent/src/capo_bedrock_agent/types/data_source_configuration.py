"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.confluence_data_source_configuration
    import capo_bedrock_agent.types.data_source_type
    import capo_bedrock_agent.types.managed_knowledge_base_connector_configuration
    import capo_bedrock_agent.types.s3_data_source_configuration
    import capo_bedrock_agent.types.salesforce_data_source_configuration
    import capo_bedrock_agent.types.share_point_data_source_configuration
    import capo_bedrock_agent.types.web_data_source_configuration


class DataSourceConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.data_source_type.DataSourceType"
    """<p>The type of data source.</p>"""
    managed_knowledge_base_connector_configuration: NotRequired[
        "capo_bedrock_agent.types.managed_knowledge_base_connector_configuration.ManagedKnowledgeBaseConnectorConfiguration"
    ]
    """<p>Contains the configuration for a data source that connects a managed knowledge base to a supported data source connector. Specify this object when the data source type is <code>MANAGED_KNOWLEDGE_BASE_CONNECTOR</code>.</p>"""
    s3_configuration: NotRequired[
        "capo_bedrock_agent.types.s3_data_source_configuration.S3DataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Amazon S3 as your data source for self-managed knowledge bases. To configure this data source for managed knowledge bases, use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html">managedKnowledgeBaseConnectorConfiguration</a>.</p>"""
    web_configuration: NotRequired[
        "capo_bedrock_agent.types.web_data_source_configuration.WebDataSourceConfiguration"
    ]
    """<p>The configuration of web URLs to crawl for your data source. You should be authorized to crawl the URLs.</p> <note> <p>To configure this data source for managed knowledge bases, use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html">managedKnowledgeBaseConnectorConfiguration</a>. Web crawler data source connector for self-managed knowledge bases is in preview release and is subject to change.</p> </note>"""
    confluence_configuration: NotRequired[
        "capo_bedrock_agent.types.confluence_data_source_configuration.ConfluenceDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Confluence as your data source for self-managed knowledge bases.</p> <note> <p>To configure this data source for managed knowledge bases, use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html">managedKnowledgeBaseConnectorConfiguration</a>. Confluence data source connector for self-managed knowledge bases is in preview release and is subject to change.</p> </note>"""
    salesforce_configuration: NotRequired[
        "capo_bedrock_agent.types.salesforce_data_source_configuration.SalesforceDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to Salesforce as your data source.</p> <note> <p>Salesforce data source connector for self-managed knowledge bases is in preview release and is subject to change.</p> </note>"""
    share_point_configuration: NotRequired[
        "capo_bedrock_agent.types.share_point_data_source_configuration.SharePointDataSourceConfiguration"
    ]
    """<p>The configuration information to connect to SharePoint as your data source for self-managed knowledge bases.</p> <note> <p>To configure this data source for managed knowledge bases, use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html">managedKnowledgeBaseConnectorConfiguration</a>. SharePoint data source connector for self-managed knowledge bases is in preview release and is subject to change.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.data_source_type

    out["type"] = capo_bedrock_agent.types.data_source_type.serialize_json(
        value["type"]
    )
    if "managed_knowledge_base_connector_configuration" in value:
        import capo_bedrock_agent.types.managed_knowledge_base_connector_configuration

        out["managedKnowledgeBaseConnectorConfiguration"] = (
            capo_bedrock_agent.types.managed_knowledge_base_connector_configuration.serialize_json(
                value["managed_knowledge_base_connector_configuration"]
            )
        )
    if "s3_configuration" in value:
        import capo_bedrock_agent.types.s3_data_source_configuration

        out["s3Configuration"] = (
            capo_bedrock_agent.types.s3_data_source_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    if "web_configuration" in value:
        import capo_bedrock_agent.types.web_data_source_configuration

        out["webConfiguration"] = (
            capo_bedrock_agent.types.web_data_source_configuration.serialize_json(
                value["web_configuration"]
            )
        )
    if "confluence_configuration" in value:
        import capo_bedrock_agent.types.confluence_data_source_configuration

        out["confluenceConfiguration"] = (
            capo_bedrock_agent.types.confluence_data_source_configuration.serialize_json(
                value["confluence_configuration"]
            )
        )
    if "salesforce_configuration" in value:
        import capo_bedrock_agent.types.salesforce_data_source_configuration

        out["salesforceConfiguration"] = (
            capo_bedrock_agent.types.salesforce_data_source_configuration.serialize_json(
                value["salesforce_configuration"]
            )
        )
    if "share_point_configuration" in value:
        import capo_bedrock_agent.types.share_point_data_source_configuration

        out["sharePointConfiguration"] = (
            capo_bedrock_agent.types.share_point_data_source_configuration.serialize_json(
                value["share_point_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.data_source_type

        out["type"] = capo_bedrock_agent.types.data_source_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("DataSourceConfiguration.type required")
    if data.get("managedKnowledgeBaseConnectorConfiguration") is not None:
        import capo_bedrock_agent.types.managed_knowledge_base_connector_configuration

        out["managed_knowledge_base_connector_configuration"] = (
            capo_bedrock_agent.types.managed_knowledge_base_connector_configuration.deserialize_json(
                data["managedKnowledgeBaseConnectorConfiguration"]
            )
        )
    if data.get("s3Configuration") is not None:
        import capo_bedrock_agent.types.s3_data_source_configuration

        out["s3_configuration"] = (
            capo_bedrock_agent.types.s3_data_source_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    if data.get("webConfiguration") is not None:
        import capo_bedrock_agent.types.web_data_source_configuration

        out["web_configuration"] = (
            capo_bedrock_agent.types.web_data_source_configuration.deserialize_json(
                data["webConfiguration"]
            )
        )
    if data.get("confluenceConfiguration") is not None:
        import capo_bedrock_agent.types.confluence_data_source_configuration

        out["confluence_configuration"] = (
            capo_bedrock_agent.types.confluence_data_source_configuration.deserialize_json(
                data["confluenceConfiguration"]
            )
        )
    if data.get("salesforceConfiguration") is not None:
        import capo_bedrock_agent.types.salesforce_data_source_configuration

        out["salesforce_configuration"] = (
            capo_bedrock_agent.types.salesforce_data_source_configuration.deserialize_json(
                data["salesforceConfiguration"]
            )
        )
    if data.get("sharePointConfiguration") is not None:
        import capo_bedrock_agent.types.share_point_data_source_configuration

        out["share_point_configuration"] = (
            capo_bedrock_agent.types.share_point_data_source_configuration.deserialize_json(
                data["sharePointConfiguration"]
            )
        )
    return out
