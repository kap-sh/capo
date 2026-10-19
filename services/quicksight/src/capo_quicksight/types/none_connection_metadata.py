"""Generated from Smithy shape ``com.amazonaws.quicksight#NoneConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.endpoint


class NoneConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for connections that do not require authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoneConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    return out


def deserialize_json(data: dict) -> NoneConnectionMetadata:
    out: NoneConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    return out
