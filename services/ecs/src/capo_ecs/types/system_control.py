"""Generated from Smithy shape ``com.amazonaws.ecs#SystemControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class SystemControl(TypedDict, closed=True):
    namespace: NotRequired["capo_ecs.types.string.String"]
    """<p>The namespaced kernel parameter to set a <code>value</code> for.</p>"""
    value: NotRequired["capo_ecs.types.string.String"]
    """<p>The namespaced kernel parameter to set a <code>value</code> for.</p> <p>Valid IPC namespace values: <code>"kernel.msgmax" | "kernel.msgmnb" | "kernel.msgmni" | "kernel.sem" | "kernel.shmall" | "kernel.shmmax" | "kernel.shmmni" | "kernel.shm_rmid_forced"</code>, and <code>Sysctls</code> that start with <code>"fs.mqueue.*"</code> </p> <p>Valid network namespace values: <code>Sysctls</code> that start with <code>"net.*"</code>. Only namespaced <code>Sysctls</code> that exist within the container starting with "net.* are accepted.</p> <p>All of these values are supported by Fargate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemControl) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemControl:
    out: SystemControl = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
