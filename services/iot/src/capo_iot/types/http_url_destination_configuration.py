"""Generated from Smithy shape ``com.amazonaws.iot#HttpUrlDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.url


class HttpUrlDestinationConfiguration(TypedDict, closed=True):
    confirmation_url: "capo_iot.types.url.Url"
    """<p>The URL IoT uses to confirm ownership of or access to the topic rule destination URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpUrlDestinationConfiguration) -> dict:
    out: dict = {}
    out["confirmationUrl"] = value["confirmation_url"]
    return out


def deserialize_json(data: dict) -> HttpUrlDestinationConfiguration:
    out: HttpUrlDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("confirmationUrl") is not None:
        out["confirmation_url"] = data["confirmationUrl"]
    else:
        out["confirmation_url"] = ""
    return out
