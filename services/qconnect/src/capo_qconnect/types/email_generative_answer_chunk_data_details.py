"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailGenerativeAnswerChunkDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary_list
    import capo_qconnect.types.next_token
    import capo_qconnect.types.non_empty_sensitive_string


class EmailGenerativeAnswerChunkDataDetails(TypedDict, closed=True):
    completion: NotRequired[
        "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The partial or complete text content of the generative answer response.</p>"""
    references: NotRequired["capo_qconnect.types.data_summary_list.DataSummaryList"]
    """<p>Source references and citations from knowledge base articles used to generate the answer.</p>"""
    next_chunk_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>Token for retrieving the next chunk of streaming response data, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailGenerativeAnswerChunkDataDetails) -> dict:
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


def deserialize_json(data: dict) -> EmailGenerativeAnswerChunkDataDetails:
    out: EmailGenerativeAnswerChunkDataDetails = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: EmailGenerativeAnswerChunkDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Sensitive Data Redacted ***"
    if "references" in value:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.redact_sensitive(
            value["references"]
        )
    return out
