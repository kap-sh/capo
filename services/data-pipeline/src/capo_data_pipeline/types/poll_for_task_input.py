"""Generated from Smithy shape ``com.amazonaws.datapipeline#PollForTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.instance_identity
    import capo_data_pipeline.types.string


class PollForTaskInput(TypedDict, closed=True):
    worker_group: "capo_data_pipeline.types.string.string"
    """<p>The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for <code>workerGroup</code> in the call to <code>PollForTask</code>. There are no wildcard values permitted in <code>workerGroup</code>; the string must be an exact, case-sensitive, match.</p>"""
    hostname: NotRequired["capo_data_pipeline.types.id.id"]
    """<p>The public DNS name of the calling task runner.</p>"""
    instance_identity: NotRequired[
        "capo_data_pipeline.types.instance_identity.InstanceIdentity"
    ]
    """<p>Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using <code>http://169.254.169.254/latest/meta-data/instance-id</code>. For more information, see <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html">Instance Metadata</a> in the <i>Amazon Elastic Compute Cloud User Guide.</i> Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForTaskInput) -> dict:
    out: dict = {}
    out["workerGroup"] = value["worker_group"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "instance_identity" in value:
        import capo_data_pipeline.types.instance_identity

        out["instanceIdentity"] = (
            capo_data_pipeline.types.instance_identity.serialize_aws_json_1_1(
                value["instance_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForTaskInput:
    out: PollForTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("workerGroup") is not None:
        out["worker_group"] = data["workerGroup"]
    else:
        raise DeserializationError("PollForTaskInput.worker_group required")
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("instanceIdentity") is not None:
        import capo_data_pipeline.types.instance_identity

        out["instance_identity"] = (
            capo_data_pipeline.types.instance_identity.deserialize_aws_json_1_1(
                data["instanceIdentity"]
            )
        )
    return out
