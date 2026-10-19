"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_error_code
    import capo_iotsitewise.types.detailed_error_message


class DetailedError(TypedDict, closed=True):
    code: "capo_iotsitewise.types.detailed_error_code.DetailedErrorCode"
    """<p>The error code. </p>"""
    message: "capo_iotsitewise.types.detailed_error_message.DetailedErrorMessage"
    """<p>The error message. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailedError) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.detailed_error_code

    out["code"] = capo_iotsitewise.types.detailed_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DetailedError:
    out: DetailedError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.detailed_error_code

        out["code"] = capo_iotsitewise.types.detailed_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_iotsitewise.types.detailed_error_code.DetailedErrorCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
