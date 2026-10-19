"""Generated from Smithy shape ``com.amazonaws.appflow#MarketoDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.object


class MarketoDestinationProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p>The object specified in the Marketo flow destination.</p>"""
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MarketoDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "error_handling_config" in value:
        import capo_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            capo_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> MarketoDestinationProperties:
    out: MarketoDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    if data.get("errorHandlingConfig") is not None:
        import capo_appflow.types.error_handling_config

        out["error_handling_config"] = (
            capo_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    return out
