"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AddTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string
    import capo_cloudtrail.types.tags_list


class AddTagsRequest(TypedDict, closed=True):
    resource_id: "capo_cloudtrail.types.string.String"
    """<p>Specifies the ARN of the trail, event data store, dashboard, or channel to which one or more tags will be added.</p> <p>The format of a trail ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>The format of an event data store ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>The format of a dashboard ARN is: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>The format of a channel ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>"""
    tags_list: "capo_cloudtrail.types.tags_list.TagsList"
    """<p>Contains a list of tags, up to a limit of 50</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_cloudtrail.types.tags_list

    out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
        value["tags_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsRequest:
    out: AddTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagsList") is not None:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    else:
        out["tags_list"] = []
    return out
