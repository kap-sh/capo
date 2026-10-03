"""Generated from Smithy shape ``com.amazonaws.batch#EksVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_empty_dir
    import capo_batch.types.eks_host_path
    import capo_batch.types.eks_persistent_volume_claim
    import capo_batch.types.eks_secret
    import capo_batch.types.string


class EksVolume(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names">DNS subdomain names</a> in the <i>Kubernetes documentation</i>.</p>"""
    host_path: NotRequired["capo_batch.types.eks_host_path.EksHostPath"]
    """<p>Specifies the configuration of a Kubernetes <code>hostPath</code> volume. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/volumes/#hostpath">hostPath</a> in the <i>Kubernetes documentation</i>.</p>"""
    empty_dir: NotRequired["capo_batch.types.eks_empty_dir.EksEmptyDir"]
    """<p>Specifies the configuration of a Kubernetes <code>emptyDir</code> volume. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/volumes/#emptydir">emptyDir</a> in the <i>Kubernetes documentation</i>.</p>"""
    secret: NotRequired["capo_batch.types.eks_secret.EksSecret"]
    """<p>Specifies the configuration of a Kubernetes <code>secret</code> volume. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/volumes/#secret">secret</a> in the <i>Kubernetes documentation</i>.</p>"""
    persistent_volume_claim: NotRequired[
        "capo_batch.types.eks_persistent_volume_claim.EksPersistentVolumeClaim"
    ]
    """<p>Specifies the configuration of a Kubernetes <code>persistentVolumeClaim</code> bounded to a <code>persistentVolume</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims"> Persistent Volume Claims</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksVolume) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "host_path" in value:
        import capo_batch.types.eks_host_path

        out["hostPath"] = capo_batch.types.eks_host_path.serialize_json(
            value["host_path"]
        )
    if "empty_dir" in value:
        import capo_batch.types.eks_empty_dir

        out["emptyDir"] = capo_batch.types.eks_empty_dir.serialize_json(
            value["empty_dir"]
        )
    if "secret" in value:
        import capo_batch.types.eks_secret

        out["secret"] = capo_batch.types.eks_secret.serialize_json(value["secret"])
    if "persistent_volume_claim" in value:
        import capo_batch.types.eks_persistent_volume_claim

        out["persistentVolumeClaim"] = (
            capo_batch.types.eks_persistent_volume_claim.serialize_json(
                value["persistent_volume_claim"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksVolume:
    out: EksVolume = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("hostPath") is not None:
        import capo_batch.types.eks_host_path

        out["host_path"] = capo_batch.types.eks_host_path.deserialize_json(
            data["hostPath"]
        )
    if data.get("emptyDir") is not None:
        import capo_batch.types.eks_empty_dir

        out["empty_dir"] = capo_batch.types.eks_empty_dir.deserialize_json(
            data["emptyDir"]
        )
    if data.get("secret") is not None:
        import capo_batch.types.eks_secret

        out["secret"] = capo_batch.types.eks_secret.deserialize_json(data["secret"])
    if data.get("persistentVolumeClaim") is not None:
        import capo_batch.types.eks_persistent_volume_claim

        out["persistent_volume_claim"] = (
            capo_batch.types.eks_persistent_volume_claim.deserialize_json(
                data["persistentVolumeClaim"]
            )
        )
    return out
