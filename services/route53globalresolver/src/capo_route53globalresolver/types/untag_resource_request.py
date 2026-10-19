"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_route53globalresolver.types.tag_keys.TagKeys"
    """<p>The tag keys associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_route53globalresolver.types.tag_keys

    out["tagKeys"] = capo_route53globalresolver.types.tag_keys.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_route53globalresolver.types.tag_keys

        out["tag_keys"] = capo_route53globalresolver.types.tag_keys.deserialize_json(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
