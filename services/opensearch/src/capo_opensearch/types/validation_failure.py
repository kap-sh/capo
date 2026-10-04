"""Generated from Smithy shape ``com.amazonaws.opensearch#ValidationFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string
    import capo_opensearch.types.validation_failure_severity


class ValidationFailure(TypedDict, closed=True):
    code: NotRequired["capo_opensearch.types.string.String"]
    """<p>The error code of the failure.</p>"""
    message: NotRequired["capo_opensearch.types.string.String"]
    """<p>A message corresponding to the failure.</p>"""
    severity: NotRequired[
        "capo_opensearch.types.validation_failure_severity.ValidationFailureSeverity"
    ]
    """<p>The severity of the validation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationFailure) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "severity" in value:
        import capo_opensearch.types.validation_failure_severity

        out["Severity"] = (
            capo_opensearch.types.validation_failure_severity.serialize_json(
                value["severity"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationFailure:
    out: ValidationFailure = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Severity") is not None:
        import capo_opensearch.types.validation_failure_severity

        out["severity"] = (
            capo_opensearch.types.validation_failure_severity.deserialize_json(
                data["Severity"]
            )
        )
    return out
