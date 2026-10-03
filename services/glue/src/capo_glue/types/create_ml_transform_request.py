"""Generated from Smithy shape ``com.amazonaws.glue#CreateMLTransformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.glue_tables
    import capo_glue.types.glue_version_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.tags_map
    import capo_glue.types.timeout
    import capo_glue.types.transform_encryption
    import capo_glue.types.transform_parameters
    import capo_glue.types.worker_type


class CreateMLTransformRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The unique name that you give the transform when you create it.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the machine learning transform that is being defined. The default is an empty string.</p>"""
    input_record_tables: "capo_glue.types.glue_tables.GlueTables"
    """<p>A list of Glue table definitions used by the transform.</p>"""
    parameters: "capo_glue.types.transform_parameters.TransformParameters"
    """<p>The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type.</p>"""
    role: "capo_glue.types.role_string.RoleString"
    """<p>The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both Glue service role permissions to Glue resources, and Amazon S3 permissions required by the transform. </p> <ul> <li> <p>This role needs Glue service role permissions to allow access to resources in Glue. See <a href="https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html">Attach a Policy to IAM Users That Access Glue</a>.</p> </li> <li> <p>This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.</p> </li> </ul>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions">Glue Versions</a> in the developer guide.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/">Glue pricing page</a>. </p> <p> <code>MaxCapacity</code> is a mutually exclusive option with <code>NumberOfWorkers</code> and <code>WorkerType</code>.</p> <ul> <li> <p>If either <code>NumberOfWorkers</code> or <code>WorkerType</code> is set, then <code>MaxCapacity</code> cannot be set.</p> </li> <li> <p>If <code>MaxCapacity</code> is set then neither <code>NumberOfWorkers</code> or <code>WorkerType</code> can be set.</p> </li> <li> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p> </li> <li> <p> <code>MaxCapacity</code> and <code>NumberOfWorkers</code> must both be at least 1.</p> </li> </ul> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p> <p>When the <code>WorkerType</code> field is set to a value other than <code>Standard</code>, the <code>MaxCapacity</code> field is set automatically and becomes read-only.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.</p> </li> </ul> <p> <code>MaxCapacity</code> is a mutually exclusive option with <code>NumberOfWorkers</code> and <code>WorkerType</code>.</p> <ul> <li> <p>If either <code>NumberOfWorkers</code> or <code>WorkerType</code> is set, then <code>MaxCapacity</code> cannot be set.</p> </li> <li> <p>If <code>MaxCapacity</code> is set then neither <code>NumberOfWorkers</code> or <code>WorkerType</code> can be set.</p> </li> <li> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p> </li> <li> <p> <code>MaxCapacity</code> and <code>NumberOfWorkers</code> must both be at least 1.</p> </li> </ul>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when this task runs.</p> <p>If <code>WorkerType</code> is set, then <code>NumberOfWorkers</code> is required (and vice versa).</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    max_retries: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of times to retry a task for this transform after a task run fails.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in Glue, see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html">Amazon Web Services Tags in Glue</a> in the developer guide.</p>"""
    transform_encryption: NotRequired[
        "capo_glue.types.transform_encryption.TransformEncryption"
    ]
    """<p>The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMLTransformRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.glue_tables

    out["InputRecordTables"] = capo_glue.types.glue_tables.serialize_aws_json_1_1(
        value["input_record_tables"]
    )
    import capo_glue.types.transform_parameters

    out["Parameters"] = capo_glue.types.transform_parameters.serialize_aws_json_1_1(
        value["parameters"]
    )
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
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "transform_encryption" in value:
        import capo_glue.types.transform_encryption

        out["TransformEncryption"] = (
            capo_glue.types.transform_encryption.serialize_aws_json_1_1(
                value["transform_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMLTransformRequest:
    out: CreateMLTransformRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateMLTransformRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("InputRecordTables") is not None:
        import capo_glue.types.glue_tables

        out["input_record_tables"] = (
            capo_glue.types.glue_tables.deserialize_aws_json_1_1(
                data["InputRecordTables"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMLTransformRequest.input_record_tables required"
        )
    if data.get("Parameters") is not None:
        import capo_glue.types.transform_parameters

        out["parameters"] = (
            capo_glue.types.transform_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    else:
        raise DeserializationError("CreateMLTransformRequest.parameters required")
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("CreateMLTransformRequest.role required")
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
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("TransformEncryption") is not None:
        import capo_glue.types.transform_encryption

        out["transform_encryption"] = (
            capo_glue.types.transform_encryption.deserialize_aws_json_1_1(
                data["TransformEncryption"]
            )
        )
    return out
