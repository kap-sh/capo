"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentContextResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.context_summary


class CreateAgentContextResponse(TypedDict, closed=True):
    context: "capo_wellarchitected.types.context_summary.ContextSummary"
    """<p>The created context summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentContextResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.context_summary

    out["context"] = capo_wellarchitected.types.context_summary.serialize_json(
        value["context"]
    )
    return out


def deserialize_json(data: dict) -> CreateAgentContextResponse:
    out: CreateAgentContextResponse = {}  # type: ignore[typeddict-item]
    if data.get("context") is not None:
        import capo_wellarchitected.types.context_summary

        out["context"] = capo_wellarchitected.types.context_summary.deserialize_json(
            data["context"]
        )
    else:
        raise DeserializationError("CreateAgentContextResponse.context required")
    return out


def redact_sensitive(value: CreateAgentContextResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "context" in value:
        import capo_wellarchitected.types.context_summary

        out["context"] = capo_wellarchitected.types.context_summary.redact_sensitive(
            value["context"]
        )
    return out
