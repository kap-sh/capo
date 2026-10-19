"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.salesforce_chatter_feed_configuration
    import capo_kendra.types.salesforce_knowledge_article_configuration
    import capo_kendra.types.salesforce_standard_object_attachment_configuration
    import capo_kendra.types.salesforce_standard_object_configuration_list
    import capo_kendra.types.secret_arn
    import capo_kendra.types.url


class SalesforceConfiguration(TypedDict, closed=True):
    server_url: "capo_kendra.types.url.Url"
    """<p>The instance URL for the Salesforce site that you want to index.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token. </p> </li> <li> <p>consumerKey - The application public key generated when you created your Salesforce application.</p> </li> <li> <p>consumerSecret - The application private key generated when you created your Salesforce application.</p> </li> <li> <p>password - The password associated with the user logging in to the Salesforce instance.</p> </li> <li> <p>securityToken - The token associated with the user logging in to the Salesforce instance.</p> </li> <li> <p>username - The user name of the user logging in to the Salesforce instance.</p> </li> </ul>"""
    standard_object_configurations: NotRequired[
        "capo_kendra.types.salesforce_standard_object_configuration_list.SalesforceStandardObjectConfigurationList"
    ]
    """<p>Configuration of the Salesforce standard objects that Amazon Kendra indexes.</p>"""
    knowledge_article_configuration: NotRequired[
        "capo_kendra.types.salesforce_knowledge_article_configuration.SalesforceKnowledgeArticleConfiguration"
    ]
    """<p>Configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.</p>"""
    chatter_feed_configuration: NotRequired[
        "capo_kendra.types.salesforce_chatter_feed_configuration.SalesforceChatterFeedConfiguration"
    ]
    """<p>Configuration information for Salesforce chatter feeds.</p>"""
    crawl_attachments: "capo_kendra.types.boolean.Boolean"
    """<p>Indicates whether Amazon Kendra should index attachments to Salesforce objects.</p>"""
    standard_object_attachment_configuration: NotRequired[
        "capo_kendra.types.salesforce_standard_object_attachment_configuration.SalesforceStandardObjectAttachmentConfiguration"
    ]
    """<p>Configuration information for processing attachments to Salesforce standard objects. </p>"""
    include_attachment_file_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain documents in your Salesforce. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the name of the attached file.</p>"""
    exclude_attachment_file_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain documents in your Salesforce. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the name of the attached file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceConfiguration) -> dict:
    out: dict = {}
    out["ServerUrl"] = value["server_url"]
    out["SecretArn"] = value["secret_arn"]
    if "standard_object_configurations" in value:
        import capo_kendra.types.salesforce_standard_object_configuration_list

        out["StandardObjectConfigurations"] = (
            capo_kendra.types.salesforce_standard_object_configuration_list.serialize_aws_json_1_1(
                value["standard_object_configurations"]
            )
        )
    if "knowledge_article_configuration" in value:
        import capo_kendra.types.salesforce_knowledge_article_configuration

        out["KnowledgeArticleConfiguration"] = (
            capo_kendra.types.salesforce_knowledge_article_configuration.serialize_aws_json_1_1(
                value["knowledge_article_configuration"]
            )
        )
    if "chatter_feed_configuration" in value:
        import capo_kendra.types.salesforce_chatter_feed_configuration

        out["ChatterFeedConfiguration"] = (
            capo_kendra.types.salesforce_chatter_feed_configuration.serialize_aws_json_1_1(
                value["chatter_feed_configuration"]
            )
        )
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    if "standard_object_attachment_configuration" in value:
        import capo_kendra.types.salesforce_standard_object_attachment_configuration

        out["StandardObjectAttachmentConfiguration"] = (
            capo_kendra.types.salesforce_standard_object_attachment_configuration.serialize_aws_json_1_1(
                value["standard_object_attachment_configuration"]
            )
        )
    if "include_attachment_file_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["IncludeAttachmentFilePatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["include_attachment_file_patterns"]
            )
        )
    if "exclude_attachment_file_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["ExcludeAttachmentFilePatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclude_attachment_file_patterns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceConfiguration:
    out: SalesforceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerUrl") is not None:
        out["server_url"] = data["ServerUrl"]
    else:
        out["server_url"] = ""
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("StandardObjectConfigurations") is not None:
        import capo_kendra.types.salesforce_standard_object_configuration_list

        out["standard_object_configurations"] = (
            capo_kendra.types.salesforce_standard_object_configuration_list.deserialize_aws_json_1_1(
                data["StandardObjectConfigurations"]
            )
        )
    if data.get("KnowledgeArticleConfiguration") is not None:
        import capo_kendra.types.salesforce_knowledge_article_configuration

        out["knowledge_article_configuration"] = (
            capo_kendra.types.salesforce_knowledge_article_configuration.deserialize_aws_json_1_1(
                data["KnowledgeArticleConfiguration"]
            )
        )
    if data.get("ChatterFeedConfiguration") is not None:
        import capo_kendra.types.salesforce_chatter_feed_configuration

        out["chatter_feed_configuration"] = (
            capo_kendra.types.salesforce_chatter_feed_configuration.deserialize_aws_json_1_1(
                data["ChatterFeedConfiguration"]
            )
        )
    if data.get("CrawlAttachments") is not None:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if data.get("StandardObjectAttachmentConfiguration") is not None:
        import capo_kendra.types.salesforce_standard_object_attachment_configuration

        out["standard_object_attachment_configuration"] = (
            capo_kendra.types.salesforce_standard_object_attachment_configuration.deserialize_aws_json_1_1(
                data["StandardObjectAttachmentConfiguration"]
            )
        )
    if data.get("IncludeAttachmentFilePatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["include_attachment_file_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["IncludeAttachmentFilePatterns"]
            )
        )
    if data.get("ExcludeAttachmentFilePatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["exclude_attachment_file_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExcludeAttachmentFilePatterns"]
            )
        )
    return out
