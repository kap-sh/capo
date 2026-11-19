"""Generated from Smithy shape ``com.amazonaws.fms#GetViolationDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.violation_detail


class GetViolationDetailsResponse(TypedDict, closed=True):
    violation_detail: NotRequired["capo_fms.types.violation_detail.ViolationDetail"]
    """<p>Violation detail for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetViolationDetailsResponse) -> dict:
    out: dict = {}
    if "violation_detail" in value:
        import capo_fms.types.violation_detail

        out["ViolationDetail"] = capo_fms.types.violation_detail.serialize_aws_json_1_1(
            value["violation_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetViolationDetailsResponse:
    out: GetViolationDetailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ViolationDetail") is not None:
        import capo_fms.types.violation_detail

        out["violation_detail"] = (
            capo_fms.types.violation_detail.deserialize_aws_json_1_1(
                data["ViolationDetail"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetViolationDetailsResponse) -> dict:
    out: dict = {}
    if "violation_detail" in value:
        import capo_fms.types.violation_detail

        out["ViolationDetail"] = capo_fms.types.violation_detail.serialize_cbor(
            value["violation_detail"]
        )
    return out


def deserialize_cbor(data: dict) -> GetViolationDetailsResponse:
    out: GetViolationDetailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ViolationDetail") is not None:
        import capo_fms.types.violation_detail

        out["violation_detail"] = capo_fms.types.violation_detail.deserialize_cbor(
            data["ViolationDetail"]
        )
    return out
