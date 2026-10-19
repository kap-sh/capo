"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class HttpConfiguration(TypedDict, closed=True):
    base_url: "capo_mediatailor.types.__string.__string"
    """<p>The base URL for the source location host server. This string must include the protocol, such as <b>https://</b>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpConfiguration) -> dict:
    out: dict = {}
    out["BaseUrl"] = value["base_url"]
    return out


def deserialize_json(data: dict) -> HttpConfiguration:
    out: HttpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BaseUrl") is not None:
        out["base_url"] = data["BaseUrl"]
    else:
        out["base_url"] = ""
    return out
