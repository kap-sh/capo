"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncounterContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.sensitive_markdown_string


class EncounterContext(TypedDict, closed=True):
    unstructured_context: NotRequired[
        "capo_connecthealth.types.sensitive_markdown_string.SensitiveMarkdownString"
    ]
    """<p>Unstructured context information in markdown format</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncounterContext) -> dict:
    out: dict = {}
    if "unstructured_context" in value:
        out["unstructuredContext"] = value["unstructured_context"]
    return out


def deserialize_json(data: dict) -> EncounterContext:
    out: EncounterContext = {}  # type: ignore[typeddict-item]
    if data.get("unstructuredContext") is not None:
        out["unstructured_context"] = data["unstructuredContext"]
    return out


def redact_sensitive(value: EncounterContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "unstructured_context" in value:
        out["unstructured_context"] = "*** Sensitive Data Redacted ***"
    return out
