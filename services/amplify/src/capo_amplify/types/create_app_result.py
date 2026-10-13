"""Generated from Smithy shape ``com.amazonaws.amplify#CreateAppResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.app


class CreateAppResult(TypedDict, closed=True):
    app: "capo_amplify.types.app.App"


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppResult) -> dict:
    out: dict = {}
    import capo_amplify.types.app

    out["app"] = capo_amplify.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> CreateAppResult:
    out: CreateAppResult = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        import capo_amplify.types.app

        out["app"] = capo_amplify.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("CreateAppResult.app required")
    return out


def redact_sensitive(value: CreateAppResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app" in value:
        import capo_amplify.types.app

        out["app"] = capo_amplify.types.app.redact_sensitive(value["app"])
    return out
