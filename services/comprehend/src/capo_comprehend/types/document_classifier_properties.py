"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.classifier_metadata
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.document_classifier_arn
    import capo_comprehend.types.document_classifier_input_data_config
    import capo_comprehend.types.document_classifier_mode
    import capo_comprehend.types.document_classifier_output_data_config
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.model_status
    import capo_comprehend.types.timestamp
    import capo_comprehend.types.version_name
    import capo_comprehend.types.vpc_config


class DocumentClassifierProperties(TypedDict, closed=True):
    document_classifier_arn: NotRequired[
        "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the document classifier.</p>"""
    language_code: NotRequired["capo_comprehend.types.language_code.LanguageCode"]
    """<p>The language code for the language of the documents that the classifier was trained on.</p>"""
    status: NotRequired["capo_comprehend.types.model_status.ModelStatus"]
    """<p>The status of the document classifier. If the status is <code>TRAINED</code> the classifier is ready to use. If the status is <code>TRAINED_WITH_WARNINGS</code> the classifier training succeeded, but you should review the warnings returned in the <code>CreateDocumentClassifier</code> response.</p> <p> If the status is <code>FAILED</code> you can see additional information about why the classifier wasn't trained in the <code>Message</code> field.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>Additional information about the status of the classifier.</p>"""
    submit_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the document classifier was submitted for training.</p>"""
    end_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that training the document classifier completed.</p>"""
    training_start_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Indicates the time when the training starts on documentation classifiers. You are billed for the time interval between this time and the value of TrainingEndTime. </p>"""
    training_end_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that training of the document classifier was completed. Indicates the time when the training completes on documentation classifiers. You are billed for the time interval between this time and the value of TrainingStartTime.</p>"""
    input_data_config: NotRequired[
        "capo_comprehend.types.document_classifier_input_data_config.DocumentClassifierInputDataConfig"
    ]
    """<p>The input data configuration that you supplied when you created the document classifier for training.</p>"""
    output_data_config: NotRequired[
        "capo_comprehend.types.document_classifier_output_data_config.DocumentClassifierOutputDataConfig"
    ]
    """<p> Provides output results configuration parameters for custom classifier jobs.</p>"""
    classifier_metadata: NotRequired[
        "capo_comprehend.types.classifier_metadata.ClassifierMetadata"
    ]
    """<p>Information about the document classifier, including the number of documents used for training the classifier, the number of documents used for test the classifier, and an accuracy rating.</p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]
    """<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>"""
    mode: NotRequired[
        "capo_comprehend.types.document_classifier_mode.DocumentClassifierMode"
    ]
    """<p>Indicates the mode in which the specific classifier was trained. This also indicates the format of input documents and the format of the confusion matrix. Each classifier can only be trained in one mode and this cannot be changed once the classifier is trained.</p>"""
    model_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    version_name: NotRequired["capo_comprehend.types.version_name.VersionName"]
    """<p>The version name that you assigned to the document classifier.</p>"""
    source_model_arn: NotRequired[
        "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source model. This model was imported from a different Amazon Web Services account to create the document classifier model in your Amazon Web Services account.</p>"""
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierProperties) -> dict:
    out: dict = {}
    if "document_classifier_arn" in value:
        out["DocumentClassifierArn"] = value["document_classifier_arn"]
    if "language_code" in value:
        import capo_comprehend.types.language_code

        out["LanguageCode"] = (
            capo_comprehend.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "status" in value:
        import capo_comprehend.types.model_status

        out["Status"] = capo_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "training_start_time" in value:
        import capo_comprehend.types.timestamp

        out["TrainingStartTime"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["training_start_time"]
            )
        )
    if "training_end_time" in value:
        import capo_comprehend.types.timestamp

        out["TrainingEndTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["training_end_time"]
        )
    if "input_data_config" in value:
        import capo_comprehend.types.document_classifier_input_data_config

        out["InputDataConfig"] = (
            capo_comprehend.types.document_classifier_input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_comprehend.types.document_classifier_output_data_config

        out["OutputDataConfig"] = (
            capo_comprehend.types.document_classifier_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "classifier_metadata" in value:
        import capo_comprehend.types.classifier_metadata

        out["ClassifierMetadata"] = (
            capo_comprehend.types.classifier_metadata.serialize_aws_json_1_1(
                value["classifier_metadata"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "mode" in value:
        import capo_comprehend.types.document_classifier_mode

        out["Mode"] = (
            capo_comprehend.types.document_classifier_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "source_model_arn" in value:
        out["SourceModelArn"] = value["source_model_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierProperties:
    out: DocumentClassifierProperties = {}  # type: ignore[typeddict-item]
    if data.get("DocumentClassifierArn") is not None:
        out["document_classifier_arn"] = data["DocumentClassifierArn"]
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("Status") is not None:
        import capo_comprehend.types.model_status

        out["status"] = capo_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmitTime") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["SubmitTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("TrainingStartTime") is not None:
        import capo_comprehend.types.timestamp

        out["training_start_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingStartTime"]
            )
        )
    if data.get("TrainingEndTime") is not None:
        import capo_comprehend.types.timestamp

        out["training_end_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.document_classifier_input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.document_classifier_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehend.types.document_classifier_output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.document_classifier_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("ClassifierMetadata") is not None:
        import capo_comprehend.types.classifier_metadata

        out["classifier_metadata"] = (
            capo_comprehend.types.classifier_metadata.deserialize_aws_json_1_1(
                data["ClassifierMetadata"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("VpcConfig") is not None:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("Mode") is not None:
        import capo_comprehend.types.document_classifier_mode

        out["mode"] = (
            capo_comprehend.types.document_classifier_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    if data.get("ModelKmsKeyId") is not None:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("SourceModelArn") is not None:
        out["source_model_arn"] = data["SourceModelArn"]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
