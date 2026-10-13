"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ranking_data
    import capo_qconnect.types.text_data


class ContentDataDetails(TypedDict, closed=True):
    text_data: "capo_qconnect.types.text_data.TextData"
    """<p>Details about the content text data.</p>"""
    ranking_data: "capo_qconnect.types.ranking_data.RankingData"
    """<p>Details about the content ranking data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentDataDetails) -> dict:
    out: dict = {}
    import capo_qconnect.types.text_data

    out["textData"] = capo_qconnect.types.text_data.serialize_json(value["text_data"])
    import capo_qconnect.types.ranking_data

    out["rankingData"] = capo_qconnect.types.ranking_data.serialize_json(
        value["ranking_data"]
    )
    return out


def deserialize_json(data: dict) -> ContentDataDetails:
    out: ContentDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("textData") is not None:
        import capo_qconnect.types.text_data

        out["text_data"] = capo_qconnect.types.text_data.deserialize_json(
            data["textData"]
        )
    else:
        raise DeserializationError("ContentDataDetails.text_data required")
    if data.get("rankingData") is not None:
        import capo_qconnect.types.ranking_data

        out["ranking_data"] = capo_qconnect.types.ranking_data.deserialize_json(
            data["rankingData"]
        )
    else:
        raise DeserializationError("ContentDataDetails.ranking_data required")
    return out


def redact_sensitive(value: ContentDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_data" in value:
        import capo_qconnect.types.text_data

        out["text_data"] = capo_qconnect.types.text_data.redact_sensitive(
            value["text_data"]
        )
    return out
