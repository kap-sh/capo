"""Generated from Smithy shape ``com.amazonaws.braket#CreateQuantumTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.associations
    import capo_braket.types.device_arn
    import capo_braket.types.experimental_capabilities
    import capo_braket.types.job_token
    import capo_braket.types.json_value
    import capo_braket.types.string64
    import capo_braket.types.tags_map


class CreateQuantumTaskRequest(TypedDict, closed=True):
    client_token: "capo_braket.types.string64.String64"
    """<p>The client token associated with the request.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device to run the quantum task on.</p>"""
    device_parameters: NotRequired["capo_braket.types.json_value.JsonValue"]
    """<p>The parameters for the device to run the quantum task on.</p>"""
    shots: "int"
    """<p>The number of shots to use for the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket to store quantum task result files in.</p>"""
    output_s3_key_prefix: "str"
    """<p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>"""
    action: "capo_braket.types.json_value.JsonValue"
    """<p>The action associated with the quantum task.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Tags to be added to the quantum task you're creating.</p>"""
    job_token: NotRequired["capo_braket.types.job_token.JobToken"]
    """<p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>"""
    associations: NotRequired["capo_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the quantum task.</p>"""
    experimental_capabilities: NotRequired[
        "capo_braket.types.experimental_capabilities.ExperimentalCapabilities"
    ]
    """<p>Enable experimental capabilities for the quantum task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuantumTaskRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["deviceArn"] = value["device_arn"]
    if "device_parameters" in value:
        out["deviceParameters"] = value["device_parameters"]
    out["shots"] = value["shots"]
    out["outputS3Bucket"] = value["output_s3_bucket"]
    out["outputS3KeyPrefix"] = value["output_s3_key_prefix"]
    out["action"] = value["action"]
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    if "job_token" in value:
        out["jobToken"] = value["job_token"]
    if "associations" in value:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.serialize_json(
            value["associations"]
        )
    if "experimental_capabilities" in value:
        import capo_braket.types.experimental_capabilities

        out["experimentalCapabilities"] = (
            capo_braket.types.experimental_capabilities.serialize_json(
                value["experimental_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateQuantumTaskRequest:
    out: CreateQuantumTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        out["device_arn"] = ""
    if data.get("deviceParameters") is not None:
        out["device_parameters"] = data["deviceParameters"]
    if data.get("shots") is not None:
        out["shots"] = data["shots"]
    else:
        out["shots"] = 0
    if data.get("outputS3Bucket") is not None:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        out["output_s3_bucket"] = ""
    if data.get("outputS3KeyPrefix") is not None:
        out["output_s3_key_prefix"] = data["outputS3KeyPrefix"]
    else:
        out["output_s3_key_prefix"] = ""
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    if data.get("jobToken") is not None:
        out["job_token"] = data["jobToken"]
    if data.get("associations") is not None:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.deserialize_json(
            data["associations"]
        )
    if data.get("experimentalCapabilities") is not None:
        import capo_braket.types.experimental_capabilities

        out["experimental_capabilities"] = (
            capo_braket.types.experimental_capabilities.deserialize_json(
                data["experimentalCapabilities"]
            )
        )
    return out
