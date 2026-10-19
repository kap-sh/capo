"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#BatchGetFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.batch_get_findings_errors
    import capo_codeguru_security.types.findings


class BatchGetFindingsResponse(TypedDict, closed=True):
    findings: "capo_codeguru_security.types.findings.Findings"
    """<p> A list of all findings which were successfully fetched.</p>"""
    failed_findings: (
        "capo_codeguru_security.types.batch_get_findings_errors.BatchGetFindingsErrors"
    )
    """<p>A list of errors for individual findings which were not fetched. Each BatchGetFindingsError contains the <code>scanName</code>, <code>findingId</code>, <code>errorCode</code> and error <code>message</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsResponse) -> dict:
    out: dict = {}
    import capo_codeguru_security.types.findings

    out["findings"] = capo_codeguru_security.types.findings.serialize_json(
        value["findings"]
    )
    import capo_codeguru_security.types.batch_get_findings_errors

    out["failedFindings"] = (
        capo_codeguru_security.types.batch_get_findings_errors.serialize_json(
            value["failed_findings"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFindingsResponse:
    out: BatchGetFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findings") is not None:
        import capo_codeguru_security.types.findings

        out["findings"] = capo_codeguru_security.types.findings.deserialize_json(
            data["findings"]
        )
    else:
        out["findings"] = []
    if data.get("failedFindings") is not None:
        import capo_codeguru_security.types.batch_get_findings_errors

        out["failed_findings"] = (
            capo_codeguru_security.types.batch_get_findings_errors.deserialize_json(
                data["failedFindings"]
            )
        )
    else:
        out["failed_findings"] = []
    return out
