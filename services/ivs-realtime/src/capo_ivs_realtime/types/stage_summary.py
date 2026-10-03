"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_name
    import capo_ivs_realtime.types.stage_session_id
    import capo_ivs_realtime.types.tags


class StageSummary(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    name: NotRequired["capo_ivs_realtime.types.stage_name.StageName"]
    """<p>Stage name.</p>"""
    active_session_id: NotRequired[
        "capo_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the active session within the stage.</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StageSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "active_session_id" in value:
        out["activeSessionId"] = value["active_session_id"]
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StageSummary:
    out: StageSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StageSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("activeSessionId") is not None:
        out["active_session_id"] = data["activeSessionId"]
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
