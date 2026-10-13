"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeChunkDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary_list
    import capo_qconnect.types.next_token
    import capo_qconnect.types.sensitive_string


class GenerativeChunkDataDetails(TypedDict, closed=True):
    completion: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>A chunk of the LLM response.</p>"""
    references: NotRequired["capo_qconnect.types.data_summary_list.DataSummaryList"]
    """<p>The references used to generate the LLM response.</p>"""
    next_chunk_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeChunkDataDetails) -> dict:
    out: dict = {}
    if "completion" in value:
        out["completion"] = value["completion"]
    if "references" in value:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.serialize_json(
            value["references"]
        )
    if "next_chunk_token" in value:
        out["nextChunkToken"] = value["next_chunk_token"]
    return out


def deserialize_json(data: dict) -> GenerativeChunkDataDetails:
    out: GenerativeChunkDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("completion") is not None:
        out["completion"] = data["completion"]
    if data.get("references") is not None:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.deserialize_json(
            data["references"]
        )
    if data.get("nextChunkToken") is not None:
        out["next_chunk_token"] = data["nextChunkToken"]
    return out


def redact_sensitive(value: GenerativeChunkDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Sensitive Data Redacted ***"
    if "references" in value:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.redact_sensitive(
            value["references"]
        )
    return out
