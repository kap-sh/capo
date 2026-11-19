"""Generated from Smithy shape ``com.amazonaws.codebuild#S3ReportExportConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.report_packaging_type
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class S3ReportExportConfig(TypedDict, closed=True):
    bucket: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The name of the S3 bucket where the raw data of a report are exported. </p>"""
    bucket_owner: NotRequired["capo_codebuild.types.string.String"]
    """<p>The Amazon Web Services account identifier of the owner of the Amazon S3 bucket. This allows report data to be exported to an Amazon S3 bucket that is owned by an account other than the account running the build.</p>"""
    path: NotRequired["capo_codebuild.types.string.String"]
    """<p> The path to the exported report's raw data results. </p>"""
    packaging: NotRequired[
        "capo_codebuild.types.report_packaging_type.ReportPackagingType"
    ]
    """<p> The type of build output artifact to create. Valid values include: </p> <ul> <li> <p> <code>NONE</code>: CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified. </p> </li> <li> <p> <code>ZIP</code>: CodeBuild creates a ZIP file with the raw data in the output bucket. </p> </li> </ul>"""
    encryption_key: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The encryption key for the report's encrypted raw data. </p>"""
    encryption_disabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> A boolean value that specifies if the results of a report are encrypted. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReportExportConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    if "path" in value:
        out["path"] = value["path"]
    if "packaging" in value:
        import capo_codebuild.types.report_packaging_type

        out["packaging"] = (
            capo_codebuild.types.report_packaging_type.serialize_aws_json_1_1(
                value["packaging"]
            )
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReportExportConfig:
    out: S3ReportExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("packaging") is not None:
        import capo_codebuild.types.report_packaging_type

        out["packaging"] = (
            capo_codebuild.types.report_packaging_type.deserialize_aws_json_1_1(
                data["packaging"]
            )
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("encryptionDisabled") is not None:
        out["encryption_disabled"] = data["encryptionDisabled"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ReportExportConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    if "path" in value:
        out["path"] = value["path"]
    if "packaging" in value:
        import capo_codebuild.types.report_packaging_type

        out["packaging"] = capo_codebuild.types.report_packaging_type.serialize_cbor(
            value["packaging"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    return out


def deserialize_cbor(data: dict) -> S3ReportExportConfig:
    out: S3ReportExportConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("bucketOwner") is not None:
        out["bucket_owner"] = data["bucketOwner"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("packaging") is not None:
        import capo_codebuild.types.report_packaging_type

        out["packaging"] = capo_codebuild.types.report_packaging_type.deserialize_cbor(
            data["packaging"]
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("encryptionDisabled") is not None:
        out["encryption_disabled"] = data["encryptionDisabled"]
    return out
