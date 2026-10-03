"""Generated from Smithy shape ``com.amazonaws.kendra#BoxConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.enterprise_id
    import capo_kendra.types.secret_arn


class BoxConfiguration(TypedDict, closed=True):
    enterprise_id: "capo_kendra.types.enterprise_id.EnterpriseId"
    """<p>The identifier of the Box Enterprise platform. You can find the enterprise ID in the Box Developer Console settings or when you create an app in Box and download your authentication credentials. For example, <i>801234567</i>.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Box platform. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>clientID—The identifier of the client OAuth 2.0 authentication application created in Box.</p> </li> <li> <p>clientSecret—A set of characters known only to the OAuth 2.0 authentication application created in Box.</p> </li> <li> <p>publicKeyId—The identifier of the public key contained within an identity certificate.</p> </li> <li> <p>privateKey—A set of characters that make up an encryption key.</p> </li> <li> <p>passphrase—A set of characters that act like a password.</p> </li> </ul> <p>You create an application in Box to generate the keys or credentials required for the secret. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-box.html">Using a Box data source</a>.</p>"""
    use_change_log: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the Slack change log to determine which documents require updating in the index. Depending on the data source change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents.</p>"""
    crawl_comments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index comments.</p>"""
    crawl_tasks: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index the contents of tasks.</p>"""
    crawl_web_links: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index web links.</p>"""
    file_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Box files to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Box fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Box field names must exist in your Box custom metadata.</p>"""
    task_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Box tasks to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Box fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Box field names must exist in your Box custom metadata.</p>"""
    comment_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Box comments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Box fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Box field names must exist in your Box custom metadata.</p>"""
    web_link_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Box web links to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Box fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Box field names must exist in your Box custom metadata.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain files and folders in your Box platform. Files and folders that match the patterns are included in the index. Files and folders that don't match the patterns are excluded from the index. If a file or folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file or folder isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain files and folders from your Box platform. Files and folders that match the patterns are excluded from the index.Files and folders that don't match the patterns are included in the index. If a file or folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file or folder isn't included in the index.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon VPC to connect to your Box. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoxConfiguration) -> dict:
    out: dict = {}
    out["EnterpriseId"] = value["enterprise_id"]
    out["SecretArn"] = value["secret_arn"]
    out["UseChangeLog"] = value.get("use_change_log", False)
    out["CrawlComments"] = value.get("crawl_comments", False)
    out["CrawlTasks"] = value.get("crawl_tasks", False)
    out["CrawlWebLinks"] = value.get("crawl_web_links", False)
    if "file_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FileFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["file_field_mappings"]
            )
        )
    if "task_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["TaskFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["task_field_mappings"]
            )
        )
    if "comment_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["CommentFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["comment_field_mappings"]
            )
        )
    if "web_link_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["WebLinkFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["web_link_field_mappings"]
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


def deserialize_aws_json_1_1(data: dict) -> BoxConfiguration:
    out: BoxConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EnterpriseId") is not None:
        out["enterprise_id"] = data["EnterpriseId"]
    else:
        raise DeserializationError("BoxConfiguration.enterprise_id required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("BoxConfiguration.secret_arn required")
    if data.get("UseChangeLog") is not None:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
    if data.get("CrawlComments") is not None:
        out["crawl_comments"] = data["CrawlComments"]
    else:
        out["crawl_comments"] = False
    if data.get("CrawlTasks") is not None:
        out["crawl_tasks"] = data["CrawlTasks"]
    else:
        out["crawl_tasks"] = False
    if data.get("CrawlWebLinks") is not None:
        out["crawl_web_links"] = data["CrawlWebLinks"]
    else:
        out["crawl_web_links"] = False
    if data.get("FileFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["file_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FileFieldMappings"]
            )
        )
    if data.get("TaskFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["task_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["TaskFieldMappings"]
            )
        )
    if data.get("CommentFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["comment_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["CommentFieldMappings"]
            )
        )
    if data.get("WebLinkFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["web_link_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["WebLinkFieldMappings"]
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
