"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_field_name
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.proxy_configuration
    import capo_kendra.types.s3_path
    import capo_kendra.types.secret_arn
    import capo_kendra.types.share_point_online_authentication_type
    import capo_kendra.types.share_point_url_list
    import capo_kendra.types.share_point_version


class SharePointConfiguration(TypedDict, closed=True):
    share_point_version: "capo_kendra.types.share_point_version.SharePointVersion"
    """<p>The version of Microsoft SharePoint that you use.</p>"""
    urls: "capo_kendra.types.share_point_url_list.SharePointUrlList"
    """<p>The Microsoft SharePoint site URLs for the documents you want to index.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the user name and password required to connect to the SharePoint instance. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html">Microsoft SharePoint</a>.</p>"""
    crawl_attachments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index document attachments.</p>"""
    use_change_log: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the SharePoint change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in SharePoint.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain documents in your SharePoint. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The regex applies to the display URL of the SharePoint document.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain documents in your SharePoint. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The regex applies to the display URL of the SharePoint document.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Microsoft SharePoint. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map SharePoint data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to SharePoint fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The SharePoint data source field names must exist in your SharePoint custom metadata.</p>"""
    document_title_field_name: NotRequired[
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The Microsoft SharePoint attribute field that contains the title of the document.</p>"""
    disable_local_groups: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to disable local groups information.</p>"""
    ssl_certificate_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    """<p>The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to SharePoint Server if you require a secure SSL connection.</p> <p>You can generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html">Create and sign an X509 certificate</a>.</p>"""
    authentication_type: NotRequired[
        "capo_kendra.types.share_point_online_authentication_type.SharePointOnlineAuthenticationType"
    ]
    """<p>Whether you want to connect to SharePoint Online using basic authentication of user name and password, or OAuth authentication of user name, password, client ID, and client secret, or AD App-only authentication of client secret.</p>"""
    proxy_configuration: NotRequired[
        "capo_kendra.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>Configuration information to connect to your Microsoft SharePoint site URLs via instance via a web proxy. You can use this option for SharePoint Server.</p> <p>You must provide the website host name and port number. For example, the host name of <i>https://a.example.com/page1.html</i> is "a.example.com" and the port is 443, the standard port for HTTPS.</p> <p>Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication of user name and password. To store web proxy credentials, you use a secret in Secrets Manager.</p> <p>It is recommended that you follow best security practices when configuring your web proxy. This includes setting up throttling, setting up logging and monitoring, and applying security patches on a regular basis. If you use your web proxy with multiple data sources, sync jobs that occur at the same time could strain the load on your proxy. It is recommended you prepare your proxy beforehand for any security and load requirements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharePointConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.share_point_version

    out["SharePointVersion"] = (
        capo_kendra.types.share_point_version.serialize_aws_json_1_1(
            value["share_point_version"]
        )
    )
    import capo_kendra.types.share_point_url_list

    out["Urls"] = capo_kendra.types.share_point_url_list.serialize_aws_json_1_1(
        value["urls"]
    )
    out["SecretArn"] = value["secret_arn"]
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    out["UseChangeLog"] = value.get("use_change_log", False)
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
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    if "document_title_field_name" in value:
        out["DocumentTitleFieldName"] = value["document_title_field_name"]
    out["DisableLocalGroups"] = value.get("disable_local_groups", False)
    if "ssl_certificate_s3_path" in value:
        import capo_kendra.types.s3_path

        out["SslCertificateS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["ssl_certificate_s3_path"]
        )
    if "authentication_type" in value:
        import capo_kendra.types.share_point_online_authentication_type

        out["AuthenticationType"] = (
            capo_kendra.types.share_point_online_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "proxy_configuration" in value:
        import capo_kendra.types.proxy_configuration

        out["ProxyConfiguration"] = (
            capo_kendra.types.proxy_configuration.serialize_aws_json_1_1(
                value["proxy_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SharePointConfiguration:
    out: SharePointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SharePointVersion") is not None:
        import capo_kendra.types.share_point_version

        out["share_point_version"] = (
            capo_kendra.types.share_point_version.deserialize_aws_json_1_1(
                data["SharePointVersion"]
            )
        )
    else:
        raise DeserializationError(
            "SharePointConfiguration.share_point_version required"
        )
    if data.get("Urls") is not None:
        import capo_kendra.types.share_point_url_list

        out["urls"] = capo_kendra.types.share_point_url_list.deserialize_aws_json_1_1(
            data["Urls"]
        )
    else:
        raise DeserializationError("SharePointConfiguration.urls required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("SharePointConfiguration.secret_arn required")
    if data.get("CrawlAttachments") is not None:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if data.get("UseChangeLog") is not None:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
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
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if data.get("DocumentTitleFieldName") is not None:
        out["document_title_field_name"] = data["DocumentTitleFieldName"]
    if data.get("DisableLocalGroups") is not None:
        out["disable_local_groups"] = data["DisableLocalGroups"]
    else:
        out["disable_local_groups"] = False
    if data.get("SslCertificateS3Path") is not None:
        import capo_kendra.types.s3_path

        out["ssl_certificate_s3_path"] = (
            capo_kendra.types.s3_path.deserialize_aws_json_1_1(
                data["SslCertificateS3Path"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_kendra.types.share_point_online_authentication_type

        out["authentication_type"] = (
            capo_kendra.types.share_point_online_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("ProxyConfiguration") is not None:
        import capo_kendra.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_kendra.types.proxy_configuration.deserialize_aws_json_1_1(
                data["ProxyConfiguration"]
            )
        )
    return out
