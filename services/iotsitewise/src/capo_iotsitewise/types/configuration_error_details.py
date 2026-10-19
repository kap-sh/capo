"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_code
    import capo_iotsitewise.types.error_message


class ConfigurationErrorDetails(TypedDict, closed=True):
    code: "capo_iotsitewise.types.error_code.ErrorCode"
    """<p>The error code.</p>"""
    message: "capo_iotsitewise.types.error_message.ErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationErrorDetails) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.error_code

    out["code"] = capo_iotsitewise.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConfigurationErrorDetails:
    out: ConfigurationErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.error_code

        out["code"] = capo_iotsitewise.types.error_code.deserialize_json(data["code"])
    else:
        import typing

        out["code"] = typing.cast("capo_iotsitewise.types.error_code.ErrorCode", "")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
