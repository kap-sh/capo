"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.customization_feature_config
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.output_config
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.tag_map
    import capo_rekognition.types.testing_data
    import capo_rekognition.types.training_data
    import capo_rekognition.types.version_description
    import capo_rekognition.types.version_name


class CreateProjectVersionRequest(TypedDict, closed=True):
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the Amazon Rekognition project that will manage the project version you want to train.</p>"""
    version_name: "capo_rekognition.types.version_name.VersionName"
    """<p>A name for the version of the project version. This value must be unique.</p>"""
    output_config: "capo_rekognition.types.output_config.OutputConfig"
    """<p>The Amazon S3 bucket location to store the results of training. The bucket can be any S3 bucket in your AWS account. You need <code>s3:PutObject</code> permission on the bucket. </p>"""
    training_data: NotRequired["capo_rekognition.types.training_data.TrainingData"]
    """<p>Specifies an external manifest that the services uses to train the project version. If you specify <code>TrainingData</code> you must also specify <code>TestingData</code>. The project must not have any associated datasets. </p>"""
    testing_data: NotRequired["capo_rekognition.types.testing_data.TestingData"]
    """<p>Specifies an external manifest that the service uses to test the project version. If you specify <code>TestingData</code> you must also specify <code>TrainingData</code>. The project must not have any associated datasets.</p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p> A set of tags (key-value pairs) that you want to attach to the project version. </p>"""
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training images, test images, and manifest files copied into the service for the project version. Your source images are unaffected. The key is also used to encrypt training results and manifest files written to the output Amazon S3 bucket (<code>OutputConfig</code>).</p> <p>If you choose to use your own KMS key, you need the following permissions on the KMS key.</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:Decrypt</p> </li> </ul> <p>If you don't specify a value for <code>KmsKeyId</code>, images copied into the service are encrypted using a key that AWS owns and manages.</p>"""
    version_description: NotRequired[
        "capo_rekognition.types.version_description.VersionDescription"
    ]
    """<p>A description applied to the project version being created.</p>"""
    feature_config: NotRequired[
        "capo_rekognition.types.customization_feature_config.CustomizationFeatureConfig"
    ]
    """<p>Feature-specific configuration of the training job. If the job configuration does not match the feature type associated with the project, an InvalidParameterException is returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectVersionRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    out["VersionName"] = value["version_name"]
    import capo_rekognition.types.output_config

    out["OutputConfig"] = capo_rekognition.types.output_config.serialize_aws_json_1_1(
        value["output_config"]
    )
    if "training_data" in value:
        import capo_rekognition.types.training_data

        out["TrainingData"] = (
            capo_rekognition.types.training_data.serialize_aws_json_1_1(
                value["training_data"]
            )
        )
    if "testing_data" in value:
        import capo_rekognition.types.testing_data

        out["TestingData"] = capo_rekognition.types.testing_data.serialize_aws_json_1_1(
            value["testing_data"]
        )
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "feature_config" in value:
        import capo_rekognition.types.customization_feature_config

        out["FeatureConfig"] = (
            capo_rekognition.types.customization_feature_config.serialize_aws_json_1_1(
                value["feature_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectVersionRequest:
    out: CreateProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        out["project_arn"] = ""
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
        raise DeserializationError("CreateProjectVersionRequest.output_config required")
    if data.get("TrainingData") is not None:
        import capo_rekognition.types.training_data

        out["training_data"] = (
            capo_rekognition.types.training_data.deserialize_aws_json_1_1(
                data["TrainingData"]
            )
        )
    if data.get("TestingData") is not None:
        import capo_rekognition.types.testing_data

        out["testing_data"] = (
            capo_rekognition.types.testing_data.deserialize_aws_json_1_1(
                data["TestingData"]
            )
        )
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("FeatureConfig") is not None:
        import capo_rekognition.types.customization_feature_config

        out["feature_config"] = (
            capo_rekognition.types.customization_feature_config.deserialize_aws_json_1_1(
                data["FeatureConfig"]
            )
        )
    return out
