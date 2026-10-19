"""Generated from Smithy shape ``com.amazonaws.iot#StartThingRegistrationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.registry_s3_bucket_name
    import capo_iot.types.registry_s3_key_name
    import capo_iot.types.role_arn
    import capo_iot.types.template_body


class StartThingRegistrationTaskRequest(TypedDict, closed=True):
    template_body: "capo_iot.types.template_body.TemplateBody"
    """<p>The provisioning template.</p>"""
    input_file_bucket: "capo_iot.types.registry_s3_bucket_name.RegistryS3BucketName"
    """<p>The S3 bucket that contains the input file.</p>"""
    input_file_key: "capo_iot.types.registry_s3_key_name.RegistryS3KeyName"
    """<p>The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The IAM role ARN that grants permission the input file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThingRegistrationTaskRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    out["inputFileBucket"] = value["input_file_bucket"]
    out["inputFileKey"] = value["input_file_key"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StartThingRegistrationTaskRequest:
    out: StartThingRegistrationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateBody") is not None:
        out["template_body"] = data["templateBody"]
    else:
        out["template_body"] = ""
    if data.get("inputFileBucket") is not None:
        out["input_file_bucket"] = data["inputFileBucket"]
    else:
        out["input_file_bucket"] = ""
    if data.get("inputFileKey") is not None:
        out["input_file_key"] = data["inputFileKey"]
    else:
        out["input_file_key"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
