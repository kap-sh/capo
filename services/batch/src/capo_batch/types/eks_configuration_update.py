"""Generated from Smithy shape ``com.amazonaws.batch#EksConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_access_entry


class EksConfigurationUpdate(TypedDict, closed=True):
    access_entry: NotRequired["capo_batch.types.eks_access_entry.EksAccessEntry"]
    """<p>The updated access entry configuration for the compute environment. Set <code>desiredState</code> to declare whether Batch will manage an access entry on the cluster. For the accepted values, see <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_EksAccessEntry.html"> <code>EksAccessEntry</code> </a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksConfigurationUpdate) -> dict:
    out: dict = {}
    if "access_entry" in value:
        import capo_batch.types.eks_access_entry

        out["accessEntry"] = capo_batch.types.eks_access_entry.serialize_json(
            value["access_entry"]
        )
    return out


def deserialize_json(data: dict) -> EksConfigurationUpdate:
    out: EksConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("accessEntry") is not None:
        import capo_batch.types.eks_access_entry

        out["access_entry"] = capo_batch.types.eks_access_entry.deserialize_json(
            data["accessEntry"]
        )
    return out
