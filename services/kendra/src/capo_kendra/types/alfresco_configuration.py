"""Generated from Smithy shape ``com.amazonaws.kendra#AlfrescoConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.entity_filter
    import capo_kendra.types.s3_path
    import capo_kendra.types.secret_arn
    import capo_kendra.types.site_id
    import capo_kendra.types.site_url


class AlfrescoConfiguration(TypedDict, closed=True):
    site_url: "capo_kendra.types.site_url.SiteUrl"
    """<p>The URL of the Alfresco site. For example, <i>https://hostname:8080</i>.</p>"""
    site_id: "capo_kendra.types.site_id.SiteId"
    """<p>The identifier of the Alfresco site. For example, <i>my-site</i>.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Alfresco data source. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>username—The user name of the Alfresco account.</p> </li> <li> <p>password—The password of the Alfresco account.</p> </li> </ul>"""
    ssl_certificate_s3_path: "capo_kendra.types.s3_path.S3Path"
    """<p>The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to Alfresco if you require a secure SSL connection.</p> <p>You can simply generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html">Create and sign an X509 certificate</a>.</p>"""
    crawl_system_folders: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index shared files.</p>"""
    crawl_comments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index comments of blogs and other content.</p>"""
    entity_filter: NotRequired["capo_kendra.types.entity_filter.EntityFilter"]
    """<p>Specify whether to index document libraries, wikis, or blogs. You can specify one or more of these options.</p>"""
    document_library_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Alfresco document libraries to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Alfresco fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html"> Mapping data source fields</a>. The Alfresco data source field names must exist in your Alfresco custom metadata.</p>"""
    blog_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Alfresco blogs to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Alfresco fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html"> Mapping data source fields</a>. The Alfresco data source field names must exist in your Alfresco custom metadata.</p>"""
    wiki_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Alfresco wikis to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Alfresco fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html"> Mapping data source fields</a>. The Alfresco data source field names must exist in your Alfresco custom metadata.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain files in your Alfresco data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain files in your Alfresco data source. Files that match the patterns are excluded from the index. Files that don't match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Alfresco. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlfrescoConfiguration) -> dict:
    out: dict = {}
    out["SiteUrl"] = value["site_url"]
    out["SiteId"] = value["site_id"]
    out["SecretArn"] = value["secret_arn"]
    import capo_kendra.types.s3_path

    out["SslCertificateS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
        value["ssl_certificate_s3_path"]
    )
    out["CrawlSystemFolders"] = value.get("crawl_system_folders", False)
    out["CrawlComments"] = value.get("crawl_comments", False)
    if "entity_filter" in value:
        import capo_kendra.types.entity_filter

        out["EntityFilter"] = capo_kendra.types.entity_filter.serialize_aws_json_1_1(
            value["entity_filter"]
        )
    if "document_library_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["DocumentLibraryFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["document_library_field_mappings"]
            )
        )
    if "blog_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["BlogFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["blog_field_mappings"]
            )
        )
    if "wiki_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["WikiFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["wiki_field_mappings"]
            )
        )
    if "inclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["InclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["inclusion_patterns"]
            )
        )
    if "exclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["ExclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclusion_patterns"]
            )
        )
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlfrescoConfiguration:
    out: AlfrescoConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SiteUrl") is not None:
        out["site_url"] = data["SiteUrl"]
    else:
        raise DeserializationError("AlfrescoConfiguration.site_url required")
    if data.get("SiteId") is not None:
        out["site_id"] = data["SiteId"]
    else:
        raise DeserializationError("AlfrescoConfiguration.site_id required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("AlfrescoConfiguration.secret_arn required")
    if data.get("SslCertificateS3Path") is not None:
        import capo_kendra.types.s3_path

        out["ssl_certificate_s3_path"] = (
            capo_kendra.types.s3_path.deserialize_aws_json_1_1(
                data["SslCertificateS3Path"]
            )
        )
    else:
        raise DeserializationError(
            "AlfrescoConfiguration.ssl_certificate_s3_path required"
        )
    if data.get("CrawlSystemFolders") is not None:
        out["crawl_system_folders"] = data["CrawlSystemFolders"]
    else:
        out["crawl_system_folders"] = False
    if data.get("CrawlComments") is not None:
        out["crawl_comments"] = data["CrawlComments"]
    else:
        out["crawl_comments"] = False
    if data.get("EntityFilter") is not None:
        import capo_kendra.types.entity_filter

        out["entity_filter"] = capo_kendra.types.entity_filter.deserialize_aws_json_1_1(
            data["EntityFilter"]
        )
    if data.get("DocumentLibraryFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["document_library_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["DocumentLibraryFieldMappings"]
            )
        )
    if data.get("BlogFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["blog_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["BlogFieldMappings"]
            )
        )
    if data.get("WikiFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["wiki_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["WikiFieldMappings"]
            )
        )
    if data.get("InclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["inclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["InclusionPatterns"]
            )
        )
    if data.get("ExclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["exclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExclusionPatterns"]
            )
        )
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    return out
