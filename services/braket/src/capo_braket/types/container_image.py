"""Generated from Smithy shape ``com.amazonaws.braket#ContainerImage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.uri


class ContainerImage(TypedDict, closed=True):
    uri: "capo_braket.types.uri.Uri"
    """<p>The URI locating the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerImage) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> ContainerImage:
    out: ContainerImage = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
