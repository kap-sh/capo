"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingForHttpCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.responder_error_masking_action
    import capo_rtbfabric.types.responder_error_masking_logging_types


class ResponderErrorMaskingForHttpCode(TypedDict, closed=True):
    http_code: "str"
    """<p>The HTTP error code.</p>"""
    action: "capo_rtbfabric.types.responder_error_masking_action.ResponderErrorMaskingAction"
    """<p>The action for the error..</p>"""
    logging_types: "capo_rtbfabric.types.responder_error_masking_logging_types.ResponderErrorMaskingLoggingTypes"
    """<p>The error log type.</p>"""
    response_logging_percentage: NotRequired["float"]
    """<p>The percentage of response logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponderErrorMaskingForHttpCode) -> dict:
    out: dict = {}
    out["httpCode"] = value["http_code"]
    import capo_rtbfabric.types.responder_error_masking_action

    out["action"] = capo_rtbfabric.types.responder_error_masking_action.serialize_json(
        value["action"]
    )
    import capo_rtbfabric.types.responder_error_masking_logging_types

    out["loggingTypes"] = (
        capo_rtbfabric.types.responder_error_masking_logging_types.serialize_json(
            value["logging_types"]
        )
    )
    if "response_logging_percentage" in value:
        out["responseLoggingPercentage"] = (
            "NaN"
            if value["response_logging_percentage"]
            != value["response_logging_percentage"]
            else "Infinity"
            if value["response_logging_percentage"] == float("inf")
            else "-Infinity"
            if value["response_logging_percentage"] == float("-inf")
            else value["response_logging_percentage"]
        )
    return out


def deserialize_json(data: dict) -> ResponderErrorMaskingForHttpCode:
    out: ResponderErrorMaskingForHttpCode = {}  # type: ignore[typeddict-item]
    if data.get("httpCode") is not None:
        out["http_code"] = data["httpCode"]
    else:
        out["http_code"] = ""
    if data.get("action") is not None:
        import capo_rtbfabric.types.responder_error_masking_action

        out["action"] = (
            capo_rtbfabric.types.responder_error_masking_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_rtbfabric.types.responder_error_masking_action.ResponderErrorMaskingAction",
            "",
        )
    if data.get("loggingTypes") is not None:
        import capo_rtbfabric.types.responder_error_masking_logging_types

        out["logging_types"] = (
            capo_rtbfabric.types.responder_error_masking_logging_types.deserialize_json(
                data["loggingTypes"]
            )
        )
    else:
        out["logging_types"] = []
    if data.get("responseLoggingPercentage") is not None:
        out["response_logging_percentage"] = float(data["responseLoggingPercentage"])
    return out
