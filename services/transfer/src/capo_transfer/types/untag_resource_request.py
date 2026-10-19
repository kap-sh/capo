"""Generated from Smithy shape ``com.amazonaws.transfer#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>"""
    tag_keys: "capo_transfer.types.tag_keys.TagKeys"
    """<p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_transfer.types.tag_keys

    out["TagKeys"] = capo_transfer.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_transfer.types.tag_keys

        out["tag_keys"] = capo_transfer.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
