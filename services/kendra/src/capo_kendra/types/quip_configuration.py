"""Generated from Smithy shape ``com.amazonaws.kendra#QuipConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.domain
    import capo_kendra.types.folder_id_list
    import capo_kendra.types.secret_arn


class QuipConfiguration(TypedDict, closed=True):
    domain: "capo_kendra.types.domain.Domain"
    """<p>The Quip site domain. For example, <i>https://quip-company.quipdomain.com/browse</i>. The domain in this example is "quipdomain".</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs that are required to connect to your Quip. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>accessToken—The token created in Quip. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html">Using a Quip data source</a>.</p> </li> </ul>"""
    crawl_file_comments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index file comments.</p>"""
    crawl_chat_rooms: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index the contents of chat rooms.</p>"""
    crawl_attachments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index attachments.</p>"""
    folder_ids: NotRequired["capo_kendra.types.folder_id_list.FolderIdList"]
    """<p>The identifiers of the Quip folders you want to index. You can find the folder ID in your browser URL when you access your folder in Quip. For example, <i>https://quip-company.quipdomain.com/zlLuOVNSarTL/folder-name</i>. The folder ID in this example is "zlLuOVNSarTL".</p>"""
    thread_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Quip threads to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Quip fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Quip field names must exist in your Quip custom metadata.</p>"""
    message_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Quip messages to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Quip fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Quip field names must exist in your Quip custom metadata.</p>"""
    attachment_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of Quip attachments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Quip fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Quip field names must exist in your Quip custom metadata.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain files in your Quip file system. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain files in your Quip file system. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud (VPC) to connect to your Quip. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuipConfiguration) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    out["SecretArn"] = value["secret_arn"]
    out["CrawlFileComments"] = value.get("crawl_file_comments", False)
    out["CrawlChatRooms"] = value.get("crawl_chat_rooms", False)
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    if "folder_ids" in value:
        import capo_kendra.types.folder_id_list

        out["FolderIds"] = capo_kendra.types.folder_id_list.serialize_aws_json_1_1(
            value["folder_ids"]
        )
    if "thread_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["ThreadFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["thread_field_mappings"]
            )
        )
    if "message_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["MessageFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["message_field_mappings"]
            )
        )
    if "attachment_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["AttachmentFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["attachment_field_mappings"]
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


def deserialize_aws_json_1_1(data: dict) -> QuipConfiguration:
    out: QuipConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("QuipConfiguration.domain required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("QuipConfiguration.secret_arn required")
    if data.get("CrawlFileComments") is not None:
        out["crawl_file_comments"] = data["CrawlFileComments"]
    else:
        out["crawl_file_comments"] = False
    if data.get("CrawlChatRooms") is not None:
        out["crawl_chat_rooms"] = data["CrawlChatRooms"]
    else:
        out["crawl_chat_rooms"] = False
    if data.get("CrawlAttachments") is not None:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if data.get("FolderIds") is not None:
        import capo_kendra.types.folder_id_list

        out["folder_ids"] = capo_kendra.types.folder_id_list.deserialize_aws_json_1_1(
            data["FolderIds"]
        )
    if data.get("ThreadFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["thread_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["ThreadFieldMappings"]
            )
        )
    if data.get("MessageFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["message_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["MessageFieldMappings"]
            )
        )
    if data.get("AttachmentFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["attachment_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["AttachmentFieldMappings"]
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
