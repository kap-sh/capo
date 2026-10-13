"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetProtectedQueryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query


class GetProtectedQueryOutput(TypedDict, closed=True):
    protected_query: "capo_cleanrooms.types.protected_query.ProtectedQuery"
    """<p>The query processing metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProtectedQueryOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_query

    out["protectedQuery"] = capo_cleanrooms.types.protected_query.serialize_json(
        value["protected_query"]
    )
    return out


def deserialize_json(data: dict) -> GetProtectedQueryOutput:
    out: GetProtectedQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("protectedQuery") is not None:
        import capo_cleanrooms.types.protected_query

        out["protected_query"] = capo_cleanrooms.types.protected_query.deserialize_json(
            data["protectedQuery"]
        )
    else:
        raise DeserializationError("GetProtectedQueryOutput.protected_query required")
    return out


def redact_sensitive(value: GetProtectedQueryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protected_query" in value:
        import capo_cleanrooms.types.protected_query

        out["protected_query"] = capo_cleanrooms.types.protected_query.redact_sensitive(
            value["protected_query"]
        )
    return out
