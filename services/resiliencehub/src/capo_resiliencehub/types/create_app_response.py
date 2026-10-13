"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateAppResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app


class CreateAppResponse(TypedDict, closed=True):
    app: "capo_resiliencehub.types.app.App"
    """<p>The created application returned as an object with details including compliance status, creation time, description, resiliency score, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app

    out["app"] = capo_resiliencehub.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> CreateAppResponse:
    out: CreateAppResponse = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        import capo_resiliencehub.types.app

        out["app"] = capo_resiliencehub.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("CreateAppResponse.app required")
    return out


def redact_sensitive(value: CreateAppResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app" in value:
        import capo_resiliencehub.types.app

        out["app"] = capo_resiliencehub.types.app.redact_sensitive(value["app"])
    return out
