"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateBatchPredictionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.iam_role_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.s3_bucket_location
    import capo_frauddetector.types.tag_list
    import capo_frauddetector.types.whole_number_version_string


class CreateBatchPredictionJobRequest(TypedDict, closed=True):
    job_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The ID of the batch prediction job.</p>"""
    input_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation"
    """<p>The Amazon S3 location of your training file.</p>"""
    output_path: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation"
    """<p>The Amazon S3 location of your output file.</p>"""
    event_type_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""
    detector_name: "capo_frauddetector.types.identifier.identifier"
    """<p>The name of the detector.</p>"""
    detector_version: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The detector version.</p>"""
    iam_role_arn: "capo_frauddetector.types.iam_role_arn.iamRoleArn"
    """<p>The ARN of the IAM role to use for this job request.</p> <p>The IAM Role must have read permissions to your input S3 bucket and write permissions to your output S3 bucket. For more information about bucket permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html">User policy examples</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchPredictionJobRequest) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["inputPath"] = value["input_path"]
    out["outputPath"] = value["output_path"]
    out["eventTypeName"] = value["event_type_name"]
    out["detectorName"] = value["detector_name"]
    if "detector_version" in value:
        out["detectorVersion"] = value["detector_version"]
    out["iamRoleArn"] = value["iam_role_arn"]
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchPredictionJobRequest:
    out: CreateBatchPredictionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("CreateBatchPredictionJobRequest.job_id required")
    if data.get("inputPath") is not None:
        out["input_path"] = data["inputPath"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionJobRequest.input_path required"
        )
    if data.get("outputPath") is not None:
        out["output_path"] = data["outputPath"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionJobRequest.output_path required"
        )
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionJobRequest.event_type_name required"
        )
    if data.get("detectorName") is not None:
        out["detector_name"] = data["detectorName"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionJobRequest.detector_name required"
        )
    if data.get("detectorVersion") is not None:
        out["detector_version"] = data["detectorVersion"]
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        raise DeserializationError(
            "CreateBatchPredictionJobRequest.iam_role_arn required"
        )
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
