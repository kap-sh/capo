"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the resource to be tagged.</p>"""
    tags: "capo_route53globalresolver.types.tags.Tags"
    """<p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_route53globalresolver.types.tags

    out["tags"] = capo_route53globalresolver.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
