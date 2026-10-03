"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackKeyPairSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_key_pair_arn
    import capo_ivs.types.playback_key_pair_name
    import capo_ivs.types.tags


class PlaybackKeyPairSummary(TypedDict, closed=True):
    arn: NotRequired["capo_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn"]
    """<p>Key-pair ARN.</p>"""
    name: NotRequired["capo_ivs.types.playback_key_pair_name.PlaybackKeyPairName"]
    """<p>Playback-key-pair name. The value does not need to be unique.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackKeyPairSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PlaybackKeyPairSummary:
    out: PlaybackKeyPairSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
