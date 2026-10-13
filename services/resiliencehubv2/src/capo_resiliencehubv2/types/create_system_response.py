"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateSystemResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system


class CreateSystemResponse(TypedDict, closed=True):
    system: "capo_resiliencehubv2.types.system.System"
    """<p>The created system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSystemResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.system

    out["system"] = capo_resiliencehubv2.types.system.serialize_json(value["system"])
    return out


def deserialize_json(data: dict) -> CreateSystemResponse:
    out: CreateSystemResponse = {}  # type: ignore[typeddict-item]
    if data.get("system") is not None:
        import capo_resiliencehubv2.types.system

        out["system"] = capo_resiliencehubv2.types.system.deserialize_json(
            data["system"]
        )
    else:
        raise DeserializationError("CreateSystemResponse.system required")
    return out


def redact_sensitive(value: CreateSystemResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "system" in value:
        import capo_resiliencehubv2.types.system

        out["system"] = capo_resiliencehubv2.types.system.redact_sensitive(
            value["system"]
        )
    return out
