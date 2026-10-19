"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeDataDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary_list
    import capo_qconnect.types.ranking_data
    import capo_qconnect.types.sensitive_string


class GenerativeDataDetails(TypedDict, closed=True):
    completion: "capo_qconnect.types.sensitive_string.SensitiveString"
    """<p>The LLM response.</p>"""
    references: "capo_qconnect.types.data_summary_list.DataSummaryList"
    """<p>The references used to generative the LLM response.</p>"""
    ranking_data: "capo_qconnect.types.ranking_data.RankingData"
    """<p>Details about the generative content ranking data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeDataDetails) -> dict:
    out: dict = {}
    out["completion"] = value["completion"]
    import capo_qconnect.types.data_summary_list

    out["references"] = capo_qconnect.types.data_summary_list.serialize_json(
        value["references"]
    )
    import capo_qconnect.types.ranking_data

    out["rankingData"] = capo_qconnect.types.ranking_data.serialize_json(
        value["ranking_data"]
    )
    return out


def deserialize_json(data: dict) -> GenerativeDataDetails:
    out: GenerativeDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("completion") is not None:
        out["completion"] = data["completion"]
    else:
        out["completion"] = ""
    if data.get("references") is not None:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.deserialize_json(
            data["references"]
        )
    else:
        out["references"] = []
    if data.get("rankingData") is not None:
        import capo_qconnect.types.ranking_data

        out["ranking_data"] = capo_qconnect.types.ranking_data.deserialize_json(
            data["rankingData"]
        )
    else:
        raise DeserializationError("GenerativeDataDetails.ranking_data required")
    return out


def redact_sensitive(value: GenerativeDataDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "completion" in value:
        out["completion"] = "*** Sensitive Data Redacted ***"
    if "references" in value:
        import capo_qconnect.types.data_summary_list

        out["references"] = capo_qconnect.types.data_summary_list.redact_sensitive(
            value["references"]
        )
    return out
