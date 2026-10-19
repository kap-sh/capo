"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.iam_role_arn
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.update_output_list


class UpdateFeedRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>"""
    access_role_arn: NotRequired[
        "capo_elementalinference.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The ARN of an IAM role that Elemental Inference assumes to access resources in your account on your behalf. You can specify the existing role (to leave it unchanged) or a new role. You specify one access role for each feed. </p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed to update.</p>"""
    outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList"
    """<p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFeedRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "access_role_arn" in value:
        out["accessRoleArn"] = value["access_role_arn"]
    import capo_elementalinference.types.update_output_list

    out["outputs"] = capo_elementalinference.types.update_output_list.serialize_json(
        value["outputs"]
    )
    return out


def deserialize_json(data: dict) -> UpdateFeedRequest:
    out: UpdateFeedRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("accessRoleArn") is not None:
        out["access_role_arn"] = data["accessRoleArn"]
    if data.get("outputs") is not None:
        import capo_elementalinference.types.update_output_list

        out["outputs"] = (
            capo_elementalinference.types.update_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        out["outputs"] = []
    return out
