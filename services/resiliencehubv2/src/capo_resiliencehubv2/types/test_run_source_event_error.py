"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEventError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_source_event_error_code


class TestRunSourceEventError(TypedDict, closed=True):
    error_code: "capo_resiliencehubv2.types.test_run_source_event_error_code.TestRunSourceEventErrorCode"
    """<p>The error code.</p>"""
    error_message: "str"
    """<p>A human-readable description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEventError) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run_source_event_error_code

    out["errorCode"] = (
        capo_resiliencehubv2.types.test_run_source_event_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> TestRunSourceEventError:
    out: TestRunSourceEventError = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_resiliencehubv2.types.test_run_source_event_error_code

        out["error_code"] = (
            capo_resiliencehubv2.types.test_run_source_event_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_resiliencehubv2.types.test_run_source_event_error_code.TestRunSourceEventErrorCode",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
