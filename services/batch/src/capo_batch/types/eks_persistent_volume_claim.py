"""Generated from Smithy shape ``com.amazonaws.batch#EksPersistentVolumeClaim``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.string


class EksPersistentVolumeClaim(TypedDict, closed=True):
    claim_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the <code>persistentVolumeClaim</code> bounded to a <code>persistentVolume</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims"> Persistent Volume Claims</a> in the <i>Kubernetes documentation</i>.</p>"""
    read_only: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>An optional boolean value indicating if the mount is read only. Default is false. For more information, see <a href="https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts"> Read Only Mounts</a> in the <i>Kubernetes documentation</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPersistentVolumeClaim) -> dict:
    out: dict = {}
    if "claim_name" in value:
        out["claimName"] = value["claim_name"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    return out


def deserialize_json(data: dict) -> EksPersistentVolumeClaim:
    out: EksPersistentVolumeClaim = {}  # type: ignore[typeddict-item]
    if data.get("claimName") is not None:
        out["claim_name"] = data["claimName"]
    if data.get("readOnly") is not None:
        out["read_only"] = data["readOnly"]
    return out
