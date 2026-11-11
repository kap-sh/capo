"""Generated from Smithy shape ``com.amazonaws.ecs#TrustedExecutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.isolation_mode
    import capo_ecs.types.string


class TrustedExecutionConfiguration(TypedDict, closed=True):
    isolation_mode: "capo_ecs.types.isolation_mode.IsolationMode"
    """<p>The isolation mode for tasks that use this task definition. The isolation mode determines how a task is isolated from other tasks on the same Amazon EC2 instance.</p> <ul> <li> <p> <code>SHARED</code>: The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode.</p> </li> <li> <p> <code>ISOLATED_SANDBOX</code>: The task runs in its own <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html">Nitro Sandbox</a>, which is a lightweight virtual machine that is isolated by the Amazon Web Services Nitro System. Each task's sandbox is isolated from every other task's sandbox on the same Amazon EC2 instance, so one task can't access another task's memory or storage. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html">Isolated and confidential tasks</a> in <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>CONFIDENTIAL_SANDBOX</code>: The task runs in its own <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html">Nitro Sandbox</a>, which is a lightweight virtual machine that is isolated by the Amazon Web Services Nitro System, with cryptographic attestation. The host can't access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your Key Management Service key. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html">Isolated and confidential tasks</a> in <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> </ul>"""
    attestation_policy: NotRequired["capo_ecs.types.string.String"]
    """<p>The base64-encoded attestation policy envelope for the task. The policy specifies which containers are allowed to run and the runtime configuration that is cryptographically attested. This parameter is required when <code>isolationMode</code> is <code>CONFIDENTIAL_SANDBOX</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedExecutionConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.isolation_mode

    out["isolationMode"] = capo_ecs.types.isolation_mode.serialize_aws_json_1_1(
        value["isolation_mode"]
    )
    if "attestation_policy" in value:
        out["attestationPolicy"] = value["attestation_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedExecutionConfiguration:
    out: TrustedExecutionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("isolationMode") is not None:
        import capo_ecs.types.isolation_mode

        out["isolation_mode"] = capo_ecs.types.isolation_mode.deserialize_aws_json_1_1(
            data["isolationMode"]
        )
    else:
        import typing

        out["isolation_mode"] = typing.cast(
            "capo_ecs.types.isolation_mode.IsolationMode", ""
        )
    if data.get("attestationPolicy") is not None:
        out["attestation_policy"] = data["attestationPolicy"]
    return out
