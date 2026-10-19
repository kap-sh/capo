"""Generated from Smithy shape ``com.amazonaws.transfer#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.tags


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>An Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a server, user, or role.</p>"""
    tags: "capo_transfer.types.tags.Tags"
    """<p>Key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (servers, users, workflows, and so on) for any purpose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_transfer.types.tags

    out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out
