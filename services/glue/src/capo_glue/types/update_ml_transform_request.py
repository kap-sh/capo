"""Generated from Smithy shape ``com.amazonaws.glue#UpdateMLTransformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.glue_version_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.timeout
    import capo_glue.types.transform_parameters
    import capo_glue.types.worker_type


class UpdateMLTransformRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>A unique identifier that was generated when the transform was created.</p>"""
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The unique name that you gave the transform when you created it.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the transform. The default is an empty string.</p>"""
    parameters: NotRequired["capo_glue.types.transform_parameters.TransformParameters"]
    """<p>The configuration parameters that are specific to the transform type (algorithm) used. Conditionally dependent on the transform type.</p>"""
    role: NotRequired["capo_glue.types.role_string.RoleString"]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.</p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions">Glue Versions</a> in the developer guide.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/">Glue pricing page</a>. </p> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.</p> </li> </ul>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when this task runs.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    max_retries: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of times to retry a task for this transform after a task run fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMLTransformRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_glue.types.transform_parameters

        out["Parameters"] = capo_glue.types.transform_parameters.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "max_capacity" in value:
        out["MaxCapacity"] = (
            "NaN"
            if value["max_capacity"] != value["max_capacity"]
            else "Infinity"
            if value["max_capacity"] == float("inf")
            else "-Infinity"
            if value["max_capacity"] == float("-inf")
            else value["max_capacity"]
        )
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "max_retries" in value:
        out["MaxRetries"] = value["max_retries"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMLTransformRequest:
    out: UpdateMLTransformRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("UpdateMLTransformRequest.transform_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_glue.types.transform_parameters

        out["parameters"] = (
            capo_glue.types.transform_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = float(data["MaxCapacity"])
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("MaxRetries") is not None:
        out["max_retries"] = data["MaxRetries"]
    return out
