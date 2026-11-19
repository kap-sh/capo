"""Generated from Smithy shape ``com.amazonaws.connectcases#GetMergeCasesStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id


class GetMergeCasesStatusRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>The unique identifier of the case. This can be the primary case or the secondary case of a merge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMergeCasesStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMergeCasesStatusRequest:
    out: GetMergeCasesStatusRequest = {}  # type: ignore[typeddict-item]
    return out
