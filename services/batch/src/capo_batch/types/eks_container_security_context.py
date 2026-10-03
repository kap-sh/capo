"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerSecurityContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.long


class EksContainerSecurityContext(TypedDict, closed=True):
    run_as_user: NotRequired["capo_batch.types.long.Long"]
    """<p>When this parameter is specified, the container is run as the specified user ID (<code>uid</code>). If this parameter isn't specified, the default is the user that's specified in the image metadata. This parameter maps to <code>RunAsUser</code> and <code>MustRanAs</code> policy in the <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups">Users and groups pod security policies</a> in the <i>Kubernetes documentation</i>.</p>"""
    run_as_group: NotRequired["capo_batch.types.long.Long"]
    """<p>When this parameter is specified, the container is run as the specified group ID (<code>gid</code>). If this parameter isn't specified, the default is the group that's specified in the image metadata. This parameter maps to <code>RunAsGroup</code> and <code>MustRunAs</code> policy in the <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups">Users and groups pod security policies</a> in the <i>Kubernetes documentation</i>.</p>"""
    privileged: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>When this parameter is <code>true</code>, the container is given elevated permissions on the host container instance. The level of permissions are similar to the <code>root</code> user permissions. The default value is <code>false</code>. This parameter maps to <code>privileged</code> policy in the <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#privileged">Privileged pod security policies</a> in the <i>Kubernetes documentation</i>.</p>"""
    allow_privilege_escalation: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process. The default value is <code>false</code>.</p>"""
    read_only_root_filesystem: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>When this parameter is <code>true</code>, the container is given read-only access to its root file system. The default value is <code>false</code>. This parameter maps to <code>ReadOnlyRootFilesystem</code> policy in the <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#volumes-and-file-systems">Volumes and file systems pod security policies</a> in the <i>Kubernetes documentation</i>.</p>"""
    run_as_non_root: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>When this parameter is specified, the container is run as a user with a <code>uid</code> other than 0. If this parameter isn't specified, so such rule is enforced. This parameter maps to <code>RunAsUser</code> and <code>MustRunAsNonRoot</code> policy in the <a href="https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups">Users and groups pod security policies</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerSecurityContext) -> dict:
    out: dict = {}
    if "run_as_user" in value:
        out["runAsUser"] = value["run_as_user"]
    if "run_as_group" in value:
        out["runAsGroup"] = value["run_as_group"]
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "allow_privilege_escalation" in value:
        out["allowPrivilegeEscalation"] = value["allow_privilege_escalation"]
    if "read_only_root_filesystem" in value:
        out["readOnlyRootFilesystem"] = value["read_only_root_filesystem"]
    if "run_as_non_root" in value:
        out["runAsNonRoot"] = value["run_as_non_root"]
    return out


def deserialize_json(data: dict) -> EksContainerSecurityContext:
    out: EksContainerSecurityContext = {}  # type: ignore[typeddict-item]
    if data.get("runAsUser") is not None:
        out["run_as_user"] = data["runAsUser"]
    if data.get("runAsGroup") is not None:
        out["run_as_group"] = data["runAsGroup"]
    if data.get("privileged") is not None:
        out["privileged"] = data["privileged"]
    if data.get("allowPrivilegeEscalation") is not None:
        out["allow_privilege_escalation"] = data["allowPrivilegeEscalation"]
    if data.get("readOnlyRootFilesystem") is not None:
        out["read_only_root_filesystem"] = data["readOnlyRootFilesystem"]
    if data.get("runAsNonRoot") is not None:
        out["run_as_non_root"] = data["runAsNonRoot"]
    return out
