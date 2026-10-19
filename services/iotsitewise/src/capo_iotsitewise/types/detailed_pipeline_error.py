"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedPipelineError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_pipeline_error_code


class DetailedPipelineError(TypedDict, closed=True):
    code: (
        "capo_iotsitewise.types.detailed_pipeline_error_code.DetailedPipelineErrorCode"
    )
    """<p>The error code.</p>"""
    message: "str"
    """<p>The associated error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailedPipelineError) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.detailed_pipeline_error_code

    out["code"] = capo_iotsitewise.types.detailed_pipeline_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DetailedPipelineError:
    out: DetailedPipelineError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.detailed_pipeline_error_code

        out["code"] = (
            capo_iotsitewise.types.detailed_pipeline_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_iotsitewise.types.detailed_pipeline_error_code.DetailedPipelineErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
