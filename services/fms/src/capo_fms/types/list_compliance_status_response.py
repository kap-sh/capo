"""Generated from Smithy shape ``com.amazonaws.fms#ListComplianceStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_token
    import capo_fms.types.policy_compliance_status_list


class ListComplianceStatusResponse(TypedDict, closed=True):
    policy_compliance_status_list: NotRequired[
        "capo_fms.types.policy_compliance_status_list.PolicyComplianceStatusList"
    ]
    """<p>An array of <code>PolicyComplianceStatus</code> objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you have more <code>PolicyComplianceStatus</code> objects than the number that you specified for <code>MaxResults</code> in the request, the response includes a <code>NextToken</code> value. To list more <code>PolicyComplianceStatus</code> objects, submit another <code>ListComplianceStatus</code> request, and specify the <code>NextToken</code> value from the response in the <code>NextToken</code> value in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComplianceStatusResponse) -> dict:
    out: dict = {}
    if "policy_compliance_status_list" in value:
        import capo_fms.types.policy_compliance_status_list

        out["PolicyComplianceStatusList"] = (
            capo_fms.types.policy_compliance_status_list.serialize_aws_json_1_1(
                value["policy_compliance_status_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComplianceStatusResponse:
    out: ListComplianceStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyComplianceStatusList") is not None:
        import capo_fms.types.policy_compliance_status_list

        out["policy_compliance_status_list"] = (
            capo_fms.types.policy_compliance_status_list.deserialize_aws_json_1_1(
                data["PolicyComplianceStatusList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListComplianceStatusResponse) -> dict:
    out: dict = {}
    if "policy_compliance_status_list" in value:
        import capo_fms.types.policy_compliance_status_list

        out["PolicyComplianceStatusList"] = (
            capo_fms.types.policy_compliance_status_list.serialize_cbor(
                value["policy_compliance_status_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListComplianceStatusResponse:
    out: ListComplianceStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyComplianceStatusList") is not None:
        import capo_fms.types.policy_compliance_status_list

        out["policy_compliance_status_list"] = (
            capo_fms.types.policy_compliance_status_list.deserialize_cbor(
                data["PolicyComplianceStatusList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
