"""Generated from Smithy shape ``com.amazonaws.ecs#TrustedExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.attestation_policy_status
    import capo_ecs.types.isolation_mode


class TrustedExecutionSummary(TypedDict, closed=True):
    isolation_mode: "capo_ecs.types.isolation_mode.IsolationMode"
    """<p>The isolation mode that the task runs in. This value mirrors the <code>isolationMode</code> that was set in the task definition's <code>TrustedExecutionConfiguration</code>.</p> <ul> <li> <p> <code>SHARED</code>: The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode.</p> </li> <li> <p> <code>ISOLATED_SANDBOX</code>: The task runs in its own <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html">Nitro Sandbox</a>, which is a lightweight virtual machine that is isolated by the Amazon Web Services Nitro System. Each task's sandbox is isolated from every other task's sandbox on the same Amazon EC2 instance, so one task can't access another task's memory or storage. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html">Isolated and confidential tasks</a> in <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>CONFIDENTIAL_SANDBOX</code>: The task runs in its own <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html">Nitro Sandbox</a>, which is a lightweight virtual machine that is isolated by the Amazon Web Services Nitro System, with cryptographic attestation. The host can't access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your Key Management Service key. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html">Isolated and confidential tasks</a> in <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> </ul>"""
    attestation_policy_status: NotRequired[
        "capo_ecs.types.attestation_policy_status.AttestationPolicyStatus"
    ]
    """<p>The status of the attestation policy for the task. This value is present only for tasks that use the <code>CONFIDENTIAL_SANDBOX</code> isolation mode.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedExecutionSummary) -> dict:
    out: dict = {}
    import capo_ecs.types.isolation_mode

    out["isolationMode"] = capo_ecs.types.isolation_mode.serialize_aws_json_1_1(
        value["isolation_mode"]
    )
    if "attestation_policy_status" in value:
        import capo_ecs.types.attestation_policy_status

        out["attestationPolicyStatus"] = (
            capo_ecs.types.attestation_policy_status.serialize_aws_json_1_1(
                value["attestation_policy_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedExecutionSummary:
    out: TrustedExecutionSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("attestationPolicyStatus") is not None:
        import capo_ecs.types.attestation_policy_status

        out["attestation_policy_status"] = (
            capo_ecs.types.attestation_policy_status.deserialize_aws_json_1_1(
                data["attestationPolicyStatus"]
            )
        )
    return out
