"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.cluster_metadata


class ClusterDetails(TypedDict, closed=True):
    last_in_use: "datetime.datetime"
    """<p>The last timestamp when Amazon Inspector recorded the image in use in the task or pod in the cluster.</p>"""
    running_unit_count: NotRequired["int"]
    """<p>The number of tasks or pods where an image was running on the cluster.</p>"""
    stopped_unit_count: NotRequired["int"]
    """<p>The number of tasks or pods where an image was stopped on the cluster in the last 24 hours.</p>"""
    cluster_metadata: "capo_inspector2.types.cluster_metadata.ClusterMetadata"


# --- restJson1 ser/de ---
def serialize_json(value: ClusterDetails) -> dict:
    out: dict = {}
    import capo_inspector2.types._prelude.timestamp

    out["lastInUse"] = capo_inspector2.types._prelude.timestamp.serialize_json(
        value["last_in_use"]
    )
    if "running_unit_count" in value:
        out["runningUnitCount"] = value["running_unit_count"]
    if "stopped_unit_count" in value:
        out["stoppedUnitCount"] = value["stopped_unit_count"]
    import capo_inspector2.types.cluster_metadata

    out["clusterMetadata"] = capo_inspector2.types.cluster_metadata.serialize_json(
        value["cluster_metadata"]
    )
    return out


def deserialize_json(data: dict) -> ClusterDetails:
    out: ClusterDetails = {}  # type: ignore[typeddict-item]
    if data.get("lastInUse") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["last_in_use"] = capo_inspector2.types._prelude.timestamp.deserialize_json(
            data["lastInUse"]
        )
    else:
        import datetime

        out["last_in_use"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("runningUnitCount") is not None:
        out["running_unit_count"] = data["runningUnitCount"]
    if data.get("stoppedUnitCount") is not None:
        out["stopped_unit_count"] = data["stoppedUnitCount"]
    if data.get("clusterMetadata") is not None:
        import capo_inspector2.types.cluster_metadata

        out["cluster_metadata"] = (
            capo_inspector2.types.cluster_metadata.deserialize_json(
                data["clusterMetadata"]
            )
        )
    else:
        out["cluster_metadata"] = {"$unknown": {"name": ""}}
    return out
