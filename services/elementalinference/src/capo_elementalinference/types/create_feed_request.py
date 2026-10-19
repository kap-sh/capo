"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.iam_role_arn
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class CreateFeedRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this feed.</p>"""
    access_role_arn: NotRequired[
        "capo_elementalinference.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. For example, the smart crop feature uses this role to read graphics-compositing templates from your Amazon S3 bucket. You specify one access role for each feed. </p>"""
    outputs: "capo_elementalinference.types.create_output_list.CreateOutputList"
    """<p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags. You can also add tags later, using TagResource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFeedRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "access_role_arn" in value:
        out["accessRoleArn"] = value["access_role_arn"]
    import capo_elementalinference.types.create_output_list

    out["outputs"] = capo_elementalinference.types.create_output_list.serialize_json(
        value["outputs"]
    )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFeedRequest:
    out: CreateFeedRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("accessRoleArn") is not None:
        out["access_role_arn"] = data["accessRoleArn"]
    if data.get("outputs") is not None:
        import capo_elementalinference.types.create_output_list

        out["outputs"] = (
            capo_elementalinference.types.create_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        out["outputs"] = []
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
