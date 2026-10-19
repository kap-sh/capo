"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_map_output


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "capo_observabilityadmin.types.tag_map_output.TagMapOutput"
    """<p> The list of tags associated with the telemetry rule resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.tag_map_output

    out["Tags"] = capo_observabilityadmin.types.tag_map_output.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_output

        out["tags"] = capo_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out
