"""Generated from Smithy shape ``com.amazonaws.fms#PolicyComplianceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.evaluation_results
    import capo_fms.types.issue_info_map
    import capo_fms.types.policy_id
    import capo_fms.types.resource_name
    import capo_fms.types.time_stamp


class PolicyComplianceStatus(TypedDict, closed=True):
    policy_owner: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account that created the Firewall Manager policy.</p>"""
    policy_id: NotRequired["capo_fms.types.policy_id.PolicyId"]
    """<p>The ID of the Firewall Manager policy.</p>"""
    policy_name: NotRequired["capo_fms.types.resource_name.ResourceName"]
    """<p>The name of the Firewall Manager policy.</p>"""
    member_account: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The member account ID.</p>"""
    evaluation_results: NotRequired[
        "capo_fms.types.evaluation_results.EvaluationResults"
    ]
    """<p>An array of <code>EvaluationResult</code> objects.</p>"""
    last_updated: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>Timestamp of the last update to the <code>EvaluationResult</code> objects.</p>"""
    issue_info_map: NotRequired["capo_fms.types.issue_info_map.IssueInfoMap"]
    """<p>Details about problems with dependent services, such as WAF or Config, and the error message received that indicates the problem with the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyComplianceStatus) -> dict:
    out: dict = {}
    if "policy_owner" in value:
        out["PolicyOwner"] = value["policy_owner"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "member_account" in value:
        out["MemberAccount"] = value["member_account"]
    if "evaluation_results" in value:
        import capo_fms.types.evaluation_results

        out["EvaluationResults"] = (
            capo_fms.types.evaluation_results.serialize_aws_json_1_1(
                value["evaluation_results"]
            )
        )
    if "last_updated" in value:
        import capo_fms.types.time_stamp

        out["LastUpdated"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    if "issue_info_map" in value:
        import capo_fms.types.issue_info_map

        out["IssueInfoMap"] = capo_fms.types.issue_info_map.serialize_aws_json_1_1(
            value["issue_info_map"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyComplianceStatus:
    out: PolicyComplianceStatus = {}  # type: ignore[typeddict-item]
    if data.get("PolicyOwner") is not None:
        out["policy_owner"] = data["PolicyOwner"]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("MemberAccount") is not None:
        out["member_account"] = data["MemberAccount"]
    if data.get("EvaluationResults") is not None:
        import capo_fms.types.evaluation_results

        out["evaluation_results"] = (
            capo_fms.types.evaluation_results.deserialize_aws_json_1_1(
                data["EvaluationResults"]
            )
        )
    if data.get("LastUpdated") is not None:
        import capo_fms.types.time_stamp

        out["last_updated"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if data.get("IssueInfoMap") is not None:
        import capo_fms.types.issue_info_map

        out["issue_info_map"] = capo_fms.types.issue_info_map.deserialize_aws_json_1_1(
            data["IssueInfoMap"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyComplianceStatus) -> dict:
    out: dict = {}
    if "policy_owner" in value:
        out["PolicyOwner"] = value["policy_owner"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "member_account" in value:
        out["MemberAccount"] = value["member_account"]
    if "evaluation_results" in value:
        import capo_fms.types.evaluation_results

        out["EvaluationResults"] = capo_fms.types.evaluation_results.serialize_cbor(
            value["evaluation_results"]
        )
    if "last_updated" in value:
        import capo_fms.types.time_stamp

        out["LastUpdated"] = capo_fms.types.time_stamp.serialize_cbor(
            value["last_updated"]
        )
    if "issue_info_map" in value:
        import capo_fms.types.issue_info_map

        out["IssueInfoMap"] = capo_fms.types.issue_info_map.serialize_cbor(
            value["issue_info_map"]
        )
    return out


def deserialize_cbor(data: dict) -> PolicyComplianceStatus:
    out: PolicyComplianceStatus = {}  # type: ignore[typeddict-item]
    if data.get("PolicyOwner") is not None:
        out["policy_owner"] = data["PolicyOwner"]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("MemberAccount") is not None:
        out["member_account"] = data["MemberAccount"]
    if data.get("EvaluationResults") is not None:
        import capo_fms.types.evaluation_results

        out["evaluation_results"] = capo_fms.types.evaluation_results.deserialize_cbor(
            data["EvaluationResults"]
        )
    if data.get("LastUpdated") is not None:
        import capo_fms.types.time_stamp

        out["last_updated"] = capo_fms.types.time_stamp.deserialize_cbor(
            data["LastUpdated"]
        )
    if data.get("IssueInfoMap") is not None:
        import capo_fms.types.issue_info_map

        out["issue_info_map"] = capo_fms.types.issue_info_map.deserialize_cbor(
            data["IssueInfoMap"]
        )
    return out
