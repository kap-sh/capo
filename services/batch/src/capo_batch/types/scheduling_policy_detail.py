"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.fairshare_policy
    import capo_batch.types.quota_share_policy
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class SchedulingPolicyDetail(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the fair-share scheduling policy.</p>"""
    arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the scheduling policy. An example is <code>arn:<i>aws</i>:batch:<i>us-east-1</i>:<i>123456789012</i>:scheduling-policy/<i>HighPriority</i> </code>.</p>"""
    quota_share_policy: NotRequired[
        "capo_batch.types.quota_share_policy.QuotaSharePolicy"
    ]
    """<p>The quota share scheduling policy details.</p>"""
    fairshare_policy: NotRequired["capo_batch.types.fairshare_policy.FairsharePolicy"]
    """<p>The fair-share scheduling policy details.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the fair-share scheduling policy to categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "quota_share_policy" in value:
        import capo_batch.types.quota_share_policy

        out["quotaSharePolicy"] = capo_batch.types.quota_share_policy.serialize_json(
            value["quota_share_policy"]
        )
    if "fairshare_policy" in value:
        import capo_batch.types.fairshare_policy

        out["fairsharePolicy"] = capo_batch.types.fairshare_policy.serialize_json(
            value["fairshare_policy"]
        )
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SchedulingPolicyDetail:
    out: SchedulingPolicyDetail = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("quotaSharePolicy") is not None:
        import capo_batch.types.quota_share_policy

        out["quota_share_policy"] = (
            capo_batch.types.quota_share_policy.deserialize_json(
                data["quotaSharePolicy"]
            )
        )
    if data.get("fairsharePolicy") is not None:
        import capo_batch.types.fairshare_policy

        out["fairshare_policy"] = capo_batch.types.fairshare_policy.deserialize_json(
            data["fairsharePolicy"]
        )
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
