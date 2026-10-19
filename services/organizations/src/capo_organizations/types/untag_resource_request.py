"""Generated from Smithy shape ``com.amazonaws.organizations#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.tag_keys
    import capo_organizations.types.taggable_resource_id


class UntagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_organizations.types.taggable_resource_id.TaggableResourceId"
    """<p>The ID of the resource to remove a tag from.</p> <p>You can specify any of the following taggable resources.</p> <ul> <li> <p>Amazon Web Services account – specify the account ID number.</p> </li> <li> <p>Organizational unit – specify the OU ID that begins with <code>ou-</code> and looks similar to: <code>ou-<i>1a2b-34uvwxyz</i> </code> </p> </li> <li> <p>Root – specify the root ID that begins with <code>r-</code> and looks similar to: <code>r-<i>1a2b</i> </code> </p> </li> <li> <p>Policy – specify the policy ID that begins with <code>p-</code> andlooks similar to: <code>p-<i>12abcdefg3</i> </code> </p> </li> </ul>"""
    tag_keys: "capo_organizations.types.tag_keys.TagKeys"
    """<p>The list of keys for tags to remove from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_organizations.types.tag_keys

    out["TagKeys"] = capo_organizations.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagKeys") is not None:
        import capo_organizations.types.tag_keys

        out["tag_keys"] = capo_organizations.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
