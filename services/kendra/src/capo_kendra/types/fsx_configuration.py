"""Generated from Smithy shape ``com.amazonaws.kendra#FsxConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.file_system_id
    import capo_kendra.types.fsx_file_system_type
    import capo_kendra.types.secret_arn


class FsxConfiguration(TypedDict, closed=True):
    file_system_id: "capo_kendra.types.file_system_id.FileSystemId"
    """<p>The identifier of the Amazon FSx file system.</p> <p>You can find your file system ID on the file system dashboard in the Amazon FSx console. For information on how to create a file system in Amazon FSx console, using Windows File Server as an example, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started-step1.html">Amazon FSx Getting started guide</a>.</p>"""
    file_system_type: "capo_kendra.types.fsx_file_system_type.FsxFileSystemType"
    """<p>The Amazon FSx file system type. Windows is currently the only supported type.</p>"""
    vpc_configuration: (
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    )
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Amazon FSx. Your Amazon FSx instance must reside inside your VPC.</p>"""
    secret_arn: NotRequired["capo_kendra.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Amazon FSx file system. Windows is currently the only supported type. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>username—The Active Directory user name, along with the Domain Name System (DNS) domain name. For example, <i>user@corp.example.com</i>. The Active Directory user account must have read and mounting access to the Amazon FSx file system for Windows.</p> </li> <li> <p>password—The password of the Active Directory user account with read and mounting access to the Amazon FSx Windows file system.</p> </li> </ul>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain files in your Amazon FSx file system. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain files in your Amazon FSx file system. Files that match the patterns are excluded from the index. Files that don't match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map Amazon FSx data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Amazon FSx fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Amazon FSx data source field names must exist in your Amazon FSx custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxConfiguration) -> dict:
    out: dict = {}
    out["FileSystemId"] = value["file_system_id"]
    import capo_kendra.types.fsx_file_system_type

    out["FileSystemType"] = (
        capo_kendra.types.fsx_file_system_type.serialize_aws_json_1_1(
            value["file_system_type"]
        )
    )
    import capo_kendra.types.data_source_vpc_configuration

    out["VpcConfiguration"] = (
        capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
            value["vpc_configuration"]
        )
    )
    if "secret_arn" in value:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> FsxConfiguration:
    out: FsxConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("FsxConfiguration.file_system_id required")
    if data.get("FileSystemType") is not None:
        import capo_kendra.types.fsx_file_system_type

        out["file_system_type"] = (
            capo_kendra.types.fsx_file_system_type.deserialize_aws_json_1_1(
                data["FileSystemType"]
            )
        )
    else:
        raise DeserializationError("FsxConfiguration.file_system_type required")
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    else:
        raise DeserializationError("FsxConfiguration.vpc_configuration required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
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
    return out
