"""Generated from Smithy shape ``com.amazonaws.organizations#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.taggable_resource_id
    import capo_organizations.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_organizations.types.taggable_resource_id.TaggableResourceId"
    """<p>The ID of the resource to add a tag to.</p> <p>You can specify any of the following taggable resources.</p> <ul> <li> <p>Amazon Web Services account – specify the account ID number.</p> </li> <li> <p>Organizational unit – specify the OU ID that begins with <code>ou-</code> and looks similar to: <code>ou-<i>1a2b-34uvwxyz</i> </code> </p> </li> <li> <p>Root – specify the root ID that begins with <code>r-</code> and looks similar to: <code>r-<i>1a2b</i> </code> </p> </li> <li> <p>Policy – specify the policy ID that begins with <code>p-</code> andlooks similar to: <code>p-<i>12abcdefg3</i> </code> </p> </li> </ul>"""
    tags: "capo_organizations.types.tags.Tags"
    """<p>A list of tags to add to the specified resource.</p> <p>For each tag in the list, you must specify both a tag key and a value. The value can be an empty string, but you can't set it to <code>null</code>.</p> <note> <p>If any one of the tags is not valid or if you exceed the maximum allowed number of tags for a resource, then the entire request fails.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_organizations.types.tags

    out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
