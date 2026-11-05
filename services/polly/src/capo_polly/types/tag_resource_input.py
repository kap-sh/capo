"""Generated from Smithy shape ``com.amazonaws.polly#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.amazon_resource_name
    import capo_polly.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_polly.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the only supported resource is an Amazon Polly lexicon.</p>"""
    tags: "capo_polly.types.tag_map.TagMap"
    """<p>The tags to add to the resource, as key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_polly.types.tag_map

    out["Tags"] = capo_polly.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_polly.types.tag_map

        out["tags"] = capo_polly.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
