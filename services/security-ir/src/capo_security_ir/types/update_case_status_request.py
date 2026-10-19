"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.self_managed_case_status


class UpdateCaseStatusRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateCaseStatus to identify the case to update.</p>"""
    case_status: "capo_security_ir.types.self_managed_case_status.SelfManagedCaseStatus"
    """<p>Required element for UpdateCaseStatus to identify the status for a case. Options include <code>Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseStatusRequest) -> dict:
    out: dict = {}
    import capo_security_ir.types.self_managed_case_status

    out["caseStatus"] = capo_security_ir.types.self_managed_case_status.serialize_json(
        value["case_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCaseStatusRequest:
    out: UpdateCaseStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseStatus") is not None:
        import capo_security_ir.types.self_managed_case_status

        out["case_status"] = (
            capo_security_ir.types.self_managed_case_status.deserialize_json(
                data["caseStatus"]
            )
        )
    else:
        import typing

        out["case_status"] = typing.cast(
            "capo_security_ir.types.self_managed_case_status.SelfManagedCaseStatus", ""
        )
    return out
