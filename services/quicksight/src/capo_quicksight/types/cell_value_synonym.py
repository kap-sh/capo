"""Generated from Smithy shape ``com.amazonaws.quicksight#CellValueSynonym``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_string_list
    import capo_quicksight.types.synonym_string


class CellValueSynonym(TypedDict, closed=True):
    cell_value: NotRequired["capo_quicksight.types.synonym_string.SynonymString"]
    """<p>The cell value.</p>"""
    synonyms: NotRequired[
        "capo_quicksight.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>Other names or aliases for the cell value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CellValueSynonym) -> dict:
    out: dict = {}
    if "cell_value" in value:
        out["CellValue"] = value["cell_value"]
    if "synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["Synonyms"] = capo_quicksight.types.sensitive_string_list.serialize_json(
            value["synonyms"]
        )
    return out


def deserialize_json(data: dict) -> CellValueSynonym:
    out: CellValueSynonym = {}  # type: ignore[typeddict-item]
    if data.get("CellValue") is not None:
        out["cell_value"] = data["CellValue"]
    if data.get("Synonyms") is not None:
        import capo_quicksight.types.sensitive_string_list

        out["synonyms"] = capo_quicksight.types.sensitive_string_list.deserialize_json(
            data["Synonyms"]
        )
    return out


def redact_sensitive(value: CellValueSynonym) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cell_value" in value:
        out["cell_value"] = "*** Sensitive Data Redacted ***"
    if "synonyms" in value:
        import capo_quicksight.types.sensitive_string_list

        out["synonyms"] = capo_quicksight.types.sensitive_string_list.redact_sensitive(
            value["synonyms"]
        )
    return out
