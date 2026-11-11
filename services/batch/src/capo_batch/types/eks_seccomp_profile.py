"""Generated from Smithy shape ``com.amazonaws.batch#EksSeccompProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_seccomp_localhost_profile
    import capo_batch.types.eks_seccomp_profile_type


class EksSeccompProfile(TypedDict, closed=True):
    type: NotRequired["capo_batch.types.eks_seccomp_profile_type.EksSeccompProfileType"]
    """<p>The seccomp profile type can be one of the following values:</p> <dl> <dt>RuntimeDefault</dt> <dd> <p>The <code>RuntimeDefault</code> value uses the container runtime's default seccomp profile.</p> </dd> <dt>Unconfined</dt> <dd> <p>The <code>Unconfined</code> value doesn't filter the container with seccomp.</p> </dd> <dt>Localhost</dt> <dd> <p>The <code>Localhost</code> value uses a custom profile at the path specified by <code>localhostProfile</code>.</p> </dd> </dl>"""
    localhost_profile: NotRequired[
        "capo_batch.types.eks_seccomp_localhost_profile.EksSeccompLocalhostProfile"
    ]
    """<p>The path of the profile on the node, relative to the configured seccomp profile location. You must specify this parameter when <code>type</code> is <code>Localhost</code>. Don't set this parameter for any other type. You are responsible for ensuring that the profile exists on every eligible worker node. For information about providing files to Amazon EKS nodes, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/eks-launch-templates.html">Use a launch template with Batch on Amazon EKS</a> in the <i>Batch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksSeccompProfile) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_batch.types.eks_seccomp_profile_type

        out["type"] = capo_batch.types.eks_seccomp_profile_type.serialize_json(
            value["type"]
        )
    if "localhost_profile" in value:
        out["localhostProfile"] = value["localhost_profile"]
    return out


def deserialize_json(data: dict) -> EksSeccompProfile:
    out: EksSeccompProfile = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_batch.types.eks_seccomp_profile_type

        out["type"] = capo_batch.types.eks_seccomp_profile_type.deserialize_json(
            data["type"]
        )
    if data.get("localhostProfile") is not None:
        out["localhost_profile"] = data["localhostProfile"]
    return out
