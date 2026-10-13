"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetSystemResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system


class GetSystemResponse(TypedDict, closed=True):
    system: "capo_resiliencehubv2.types.system.System"
    """<p>The requested system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSystemResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.system

    out["system"] = capo_resiliencehubv2.types.system.serialize_json(value["system"])
    return out


def deserialize_json(data: dict) -> GetSystemResponse:
    out: GetSystemResponse = {}  # type: ignore[typeddict-item]
    if data.get("system") is not None:
        import capo_resiliencehubv2.types.system

        out["system"] = capo_resiliencehubv2.types.system.deserialize_json(
            data["system"]
        )
    else:
        raise DeserializationError("GetSystemResponse.system required")
    return out


def redact_sensitive(value: GetSystemResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "system" in value:
        import capo_resiliencehubv2.types.system

        out["system"] = capo_resiliencehubv2.types.system.redact_sensitive(
            value["system"]
        )
    return out
