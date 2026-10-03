"""Generated from Smithy shape ``com.amazonaws.kendra#OneDriveConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.one_drive_users
    import capo_kendra.types.secret_arn
    import capo_kendra.types.tenant_domain


class OneDriveConfiguration(TypedDict, closed=True):
    tenant_domain: "capo_kendra.types.tenant_domain.TenantDomain"
    """<p>The Azure Active Directory domain of the organization. </p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the user name and password to connect to OneDrive. The user name should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.</p>"""
    one_drive_users: "capo_kendra.types.one_drive_users.OneDriveUsers"
    """<p>A list of user accounts whose documents should be indexed.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain documents in your OneDrive. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the file name.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain documents in your OneDrive. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the file name.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map OneDrive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to OneDrive fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The OneDrive data source field names must exist in your OneDrive custom metadata.</p>"""
    disable_local_groups: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to disable local groups information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OneDriveConfiguration) -> dict:
    out: dict = {}
    out["TenantDomain"] = value["tenant_domain"]
    out["SecretArn"] = value["secret_arn"]
    import capo_kendra.types.one_drive_users

    out["OneDriveUsers"] = capo_kendra.types.one_drive_users.serialize_aws_json_1_1(
        value["one_drive_users"]
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
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    out["DisableLocalGroups"] = value.get("disable_local_groups", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> OneDriveConfiguration:
    out: OneDriveConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TenantDomain") is not None:
        out["tenant_domain"] = data["TenantDomain"]
    else:
        raise DeserializationError("OneDriveConfiguration.tenant_domain required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("OneDriveConfiguration.secret_arn required")
    if data.get("OneDriveUsers") is not None:
        import capo_kendra.types.one_drive_users

        out["one_drive_users"] = (
            capo_kendra.types.one_drive_users.deserialize_aws_json_1_1(
                data["OneDriveUsers"]
            )
        )
    else:
        raise DeserializationError("OneDriveConfiguration.one_drive_users required")
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
    if data.get("DisableLocalGroups") is not None:
        out["disable_local_groups"] = data["DisableLocalGroups"]
    else:
        out["disable_local_groups"] = False
    return out
