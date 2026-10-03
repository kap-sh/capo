"""Generated from Smithy shape ``com.amazonaws.kendra#S3DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_list_configuration
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.documents_metadata_configuration
    import capo_kendra.types.s3_bucket_name


class S3DataSourceConfiguration(TypedDict, closed=True):
    bucket_name: "capo_kendra.types.s3_bucket_name.S3BucketName"
    """<p>The name of the bucket that contains the documents.</p>"""
    inclusion_prefixes: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of S3 prefixes for the documents that should be included in the index.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to include in your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:</p> <ul> <li> <p> <i>/myapp/config/*</i>—All files inside config directory.</p> </li> <li> <p> <i>**/*.png</i>—All .png files in all directories.</p> </li> <li> <p> <i>**/*.{png, ico, md}</i>—All .png, .ico or .md files in all directories.</p> </li> <li> <p> <i>/myapp/src/**/*.ts</i>—All .ts files inside src directory (and all its subdirectories).</p> </li> <li> <p> <i>**/!(*.module).ts</i>—All .ts files but not .module.ts</p> </li> <li> <p> <i>*.png , *.jpg</i>—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).</p> </li> <li> <p> <i>*internal*</i>—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal_only', 'company_internal'.</p> </li> <li> <p> <i>**/*internal*</i>—All internal-related files in a directory and its subdirectories.</p> </li> </ul> <p>For more examples, see <a href="https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters">Use of Exclude and Include Filters</a> in the Amazon Web Services CLI Command Reference.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to exclude from your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:</p> <ul> <li> <p> <i>/myapp/config/*</i>—All files inside config directory.</p> </li> <li> <p> <i>**/*.png</i>—All .png files in all directories.</p> </li> <li> <p> <i>**/*.{png, ico, md}</i>—All .png, .ico or .md files in all directories.</p> </li> <li> <p> <i>/myapp/src/**/*.ts</i>—All .ts files inside src directory (and all its subdirectories).</p> </li> <li> <p> <i>**/!(*.module).ts</i>—All .ts files but not .module.ts</p> </li> <li> <p> <i>*.png , *.jpg</i>—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).</p> </li> <li> <p> <i>*internal*</i>—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal_only', 'company_internal'.</p> </li> <li> <p> <i>**/*internal*</i>—All internal-related files in a directory and its subdirectories.</p> </li> </ul> <p>For more examples, see <a href="https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters">Use of Exclude and Include Filters</a> in the Amazon Web Services CLI Command Reference.</p>"""
    documents_metadata_configuration: NotRequired[
        "capo_kendra.types.documents_metadata_configuration.DocumentsMetadataConfiguration"
    ]
    access_control_list_configuration: NotRequired[
        "capo_kendra.types.access_control_list_configuration.AccessControlListConfiguration"
    ]
    """<p>Provides the path to the S3 bucket that contains the user context filtering files for the data source. For the format of the file, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html">Access control for S3 data sources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataSourceConfiguration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "inclusion_prefixes" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["InclusionPrefixes"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["inclusion_prefixes"]
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
    if "documents_metadata_configuration" in value:
        import capo_kendra.types.documents_metadata_configuration

        out["DocumentsMetadataConfiguration"] = (
            capo_kendra.types.documents_metadata_configuration.serialize_aws_json_1_1(
                value["documents_metadata_configuration"]
            )
        )
    if "access_control_list_configuration" in value:
        import capo_kendra.types.access_control_list_configuration

        out["AccessControlListConfiguration"] = (
            capo_kendra.types.access_control_list_configuration.serialize_aws_json_1_1(
                value["access_control_list_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DataSourceConfiguration:
    out: S3DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3DataSourceConfiguration.bucket_name required")
    if data.get("InclusionPrefixes") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["inclusion_prefixes"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["InclusionPrefixes"]
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
    if data.get("DocumentsMetadataConfiguration") is not None:
        import capo_kendra.types.documents_metadata_configuration

        out["documents_metadata_configuration"] = (
            capo_kendra.types.documents_metadata_configuration.deserialize_aws_json_1_1(
                data["DocumentsMetadataConfiguration"]
            )
        )
    if data.get("AccessControlListConfiguration") is not None:
        import capo_kendra.types.access_control_list_configuration

        out["access_control_list_configuration"] = (
            capo_kendra.types.access_control_list_configuration.deserialize_aws_json_1_1(
                data["AccessControlListConfiguration"]
            )
        )
    return out
