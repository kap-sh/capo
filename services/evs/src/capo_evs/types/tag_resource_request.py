"""Generated from Smithy shape ``com.amazonaws.evs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.arn
    import capo_evs.types.request_tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_evs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "capo_evs.types.request_tag_map.RequestTagMap"
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other environment or Amazon Web Services resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_evs.types.request_tag_map

    out["tags"] = capo_evs.types.request_tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_evs.types.request_tag_map

        out["tags"] = capo_evs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
