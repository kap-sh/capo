"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateResolverTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.case_status
    import capo_security_ir.types.resolver_type


class UpdateResolverTypeResponse(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Response element for UpdateResolver identifying the case ID being updated.</p>"""
    case_status: NotRequired["capo_security_ir.types.case_status.CaseStatus"]
    """<p>Response element for UpdateResolver identifying the current status of the case.</p>"""
    resolver_type: NotRequired["capo_security_ir.types.resolver_type.ResolverType"]
    """<p>Response element for UpdateResolver identifying the current resolver of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResolverTypeResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "case_status" in value:
        import capo_security_ir.types.case_status

        out["caseStatus"] = capo_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "resolver_type" in value:
        import capo_security_ir.types.resolver_type

        out["resolverType"] = capo_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResolverTypeResponse:
    out: UpdateResolverTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    if data.get("caseStatus") is not None:
        import capo_security_ir.types.case_status

        out["case_status"] = capo_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if data.get("resolverType") is not None:
        import capo_security_ir.types.resolver_type

        out["resolver_type"] = capo_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    return out
