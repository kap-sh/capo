"""Generated from Smithy shape ``com.amazonaws.oam#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_oam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_oam.types.arn
    import capo_oam.types.tag_map_input


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_oam.types.arn.Arn"
    """<p>The ARN of the resource that you're adding tags to.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>"""
    tags: "capo_oam.types.tag_map_input.TagMapInput"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_oam.types.tag_map_input

    out["Tags"] = capo_oam.types.tag_map_input.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_oam.types.tag_map_input

        out["tags"] = capo_oam.types.tag_map_input.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
