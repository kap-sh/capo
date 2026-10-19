"""Generated from Smithy shape ``com.amazonaws.elementalinference#AssociateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.associated_resource_name
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.feed_id


class AssociateFeedRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""
    associated_resource_name: (
        "capo_elementalinference.types.associated_resource_name.AssociatedResourceName"
    )
    """<p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>"""
    outputs: "capo_elementalinference.types.create_output_list.CreateOutputList"
    """<p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>"""
    dry_run: NotRequired["bool"]
    """<p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateFeedRequest) -> dict:
    out: dict = {}
    out["associatedResourceName"] = value["associated_resource_name"]
    import capo_elementalinference.types.create_output_list

    out["outputs"] = capo_elementalinference.types.create_output_list.serialize_json(
        value["outputs"]
    )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> AssociateFeedRequest:
    out: AssociateFeedRequest = {}  # type: ignore[typeddict-item]
    if data.get("associatedResourceName") is not None:
        out["associated_resource_name"] = data["associatedResourceName"]
    else:
        out["associated_resource_name"] = ""
    if data.get("outputs") is not None:
        import capo_elementalinference.types.create_output_list

        out["outputs"] = (
            capo_elementalinference.types.create_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        out["outputs"] = []
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
