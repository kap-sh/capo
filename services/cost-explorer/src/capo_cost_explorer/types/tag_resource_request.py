"""Generated from Smithy shape ``com.amazonaws.costexplorer#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.resource_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html">ResourceTag</a>. </p>"""
    resource_tags: "capo_cost_explorer.types.resource_tag_list.ResourceTagList"
    """<p> A list of tag key-value pairs to be added to the resource.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cost_explorer.types.resource_tag_list

    out["ResourceTags"] = (
        capo_cost_explorer.types.resource_tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("ResourceTags") is not None:
        import capo_cost_explorer.types.resource_tag_list

        out["resource_tags"] = (
            capo_cost_explorer.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.resource_tags required")
    return out
