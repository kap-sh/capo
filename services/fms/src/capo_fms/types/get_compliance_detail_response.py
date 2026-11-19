"""Generated from Smithy shape ``com.amazonaws.fms#GetComplianceDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.policy_compliance_detail


class GetComplianceDetailResponse(TypedDict, closed=True):
    policy_compliance_detail: NotRequired[
        "capo_fms.types.policy_compliance_detail.PolicyComplianceDetail"
    ]
    """<p>Information about the resources and the policy that you specified in the <code>GetComplianceDetail</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailResponse) -> dict:
    out: dict = {}
    if "policy_compliance_detail" in value:
        import capo_fms.types.policy_compliance_detail

        out["PolicyComplianceDetail"] = (
            capo_fms.types.policy_compliance_detail.serialize_aws_json_1_1(
                value["policy_compliance_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailResponse:
    out: GetComplianceDetailResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyComplianceDetail") is not None:
        import capo_fms.types.policy_compliance_detail

        out["policy_compliance_detail"] = (
            capo_fms.types.policy_compliance_detail.deserialize_aws_json_1_1(
                data["PolicyComplianceDetail"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetComplianceDetailResponse) -> dict:
    out: dict = {}
    if "policy_compliance_detail" in value:
        import capo_fms.types.policy_compliance_detail

        out["PolicyComplianceDetail"] = (
            capo_fms.types.policy_compliance_detail.serialize_cbor(
                value["policy_compliance_detail"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetComplianceDetailResponse:
    out: GetComplianceDetailResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyComplianceDetail") is not None:
        import capo_fms.types.policy_compliance_detail

        out["policy_compliance_detail"] = (
            capo_fms.types.policy_compliance_detail.deserialize_cbor(
                data["PolicyComplianceDetail"]
            )
        )
    return out
