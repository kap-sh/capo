"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentFrameworkResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.framework


class GetAssessmentFrameworkResponse(TypedDict, closed=True):
    framework: NotRequired["capo_auditmanager.types.framework.Framework"]
    """<p> The framework that the <code>GetAssessmentFramework</code> API returned. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentFrameworkResponse) -> dict:
    out: dict = {}
    if "framework" in value:
        import capo_auditmanager.types.framework

        out["framework"] = capo_auditmanager.types.framework.serialize_json(
            value["framework"]
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentFrameworkResponse:
    out: GetAssessmentFrameworkResponse = {}  # type: ignore[typeddict-item]
    if data.get("framework") is not None:
        import capo_auditmanager.types.framework

        out["framework"] = capo_auditmanager.types.framework.deserialize_json(
            data["framework"]
        )
    return out


def redact_sensitive(value: GetAssessmentFrameworkResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "framework" in value:
        import capo_auditmanager.types.framework

        out["framework"] = capo_auditmanager.types.framework.redact_sensitive(
            value["framework"]
        )
    return out
