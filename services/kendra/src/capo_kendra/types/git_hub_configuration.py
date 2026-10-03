"""Generated from Smithy shape ``com.amazonaws.kendra#GitHubConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.git_hub_document_crawl_properties
    import capo_kendra.types.on_premise_configuration
    import capo_kendra.types.repository_names
    import capo_kendra.types.saa_s_configuration
    import capo_kendra.types.secret_arn
    import capo_kendra.types.string_list
    import capo_kendra.types.type


class GitHubConfiguration(TypedDict, closed=True):
    saa_s_configuration: NotRequired[
        "capo_kendra.types.saa_s_configuration.SaaSConfiguration"
    ]
    """<p>Configuration information to connect to GitHub Enterprise Cloud (SaaS).</p>"""
    on_premise_configuration: NotRequired[
        "capo_kendra.types.on_premise_configuration.OnPremiseConfiguration"
    ]
    """<p>Configuration information to connect to GitHub Enterprise Server (on premises).</p>"""
    type: NotRequired["capo_kendra.types.type.Type"]
    """<p>The type of GitHub service you want to connect to—GitHub Enterprise Cloud (SaaS) or GitHub Enterprise Server (on premises).</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your GitHub. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>personalToken—The access token created in GitHub. For more information on creating a token in GitHub, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-github.html">Using a GitHub data source</a>.</p> </li> </ul>"""
    use_change_log: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the GitHub change log to determine which documents require updating in the index. Depending on the GitHub change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in GitHub.</p>"""
    git_hub_document_crawl_properties: NotRequired[
        "capo_kendra.types.git_hub_document_crawl_properties.GitHubDocumentCrawlProperties"
    ]
    """<p>Configuration information to include certain types of GitHub content. You can configure to index repository files only, or also include issues and pull requests, comments, and comment attachments.</p>"""
    repository_filter: NotRequired["capo_kendra.types.repository_names.RepositoryNames"]
    """<p>A list of names of the specific repositories you want to index.</p>"""
    inclusion_folder_name_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to include certain folder names in your GitHub repository or repositories. Folder names that match the patterns are included in the index. Folder names that don't match the patterns are excluded from the index. If a folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the folder isn't included in the index.</p>"""
    inclusion_file_type_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to include certain file types in your GitHub repository or repositories. File types that match the patterns are included in the index. File types that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    inclusion_file_name_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to include certain file names in your GitHub repository or repositories. File names that match the patterns are included in the index. File names that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_folder_name_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to exclude certain folder names in your GitHub repository or repositories. Folder names that match the patterns are excluded from the index. Folder names that don't match the patterns are included in the index. If a folder matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the folder isn't included in the index.</p>"""
    exclusion_file_type_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to exclude certain file types in your GitHub repository or repositories. File types that match the patterns are excluded from the index. File types that don't match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_file_name_patterns: NotRequired[
        "capo_kendra.types.string_list.StringList"
    ]
    """<p>A list of regular expression patterns to exclude certain file names in your GitHub repository or repositories. File names that match the patterns are excluded from the index. File names that don't match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information of an Amazon Virtual Private Cloud to connect to your GitHub. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""
    git_hub_repository_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map GitHub repository attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_commit_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub commits to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_issue_document_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub issues to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_issue_comment_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub issue comments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_issue_attachment_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub issue attachments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_pull_request_comment_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub pull request comments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_pull_request_document_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub pull requests to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""
    git_hub_pull_request_document_attachment_configuration_field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map attributes or field names of GitHub pull request attachments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to GitHub fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The GitHub data source field names must exist in your GitHub custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitHubConfiguration) -> dict:
    out: dict = {}
    if "saa_s_configuration" in value:
        import capo_kendra.types.saa_s_configuration

        out["SaaSConfiguration"] = (
            capo_kendra.types.saa_s_configuration.serialize_aws_json_1_1(
                value["saa_s_configuration"]
            )
        )
    if "on_premise_configuration" in value:
        import capo_kendra.types.on_premise_configuration

        out["OnPremiseConfiguration"] = (
            capo_kendra.types.on_premise_configuration.serialize_aws_json_1_1(
                value["on_premise_configuration"]
            )
        )
    if "type" in value:
        import capo_kendra.types.type

        out["Type"] = capo_kendra.types.type.serialize_aws_json_1_1(value["type"])
    out["SecretArn"] = value["secret_arn"]
    out["UseChangeLog"] = value.get("use_change_log", False)
    if "git_hub_document_crawl_properties" in value:
        import capo_kendra.types.git_hub_document_crawl_properties

        out["GitHubDocumentCrawlProperties"] = (
            capo_kendra.types.git_hub_document_crawl_properties.serialize_aws_json_1_1(
                value["git_hub_document_crawl_properties"]
            )
        )
    if "repository_filter" in value:
        import capo_kendra.types.repository_names

        out["RepositoryFilter"] = (
            capo_kendra.types.repository_names.serialize_aws_json_1_1(
                value["repository_filter"]
            )
        )
    if "inclusion_folder_name_patterns" in value:
        import capo_kendra.types.string_list

        out["InclusionFolderNamePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["inclusion_folder_name_patterns"]
            )
        )
    if "inclusion_file_type_patterns" in value:
        import capo_kendra.types.string_list

        out["InclusionFileTypePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["inclusion_file_type_patterns"]
            )
        )
    if "inclusion_file_name_patterns" in value:
        import capo_kendra.types.string_list

        out["InclusionFileNamePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["inclusion_file_name_patterns"]
            )
        )
    if "exclusion_folder_name_patterns" in value:
        import capo_kendra.types.string_list

        out["ExclusionFolderNamePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["exclusion_folder_name_patterns"]
            )
        )
    if "exclusion_file_type_patterns" in value:
        import capo_kendra.types.string_list

        out["ExclusionFileTypePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["exclusion_file_type_patterns"]
            )
        )
    if "exclusion_file_name_patterns" in value:
        import capo_kendra.types.string_list

        out["ExclusionFileNamePatterns"] = (
            capo_kendra.types.string_list.serialize_aws_json_1_1(
                value["exclusion_file_name_patterns"]
            )
        )
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "git_hub_repository_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubRepositoryConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_repository_configuration_field_mappings"]
            )
        )
    if "git_hub_commit_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubCommitConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_commit_configuration_field_mappings"]
            )
        )
    if "git_hub_issue_document_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubIssueDocumentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_issue_document_configuration_field_mappings"]
            )
        )
    if "git_hub_issue_comment_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubIssueCommentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_issue_comment_configuration_field_mappings"]
            )
        )
    if "git_hub_issue_attachment_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubIssueAttachmentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_issue_attachment_configuration_field_mappings"]
            )
        )
    if "git_hub_pull_request_comment_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubPullRequestCommentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_pull_request_comment_configuration_field_mappings"]
            )
        )
    if "git_hub_pull_request_document_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubPullRequestDocumentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["git_hub_pull_request_document_configuration_field_mappings"]
            )
        )
    if "git_hub_pull_request_document_attachment_configuration_field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["GitHubPullRequestDocumentAttachmentConfigurationFieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value[
                    "git_hub_pull_request_document_attachment_configuration_field_mappings"
                ]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitHubConfiguration:
    out: GitHubConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SaaSConfiguration") is not None:
        import capo_kendra.types.saa_s_configuration

        out["saa_s_configuration"] = (
            capo_kendra.types.saa_s_configuration.deserialize_aws_json_1_1(
                data["SaaSConfiguration"]
            )
        )
    if data.get("OnPremiseConfiguration") is not None:
        import capo_kendra.types.on_premise_configuration

        out["on_premise_configuration"] = (
            capo_kendra.types.on_premise_configuration.deserialize_aws_json_1_1(
                data["OnPremiseConfiguration"]
            )
        )
    if data.get("Type") is not None:
        import capo_kendra.types.type

        out["type"] = capo_kendra.types.type.deserialize_aws_json_1_1(data["Type"])
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("GitHubConfiguration.secret_arn required")
    if data.get("UseChangeLog") is not None:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
    if data.get("GitHubDocumentCrawlProperties") is not None:
        import capo_kendra.types.git_hub_document_crawl_properties

        out["git_hub_document_crawl_properties"] = (
            capo_kendra.types.git_hub_document_crawl_properties.deserialize_aws_json_1_1(
                data["GitHubDocumentCrawlProperties"]
            )
        )
    if data.get("RepositoryFilter") is not None:
        import capo_kendra.types.repository_names

        out["repository_filter"] = (
            capo_kendra.types.repository_names.deserialize_aws_json_1_1(
                data["RepositoryFilter"]
            )
        )
    if data.get("InclusionFolderNamePatterns") is not None:
        import capo_kendra.types.string_list

        out["inclusion_folder_name_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["InclusionFolderNamePatterns"]
            )
        )
    if data.get("InclusionFileTypePatterns") is not None:
        import capo_kendra.types.string_list

        out["inclusion_file_type_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["InclusionFileTypePatterns"]
            )
        )
    if data.get("InclusionFileNamePatterns") is not None:
        import capo_kendra.types.string_list

        out["inclusion_file_name_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["InclusionFileNamePatterns"]
            )
        )
    if data.get("ExclusionFolderNamePatterns") is not None:
        import capo_kendra.types.string_list

        out["exclusion_folder_name_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["ExclusionFolderNamePatterns"]
            )
        )
    if data.get("ExclusionFileTypePatterns") is not None:
        import capo_kendra.types.string_list

        out["exclusion_file_type_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["ExclusionFileTypePatterns"]
            )
        )
    if data.get("ExclusionFileNamePatterns") is not None:
        import capo_kendra.types.string_list

        out["exclusion_file_name_patterns"] = (
            capo_kendra.types.string_list.deserialize_aws_json_1_1(
                data["ExclusionFileNamePatterns"]
            )
        )
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if data.get("GitHubRepositoryConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_repository_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubRepositoryConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubCommitConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_commit_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubCommitConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubIssueDocumentConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_issue_document_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubIssueDocumentConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubIssueCommentConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_issue_comment_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubIssueCommentConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubIssueAttachmentConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_issue_attachment_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubIssueAttachmentConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubPullRequestCommentConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_pull_request_comment_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubPullRequestCommentConfigurationFieldMappings"]
            )
        )
    if data.get("GitHubPullRequestDocumentConfigurationFieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_pull_request_document_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubPullRequestDocumentConfigurationFieldMappings"]
            )
        )
    if (
        data.get("GitHubPullRequestDocumentAttachmentConfigurationFieldMappings")
        is not None
    ):
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["git_hub_pull_request_document_attachment_configuration_field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["GitHubPullRequestDocumentAttachmentConfigurationFieldMappings"]
            )
        )
    return out
