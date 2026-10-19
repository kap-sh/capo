"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceErrorMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_error_type


class DataSourceErrorMessage(TypedDict, closed=True):
    error_type: "capo_datazone.types.data_source_error_type.DataSourceErrorType"
    """<p>The type of the error message that is returned if the operation cannot be successfully completed.</p>"""
    error_detail: NotRequired["str"]
    """<p>The details of the error message that is returned if the operation cannot be successfully completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceErrorMessage) -> dict:
    out: dict = {}
    import capo_datazone.types.data_source_error_type

    out["errorType"] = capo_datazone.types.data_source_error_type.serialize_json(
        value["error_type"]
    )
    if "error_detail" in value:
        out["errorDetail"] = value["error_detail"]
    return out


def deserialize_json(data: dict) -> DataSourceErrorMessage:
    out: DataSourceErrorMessage = {}  # type: ignore[typeddict-item]
    if data.get("errorType") is not None:
        import capo_datazone.types.data_source_error_type

        out["error_type"] = capo_datazone.types.data_source_error_type.deserialize_json(
            data["errorType"]
        )
    else:
        import typing

        out["error_type"] = typing.cast(
            "capo_datazone.types.data_source_error_type.DataSourceErrorType", ""
        )
    if data.get("errorDetail") is not None:
        out["error_detail"] = data["errorDetail"]
    return out
