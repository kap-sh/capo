"""Generated from Smithy shape ``com.amazonaws.omics#CreateRunGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_group_name
    import capo_omics.types.run_group_request_id
    import capo_omics.types.tag_map


class CreateRunGroupRequest(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.run_group_name.RunGroupName"]
    """<p>A name for the group.</p>"""
    max_cpus: NotRequired["int"]
    """<p>The maximum number of CPUs that can run concurrently across all active runs in the run group.</p>"""
    max_runs: NotRequired["int"]
    """<p>The maximum number of runs that can be running at the same time.</p>"""
    max_duration: NotRequired["int"]
    """<p>The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the group.</p>"""
    request_id: "capo_omics.types.run_group_request_id.RunGroupRequestId"
    """<p>To ensure that requests don't run multiple times, specify a unique ID for each request.</p>"""
    max_gpus: NotRequired["int"]
    """<p>The maximum number of GPUs that can run concurrently across all active runs in the run group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRunGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "max_cpus" in value:
        out["maxCpus"] = value["max_cpus"]
    if "max_runs" in value:
        out["maxRuns"] = value["max_runs"]
    if "max_duration" in value:
        out["maxDuration"] = value["max_duration"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    if "max_gpus" in value:
        out["maxGpus"] = value["max_gpus"]
    return out


def deserialize_json(data: dict) -> CreateRunGroupRequest:
    out: CreateRunGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("maxCpus") is not None:
        out["max_cpus"] = data["maxCpus"]
    if data.get("maxRuns") is not None:
        out["max_runs"] = data["maxRuns"]
    if data.get("maxDuration") is not None:
        out["max_duration"] = data["maxDuration"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    if data.get("maxGpus") is not None:
        out["max_gpus"] = data["maxGpus"]
    return out
