"""Generated from Smithy shape ``com.amazonaws.batch#EksPodSecurityContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.eks_seccomp_profile
    import capo_batch.types.long


class EksPodSecurityContext(TypedDict, closed=True):
    run_as_user: NotRequired["capo_batch.types.long.Long"]
    """<p>The user ID that runs containers in the pod when a container does not specify its own user ID. The supported value range is <code>0</code> through <code>2147483647</code>.</p>"""
    run_as_group: NotRequired["capo_batch.types.long.Long"]
    """<p>The primary group ID that runs containers in the pod when a container does not specify its own group ID. The supported value range is <code>0</code> through <code>2147483647</code>.</p>"""
    run_as_non_root: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether Kubernetes validates that containers in the pod don't run as the root user unless a container specifies an overriding value.</p>"""
    seccomp_profile: NotRequired[
        "capo_batch.types.eks_seccomp_profile.EksSeccompProfile"
    ]
    """<p>The default seccomp profile for containers in the pod. A container-level seccomp profile overrides this value.</p>"""
    fs_group: NotRequired["capo_batch.types.long.Long"]
    """<p>A special supplemental group that is applied to all containers in the pod. Some volume types allow Kubernetes to change the ownership and permissions of the volume contents to this group when the volume is mounted. The supported value range is <code>0</code> through <code>2147483647</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPodSecurityContext) -> dict:
    out: dict = {}
    if "run_as_user" in value:
        out["runAsUser"] = value["run_as_user"]
    if "run_as_group" in value:
        out["runAsGroup"] = value["run_as_group"]
    if "run_as_non_root" in value:
        out["runAsNonRoot"] = value["run_as_non_root"]
    if "seccomp_profile" in value:
        import capo_batch.types.eks_seccomp_profile

        out["seccompProfile"] = capo_batch.types.eks_seccomp_profile.serialize_json(
            value["seccomp_profile"]
        )
    if "fs_group" in value:
        out["fsGroup"] = value["fs_group"]
    return out


def deserialize_json(data: dict) -> EksPodSecurityContext:
    out: EksPodSecurityContext = {}  # type: ignore[typeddict-item]
    if data.get("runAsUser") is not None:
        out["run_as_user"] = data["runAsUser"]
    if data.get("runAsGroup") is not None:
        out["run_as_group"] = data["runAsGroup"]
    if data.get("runAsNonRoot") is not None:
        out["run_as_non_root"] = data["runAsNonRoot"]
    if data.get("seccompProfile") is not None:
        import capo_batch.types.eks_seccomp_profile

        out["seccomp_profile"] = capo_batch.types.eks_seccomp_profile.deserialize_json(
            data["seccompProfile"]
        )
    if data.get("fsGroup") is not None:
        out["fs_group"] = data["fsGroup"]
    return out
