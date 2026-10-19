"""Generated from Smithy shape ``com.amazonaws.rekognition#CopyProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.output_config
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.project_version_arn
    import capo_rekognition.types.tag_map
    import capo_rekognition.types.version_name


class CopyProjectVersionRequest(TypedDict, closed=True):
    source_project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the source project in the trusting AWS account.</p>"""
    source_project_version_arn: (
        "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    )
    """<p>The ARN of the model version in the source project that you want to copy to a destination project.</p>"""
    destination_project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the project in the trusted AWS account that you want to copy the model version to. </p>"""
    version_name: "capo_rekognition.types.version_name.VersionName"
    """<p>A name for the version of the model that's copied to the destination project.</p>"""
    output_config: "capo_rekognition.types.output_config.OutputConfig"
    """<p>The S3 bucket and folder location where the training output for the source model version is placed.</p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p>The key-value tags to assign to the model version. </p>"""
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training results and manifest files written to the output Amazon S3 bucket (<code>OutputConfig</code>).</p> <p>If you choose to use your own KMS key, you need the following permissions on the KMS key.</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:Decrypt</p> </li> </ul> <p>If you don't specify a value for <code>KmsKeyId</code>, images copied into the service are encrypted using a key that AWS owns and manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProjectVersionRequest) -> dict:
    out: dict = {}
    out["SourceProjectArn"] = value["source_project_arn"]
    out["SourceProjectVersionArn"] = value["source_project_version_arn"]
    out["DestinationProjectArn"] = value["destination_project_arn"]
    out["VersionName"] = value["version_name"]
    import capo_rekognition.types.output_config

    out["OutputConfig"] = capo_rekognition.types.output_config.serialize_aws_json_1_1(
        value["output_config"]
    )
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProjectVersionRequest:
    out: CopyProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceProjectArn") is not None:
        out["source_project_arn"] = data["SourceProjectArn"]
    else:
        out["source_project_arn"] = ""
    if data.get("SourceProjectVersionArn") is not None:
        out["source_project_version_arn"] = data["SourceProjectVersionArn"]
    else:
        out["source_project_version_arn"] = ""
    if data.get("DestinationProjectArn") is not None:
        out["destination_project_arn"] = data["DestinationProjectArn"]
    else:
        out["destination_project_arn"] = ""
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    else:
        out["version_name"] = ""
    if data.get("OutputConfig") is not None:
        import capo_rekognition.types.output_config

        out["output_config"] = (
            capo_rekognition.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError("CopyProjectVersionRequest.output_config required")
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
