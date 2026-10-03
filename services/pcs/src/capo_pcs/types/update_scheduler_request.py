"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateSchedulerRequest``."""

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError


class UpdateSchedulerRequest(TypedDict, closed=True):
    version: "str"
    """<p>The scheduler version to update the cluster to. You can only update to a newer version. For more information about supported versions and update paths, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html">Updating the scheduler version on a cluster</a> in the <i>PCS User Guide</i>.</p> <p>Valid Values: <code>24.05 | 24.11 | 25.05 | 25.11 | 26.05</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSchedulerRequest) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSchedulerRequest:
    out: UpdateSchedulerRequest = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdateSchedulerRequest.version required")
    return out
