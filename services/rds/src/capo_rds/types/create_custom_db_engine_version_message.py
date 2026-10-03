"""Generated from Smithy shape ``com.amazonaws.rds#CreateCustomDBEngineVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.bucket_name
    import capo_rds.types.custom_db_engine_version_manifest
    import capo_rds.types.custom_engine_name
    import capo_rds.types.custom_engine_version
    import capo_rds.types.description
    import capo_rds.types.kms_key_id_or_arn
    import capo_rds.types.string255
    import capo_rds.types.string_list
    import capo_rds.types.tag_list


class CreateCustomDBEngineVersionMessage(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.custom_engine_name.CustomEngineName"]
    """<p>The database engine.</p> <p>RDS Custom for Oracle supports the following values:</p> <ul> <li> <p> <code>custom-oracle-ee</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> </p> </li> <li> <p> <code>custom-oracle-se2</code> </p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> </p> </li> </ul> <p>RDS Custom for SQL Server supports the following values:</p> <ul> <li> <p> <code>custom-sqlserver-ee</code> </p> </li> <li> <p> <code>custom-sqlserver-se</code> </p> </li> <li> <p> <code>custom-sqlserver-web</code> </p> </li> <li> <p> <code>custom-sqlserver-dev</code> </p> </li> </ul> <p>RDS for SQL Server supports the following values:</p> <ul> <li> <p> <code>sqlserver-ee</code> (Bring Your Own Media)</p> </li> <li> <p> <code>sqlserver-se</code> (Bring Your Own Media)</p> </li> <li> <p> <code>sqlserver-dev-ee</code> </p> </li> </ul>"""
    engine_version: NotRequired[
        "capo_rds.types.custom_engine_version.CustomEngineVersion"
    ]
    """<p>The name of your custom engine version (CEV).</p> <p>For RDS Custom for Oracle, the name format is <code>19.*customized_string*</code>. For example, a valid CEV name is <code>19.my_cev1</code>.</p> <p>For RDS Custom for SQL Server and RDS for SQL Server <code>sqlserver-dev-ee</code>, the name format is <code>*major_engine_version*.*minor_engine_version*.*customized_string*</code>. For example, a valid CEV name is <code>16.00.4215.2.my_cev1</code>.</p> <p>For RDS for SQL Server Bring Your Own Media (<code>sqlserver-ee</code>, <code>sqlserver-se</code>), specify the RDS engine version that you want to use. For example, <code>16.00.4175.1.v1</code>.</p> <p>The CEV name is unique per customer per Amazon Web Services Regions.</p>"""
    database_installation_files_s3_bucket_name: NotRequired[
        "capo_rds.types.bucket_name.BucketName"
    ]
    """<p>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is <code>my-custom-installation-files</code>.</p>"""
    database_installation_files_s3_prefix: NotRequired[
        "capo_rds.types.string255.String255"
    ]
    """<p>The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is <code>123456789012/cev1</code>. If this setting isn't specified, no prefix is assumed.</p>"""
    database_installation_files: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The database installation files (ISO and EXE) uploaded to Amazon S3 for your database engine version to import to Amazon RDS.</p> <p>For RDS for SQL Server Bring Your Own Media (<code>sqlserver-ee</code>, <code>sqlserver-se</code>), provide the SQL Server RTM ISO file once per major version and edition combination. Minor versions reuse the same file.</p>"""
    image_id: NotRequired["capo_rds.types.string255.String255"]
    """<p>The ID of the Amazon Machine Image (AMI). For RDS Custom for SQL Server, an AMI ID is required to create a CEV. For RDS Custom for Oracle, the default is the most recent AMI available, but you can specify an AMI ID that was used in a different Oracle CEV. Find the AMIs used by your CEVs by calling the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBEngineVersions.html">DescribeDBEngineVersions</a> operation.</p>"""
    kms_key_id: NotRequired["capo_rds.types.kms_key_id_or_arn.KmsKeyIdOrArn"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.</p> <p>If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you don't already have a symmetric encryption KMS key in your account, follow the instructions in <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk"> Creating a symmetric encryption KMS key</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p> <p>You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.</p>"""
    source_custom_db_engine_version_identifier: NotRequired[
        "capo_rds.types.string255.String255"
    ]
    """<p>The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either <code>Source</code> or <code>UseAwsProvidedLatestImage</code>. You can't specify a different JSON manifest when you specify <code>SourceCustomDbEngineVersionIdentifier</code>.</p>"""
    use_aws_provided_latest_image: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify <code>UseAwsProvidedLatestImage</code>, you can't also specify <code>ImageId</code>.</p>"""
    description: NotRequired["capo_rds.types.description.Description"]
    """<p>An optional description of your CEV.</p>"""
    manifest: NotRequired[
        "capo_rds.types.custom_db_engine_version_manifest.CustomDBEngineVersionManifest"
    ]
    """<p>The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.</p> <p>The following JSON fields are valid:</p> <dl> <dt>MediaImportTemplateVersion</dt> <dd> <p>Version of the CEV manifest. The date is in the format <code>YYYY-MM-DD</code>.</p> </dd> <dt>databaseInstallationFileNames</dt> <dd> <p>Ordered list of installation files for the CEV.</p> </dd> <dt>opatchFileNames</dt> <dd> <p>Ordered list of OPatch installers used for the Oracle DB engine.</p> </dd> <dt>psuRuPatchFileNames</dt> <dd> <p>The PSU and RU patches for this CEV.</p> </dd> <dt>OtherPatchFileNames</dt> <dd> <p>The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches.</p> </dd> </dl> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest"> Creating the CEV manifest</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCustomDBEngineVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "database_installation_files_s3_bucket_name" in value:
        pairs.append(
            (
                f"{key_prefix}DatabaseInstallationFilesS3BucketName",
                str(value["database_installation_files_s3_bucket_name"]),
            )
        )
    if "database_installation_files_s3_prefix" in value:
        pairs.append(
            (
                f"{key_prefix}DatabaseInstallationFilesS3Prefix",
                str(value["database_installation_files_s3_prefix"]),
            )
        )
    if "database_installation_files" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["database_installation_files"],
            pairs,
            f"{key_prefix}DatabaseInstallationFiles",
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KMSKeyId", str(value["kms_key_id"])))
    if "source_custom_db_engine_version_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SourceCustomDbEngineVersionIdentifier",
                str(value["source_custom_db_engine_version_identifier"]),
            )
        )
    if "use_aws_provided_latest_image" in value:
        pairs.append(
            (
                f"{key_prefix}UseAwsProvidedLatestImage",
                "true" if value["use_aws_provided_latest_image"] else "false",
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "manifest" in value:
        pairs.append((f"{key_prefix}Manifest", str(value["manifest"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateCustomDBEngineVersionMessage:
    out: CreateCustomDBEngineVersionMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_database_installation_files_s3_bucket_name = el.find(
        "DatabaseInstallationFilesS3BucketName"
    )
    if child_database_installation_files_s3_bucket_name is not None:
        out["database_installation_files_s3_bucket_name"] = str(
            child_database_installation_files_s3_bucket_name.text or ""
        )
    child_database_installation_files_s3_prefix = el.find(
        "DatabaseInstallationFilesS3Prefix"
    )
    if child_database_installation_files_s3_prefix is not None:
        out["database_installation_files_s3_prefix"] = str(
            child_database_installation_files_s3_prefix.text or ""
        )
    child_database_installation_files = el.find("DatabaseInstallationFiles")
    if child_database_installation_files is not None:
        import capo_rds.types.string_list

        out["database_installation_files"] = (
            capo_rds.types.string_list.deserialize_query(
                child_database_installation_files
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_kms_key_id = el.find("KMSKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_source_custom_db_engine_version_identifier = el.find(
        "SourceCustomDbEngineVersionIdentifier"
    )
    if child_source_custom_db_engine_version_identifier is not None:
        out["source_custom_db_engine_version_identifier"] = str(
            child_source_custom_db_engine_version_identifier.text or ""
        )
    child_use_aws_provided_latest_image = el.find("UseAwsProvidedLatestImage")
    if child_use_aws_provided_latest_image is not None:
        out["use_aws_provided_latest_image"] = (
            child_use_aws_provided_latest_image.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_manifest = el.find("Manifest")
    if child_manifest is not None:
        out["manifest"] = str(child_manifest.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
