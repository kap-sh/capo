"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.resource_arn
    import capo_iotthingsgraph.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotthingsgraph.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource whose tags are to be removed.</p>"""
    tag_keys: "capo_iotthingsgraph.types.tag_key_list.TagKeyList"
    """<p>A list of tag key names to remove from the resource. You don't specify the value. Both the key and its associated value are removed. </p> <p>This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html#cli-using-param-json">Using JSON for Parameters</a> in the <i>AWS CLI User Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_iotthingsgraph.types.tag_key_list

    out["tagKeys"] = capo_iotthingsgraph.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("tagKeys") is not None:
        import capo_iotthingsgraph.types.tag_key_list

        out["tag_keys"] = (
            capo_iotthingsgraph.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
