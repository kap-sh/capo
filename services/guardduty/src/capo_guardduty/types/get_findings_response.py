"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFindingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.findings


class GetFindingsResponse(TypedDict, closed=True):
    findings: NotRequired["capo_guardduty.types.findings.Findings"]
    """<p>A list of findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsResponse) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_guardduty.types.findings

        out["findings"] = capo_guardduty.types.findings.serialize_json(
            value["findings"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsResponse:
    out: GetFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_guardduty.types.findings

        out["findings"] = capo_guardduty.types.findings.deserialize_json(
            data["findings"]
        )
    return out


def redact_sensitive(value: GetFindingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "findings" in value:
        import capo_guardduty.types.findings

        out["findings"] = capo_guardduty.types.findings.redact_sensitive(
            value["findings"]
        )
    return out
