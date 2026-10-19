"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_arn
    import capo_elementalinference.types.feed_association
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_status
    import capo_elementalinference.types.get_output_list
    import capo_elementalinference.types.iam_role_arn
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.string_list
    import capo_elementalinference.types.tag_map


class GetFeedResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the feed.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the feed.</p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""
    data_endpoints: "capo_elementalinference.types.string_list.StringList"
    """<p>The dataEndpoints of the feed.</p>"""
    outputs: "capo_elementalinference.types.get_output_list.GetOutputList"
    """<p>An array of the outputs in the feed.</p>"""
    access_role_arn: NotRequired[
        "capo_elementalinference.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that Elemental Inference assumes. Elemental Inference uses this role to access resources in your account on your behalf. This property is absent if the feed doesn't have an IAM role. </p>"""
    status: "capo_elementalinference.types.feed_status.FeedStatus"
    """<p>The status of the feed.</p>"""
    association: NotRequired[
        "capo_elementalinference.types.feed_association.FeedAssociation"
    ]
    """<p>Information about the resource that is associated with the feed. It's possible that there is no associated resource. This is not an error. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>A list of the tags, if any, for the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    import capo_elementalinference.types.string_list

    out["dataEndpoints"] = capo_elementalinference.types.string_list.serialize_json(
        value["data_endpoints"]
    )
    import capo_elementalinference.types.get_output_list

    out["outputs"] = capo_elementalinference.types.get_output_list.serialize_json(
        value["outputs"]
    )
    if "access_role_arn" in value:
        out["accessRoleArn"] = value["access_role_arn"]
    import capo_elementalinference.types.feed_status

    out["status"] = capo_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    if "association" in value:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.serialize_json(
                value["association"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetFeedResponse:
    out: GetFeedResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("dataEndpoints") is not None:
        import capo_elementalinference.types.string_list

        out["data_endpoints"] = (
            capo_elementalinference.types.string_list.deserialize_json(
                data["dataEndpoints"]
            )
        )
    else:
        out["data_endpoints"] = []
    if data.get("outputs") is not None:
        import capo_elementalinference.types.get_output_list

        out["outputs"] = capo_elementalinference.types.get_output_list.deserialize_json(
            data["outputs"]
        )
    else:
        out["outputs"] = []
    if data.get("accessRoleArn") is not None:
        out["access_role_arn"] = data["accessRoleArn"]
    if data.get("status") is not None:
        import capo_elementalinference.types.feed_status

        out["status"] = capo_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.feed_status.FeedStatus", ""
        )
    if data.get("association") is not None:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.deserialize_json(
                data["association"]
            )
        )
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
