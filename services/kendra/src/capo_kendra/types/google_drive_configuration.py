"""Generated from Smithy shape ``com.amazonaws.kendra#GoogleDriveConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.exclude_mime_types_list
    import capo_kendra.types.exclude_shared_drives_list
    import capo_kendra.types.exclude_user_accounts_list
    import capo_kendra.types.secret_arn


class GoogleDriveConfiguration(TypedDict, closed=True):
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of a Secrets Managersecret that contains the credentials required to connect to Google Drive. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html">Using a Google Workspace Drive data source</a>.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain items in your Google Drive, including shared drives and users' My Drives. Items that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain items in your Google Drive, including shared drives and users' My Drives. Items that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>Maps Google Drive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Google Drive fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Google Drive data source field names must exist in your Google Drive custom metadata.</p>"""
    exclude_mime_types: NotRequired[
        "capo_kendra.types.exclude_mime_types_list.ExcludeMimeTypesList"
    ]
    """<p>A list of MIME types to exclude from the index. All documents matching the specified MIME type are excluded. </p> <p>For a list of MIME types, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html">Using a Google Workspace Drive data source</a>.</p>"""
    exclude_user_accounts: NotRequired[
        "capo_kendra.types.exclude_user_accounts_list.ExcludeUserAccountsList"
    ]
    """<p>A list of email addresses of the users. Documents owned by these users are excluded from the index. Documents shared with excluded users are indexed unless they are excluded in another way.</p>"""
    exclude_shared_drives: NotRequired[
        "capo_kendra.types.exclude_shared_drives_list.ExcludeSharedDrivesList"
    ]
    """<p>A list of identifiers or shared drives to exclude from the index. All files and folders stored on the shared drive are excluded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GoogleDriveConfiguration) -> dict:
    out: dict = {}
    out["SecretArn"] = value["secret_arn"]
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
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    if "exclude_mime_types" in value:
        import capo_kendra.types.exclude_mime_types_list

        out["ExcludeMimeTypes"] = (
            capo_kendra.types.exclude_mime_types_list.serialize_aws_json_1_1(
                value["exclude_mime_types"]
            )
        )
    if "exclude_user_accounts" in value:
        import capo_kendra.types.exclude_user_accounts_list

        out["ExcludeUserAccounts"] = (
            capo_kendra.types.exclude_user_accounts_list.serialize_aws_json_1_1(
                value["exclude_user_accounts"]
            )
        )
    if "exclude_shared_drives" in value:
        import capo_kendra.types.exclude_shared_drives_list

        out["ExcludeSharedDrives"] = (
            capo_kendra.types.exclude_shared_drives_list.serialize_aws_json_1_1(
                value["exclude_shared_drives"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GoogleDriveConfiguration:
    out: GoogleDriveConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("GoogleDriveConfiguration.secret_arn required")
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
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if data.get("ExcludeMimeTypes") is not None:
        import capo_kendra.types.exclude_mime_types_list

        out["exclude_mime_types"] = (
            capo_kendra.types.exclude_mime_types_list.deserialize_aws_json_1_1(
                data["ExcludeMimeTypes"]
            )
        )
    if data.get("ExcludeUserAccounts") is not None:
        import capo_kendra.types.exclude_user_accounts_list

        out["exclude_user_accounts"] = (
            capo_kendra.types.exclude_user_accounts_list.deserialize_aws_json_1_1(
                data["ExcludeUserAccounts"]
            )
        )
    if data.get("ExcludeSharedDrives") is not None:
        import capo_kendra.types.exclude_shared_drives_list

        out["exclude_shared_drives"] = (
            capo_kendra.types.exclude_shared_drives_list.deserialize_aws_json_1_1(
                data["ExcludeSharedDrives"]
            )
        )
    return out
