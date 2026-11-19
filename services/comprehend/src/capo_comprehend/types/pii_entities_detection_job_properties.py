"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.input_data_config
    import capo_comprehend.types.job_id
    import capo_comprehend.types.job_name
    import capo_comprehend.types.job_status
    import capo_comprehend.types.language_code
    import capo_comprehend.types.pii_entities_detection_mode
    import capo_comprehend.types.pii_output_data_config
    import capo_comprehend.types.redaction_config
    import capo_comprehend.types.timestamp


class PiiEntitiesDetectionJobProperties(TypedDict, closed=True):
    job_id: NotRequired["capo_comprehend.types.job_id.JobId"]
    """<p>The identifier assigned to the PII entities detection job.</p>"""
    job_arn: NotRequired["capo_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the PII entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:pii-entities-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_name: NotRequired["capo_comprehend.types.job_name.JobName"]
    """<p>The name that you assigned the PII entities detection job.</p>"""
    job_status: NotRequired["capo_comprehend.types.job_status.JobStatus"]
    """<p>The current status of the PII entities detection job. If the status is <code>FAILED</code>, the <code>Message</code> field shows the reason for the failure.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of a job.</p>"""
    submit_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the PII entities detection job was submitted for processing.</p>"""
    end_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the PII entities detection job completed.</p>"""
    input_data_config: NotRequired[
        "capo_comprehend.types.input_data_config.InputDataConfig"
    ]
    """<p>The input properties for a PII entities detection job.</p>"""
    output_data_config: NotRequired[
        "capo_comprehend.types.pii_output_data_config.PiiOutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the PII entities detection job.</p>"""
    redaction_config: NotRequired[
        "capo_comprehend.types.redaction_config.RedactionConfig"
    ]
    """<p>Provides configuration parameters for PII entity redaction.</p> <p>This parameter is required if you set the <code>Mode</code> parameter to <code>ONLY_REDACTION</code>. In that case, you must provide a <code>RedactionConfig</code> definition that includes the <code>PiiEntityTypes</code> parameter.</p>"""
    language_code: NotRequired["capo_comprehend.types.language_code.LanguageCode"]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    mode: NotRequired[
        "capo_comprehend.types.pii_entities_detection_mode.PiiEntitiesDetectionMode"
    ]
    """<p>Specifies whether the output provides the locations (offsets) of PII entities or a file in which PII entities are redacted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntitiesDetectionJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
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
    if "input_data_config" in value:
        import capo_comprehend.types.input_data_config

        out["InputDataConfig"] = (
            capo_comprehend.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import capo_comprehend.types.pii_output_data_config

        out["OutputDataConfig"] = (
            capo_comprehend.types.pii_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "redaction_config" in value:
        import capo_comprehend.types.redaction_config

        out["RedactionConfig"] = (
            capo_comprehend.types.redaction_config.serialize_aws_json_1_1(
                value["redaction_config"]
            )
        )
    if "language_code" in value:
        import capo_comprehend.types.language_code

        out["LanguageCode"] = (
            capo_comprehend.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "mode" in value:
        import capo_comprehend.types.pii_entities_detection_mode

        out["Mode"] = (
            capo_comprehend.types.pii_entities_detection_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PiiEntitiesDetectionJobProperties:
    out: PiiEntitiesDetectionJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
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
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehend.types.pii_output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.pii_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if data.get("RedactionConfig") is not None:
        import capo_comprehend.types.redaction_config

        out["redaction_config"] = (
            capo_comprehend.types.redaction_config.deserialize_aws_json_1_1(
                data["RedactionConfig"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Mode") is not None:
        import capo_comprehend.types.pii_entities_detection_mode

        out["mode"] = (
            capo_comprehend.types.pii_entities_detection_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PiiEntitiesDetectionJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_comprehend.types.job_status

        out["JobStatus"] = capo_comprehend.types.job_status.serialize_cbor(
            value["job_status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["submit_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "input_data_config" in value:
        import capo_comprehend.types.input_data_config

        out["InputDataConfig"] = capo_comprehend.types.input_data_config.serialize_cbor(
            value["input_data_config"]
        )
    if "output_data_config" in value:
        import capo_comprehend.types.pii_output_data_config

        out["OutputDataConfig"] = (
            capo_comprehend.types.pii_output_data_config.serialize_cbor(
                value["output_data_config"]
            )
        )
    if "redaction_config" in value:
        import capo_comprehend.types.redaction_config

        out["RedactionConfig"] = capo_comprehend.types.redaction_config.serialize_cbor(
            value["redaction_config"]
        )
    if "language_code" in value:
        import capo_comprehend.types.language_code

        out["LanguageCode"] = capo_comprehend.types.language_code.serialize_cbor(
            value["language_code"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "mode" in value:
        import capo_comprehend.types.pii_entities_detection_mode

        out["Mode"] = capo_comprehend.types.pii_entities_detection_mode.serialize_cbor(
            value["mode"]
        )
    return out


def deserialize_cbor(data: dict) -> PiiEntitiesDetectionJobProperties:
    out: PiiEntitiesDetectionJobProperties = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    if data.get("JobArn") is not None:
        out["job_arn"] = data["JobArn"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_comprehend.types.job_status

        out["job_status"] = capo_comprehend.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("SubmitTime") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["SubmitTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.input_data_config.deserialize_cbor(
                data["InputDataConfig"]
            )
        )
    if data.get("OutputDataConfig") is not None:
        import capo_comprehend.types.pii_output_data_config

        out["output_data_config"] = (
            capo_comprehend.types.pii_output_data_config.deserialize_cbor(
                data["OutputDataConfig"]
            )
        )
    if data.get("RedactionConfig") is not None:
        import capo_comprehend.types.redaction_config

        out["redaction_config"] = (
            capo_comprehend.types.redaction_config.deserialize_cbor(
                data["RedactionConfig"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = capo_comprehend.types.language_code.deserialize_cbor(
            data["LanguageCode"]
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Mode") is not None:
        import capo_comprehend.types.pii_entities_detection_mode

        out["mode"] = (
            capo_comprehend.types.pii_entities_detection_mode.deserialize_cbor(
                data["Mode"]
            )
        )
    return out
