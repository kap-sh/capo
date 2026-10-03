"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.confluence_attachment_configuration
    import capo_kendra.types.confluence_authentication_type
    import capo_kendra.types.confluence_blog_configuration
    import capo_kendra.types.confluence_page_configuration
    import capo_kendra.types.confluence_space_configuration
    import capo_kendra.types.confluence_version
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.proxy_configuration
    import capo_kendra.types.secret_arn
    import capo_kendra.types.url


class ConfluenceConfiguration(TypedDict, closed=True):
    server_url: "capo_kendra.types.url.Url"
    """<p>The URL of your Confluence instance. Use the full URL of the server. For example, <i>https://server.example.com:port/</i>. You can also use an IP address, for example, <i>https://192.168.1.113/</i>.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the user name and password required to connect to the Confluence instance. If you use Confluence Cloud, you use a generated API token as the password.</p> <p>You can also provide authentication credentials in the form of a personal access token. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html">Using a Confluence data source</a>.</p>"""
    version: "capo_kendra.types.confluence_version.ConfluenceVersion"
    """<p>The version or the type of Confluence installation to connect to.</p>"""
    space_configuration: NotRequired[
        "capo_kendra.types.confluence_space_configuration.ConfluenceSpaceConfiguration"
    ]
    """<p>Configuration information for indexing Confluence spaces.</p>"""
    page_configuration: NotRequired[
        "capo_kendra.types.confluence_page_configuration.ConfluencePageConfiguration"
    ]
    """<p>Configuration information for indexing Confluence pages.</p>"""
    blog_configuration: NotRequired[
        "capo_kendra.types.confluence_blog_configuration.ConfluenceBlogConfiguration"
    ]
    """<p>Configuration information for indexing Confluence blogs.</p>"""
    attachment_configuration: NotRequired[
        "capo_kendra.types.confluence_attachment_configuration.ConfluenceAttachmentConfiguration"
    ]
    """<p>Configuration information for indexing attachments to Confluence blogs and pages.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Confluence. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are included in the index. Content that doesn't match the patterns is excluded from the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are excluded from the index. Content that doesn't match the patterns is included in the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.</p>"""
    proxy_configuration: NotRequired[
        "capo_kendra.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>Configuration information to connect to your Confluence URL instance via a web proxy. You can use this option for Confluence Server.</p> <p>You must provide the website host name and port number. For example, the host name of <i>https://a.example.com/page1.html</i> is "a.example.com" and the port is 443, the standard port for HTTPS.</p> <p>Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication of user name and password. To store web proxy credentials, you use a secret in Secrets Manager.</p> <p>It is recommended that you follow best security practices when configuring your web proxy. This includes setting up throttling, setting up logging and monitoring, and applying security patches on a regular basis. If you use your web proxy with multiple data sources, sync jobs that occur at the same time could strain the load on your proxy. It is recommended you prepare your proxy beforehand for any security and load requirements.</p>"""
    authentication_type: NotRequired[
        "capo_kendra.types.confluence_authentication_type.ConfluenceAuthenticationType"
    ]
    """<p>Whether you want to connect to Confluence using basic authentication of user name and password, or a personal access token. You can use a personal access token for Confluence Server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceConfiguration) -> dict:
    out: dict = {}
    out["ServerUrl"] = value["server_url"]
    out["SecretArn"] = value["secret_arn"]
    import capo_kendra.types.confluence_version

    out["Version"] = capo_kendra.types.confluence_version.serialize_aws_json_1_1(
        value["version"]
    )
    if "space_configuration" in value:
        import capo_kendra.types.confluence_space_configuration

        out["SpaceConfiguration"] = (
            capo_kendra.types.confluence_space_configuration.serialize_aws_json_1_1(
                value["space_configuration"]
            )
        )
    if "page_configuration" in value:
        import capo_kendra.types.confluence_page_configuration

        out["PageConfiguration"] = (
            capo_kendra.types.confluence_page_configuration.serialize_aws_json_1_1(
                value["page_configuration"]
            )
        )
    if "blog_configuration" in value:
        import capo_kendra.types.confluence_blog_configuration

        out["BlogConfiguration"] = (
            capo_kendra.types.confluence_blog_configuration.serialize_aws_json_1_1(
                value["blog_configuration"]
            )
        )
    if "attachment_configuration" in value:
        import capo_kendra.types.confluence_attachment_configuration

        out["AttachmentConfiguration"] = (
            capo_kendra.types.confluence_attachment_configuration.serialize_aws_json_1_1(
                value["attachment_configuration"]
            )
        )
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
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
    if "proxy_configuration" in value:
        import capo_kendra.types.proxy_configuration

        out["ProxyConfiguration"] = (
            capo_kendra.types.proxy_configuration.serialize_aws_json_1_1(
                value["proxy_configuration"]
            )
        )
    if "authentication_type" in value:
        import capo_kendra.types.confluence_authentication_type

        out["AuthenticationType"] = (
            capo_kendra.types.confluence_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluenceConfiguration:
    out: ConfluenceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ServerUrl") is not None:
        out["server_url"] = data["ServerUrl"]
    else:
        raise DeserializationError("ConfluenceConfiguration.server_url required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("ConfluenceConfiguration.secret_arn required")
    if data.get("Version") is not None:
        import capo_kendra.types.confluence_version

        out["version"] = capo_kendra.types.confluence_version.deserialize_aws_json_1_1(
            data["Version"]
        )
    else:
        raise DeserializationError("ConfluenceConfiguration.version required")
    if data.get("SpaceConfiguration") is not None:
        import capo_kendra.types.confluence_space_configuration

        out["space_configuration"] = (
            capo_kendra.types.confluence_space_configuration.deserialize_aws_json_1_1(
                data["SpaceConfiguration"]
            )
        )
    if data.get("PageConfiguration") is not None:
        import capo_kendra.types.confluence_page_configuration

        out["page_configuration"] = (
            capo_kendra.types.confluence_page_configuration.deserialize_aws_json_1_1(
                data["PageConfiguration"]
            )
        )
    if data.get("BlogConfiguration") is not None:
        import capo_kendra.types.confluence_blog_configuration

        out["blog_configuration"] = (
            capo_kendra.types.confluence_blog_configuration.deserialize_aws_json_1_1(
                data["BlogConfiguration"]
            )
        )
    if data.get("AttachmentConfiguration") is not None:
        import capo_kendra.types.confluence_attachment_configuration

        out["attachment_configuration"] = (
            capo_kendra.types.confluence_attachment_configuration.deserialize_aws_json_1_1(
                data["AttachmentConfiguration"]
            )
        )
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
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
    if data.get("ProxyConfiguration") is not None:
        import capo_kendra.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_kendra.types.proxy_configuration.deserialize_aws_json_1_1(
                data["ProxyConfiguration"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_kendra.types.confluence_authentication_type

        out["authentication_type"] = (
            capo_kendra.types.confluence_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
