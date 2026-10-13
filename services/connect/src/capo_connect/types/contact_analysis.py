"""Generated from Smithy shape ``com.amazonaws.connect#ContactAnalysis``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.transcript


class ContactAnalysis(TypedDict, closed=True):
    transcript: NotRequired["capo_connect.types.transcript.Transcript"]
    """<p>Search criteria based on transcript analyzed by Connect Customer Contact Lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactAnalysis) -> dict:
    out: dict = {}
    if "transcript" in value:
        import capo_connect.types.transcript

        out["Transcript"] = capo_connect.types.transcript.serialize_json(
            value["transcript"]
        )
    return out


def deserialize_json(data: dict) -> ContactAnalysis:
    out: ContactAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("Transcript") is not None:
        import capo_connect.types.transcript

        out["transcript"] = capo_connect.types.transcript.deserialize_json(
            data["Transcript"]
        )
    return out


def redact_sensitive(value: ContactAnalysis) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transcript" in value:
        import capo_connect.types.transcript

        out["transcript"] = capo_connect.types.transcript.redact_sensitive(
            value["transcript"]
        )
    return out
