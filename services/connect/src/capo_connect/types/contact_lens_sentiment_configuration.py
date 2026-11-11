"""Generated from Smithy shape ``com.amazonaws.connect#ContactLensSentimentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string


class ContactLensSentimentConfiguration(TypedDict, closed=True):
    behavior: NotRequired["capo_connect.types.string.String"]
    """<p>Specifies whether sentiment analysis is enabled for the contact. The default value is <code>Disable</code>. Valid values:</p> <ul> <li> <p> <code>Enable</code> – Sentiment analysis is performed on the contact.</p> </li> <li> <p> <code>Disable</code> – Sentiment analysis is not performed on the contact.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactLensSentimentConfiguration) -> dict:
    out: dict = {}
    if "behavior" in value:
        out["Behavior"] = value["behavior"]
    return out


def deserialize_json(data: dict) -> ContactLensSentimentConfiguration:
    out: ContactLensSentimentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        out["behavior"] = data["Behavior"]
    return out
