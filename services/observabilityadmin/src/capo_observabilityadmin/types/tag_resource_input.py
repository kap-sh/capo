"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.tag_map_input


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the telemetry rule resource to tag. </p>"""
    tags: "capo_observabilityadmin.types.tag_map_input.TagMapInput"
    """<p> The key-value pairs to add or update for the telemetry rule resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_observabilityadmin.types.tag_map_input

    out["Tags"] = capo_observabilityadmin.types.tag_map_input.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["tags"] = capo_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out
