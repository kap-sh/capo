"""Generated from Smithy shape ``com.amazonaws.fms#ViolationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.length_bounded_string
    import capo_fms.types.policy_id
    import capo_fms.types.resource_id
    import capo_fms.types.resource_type
    import capo_fms.types.resource_violations
    import capo_fms.types.tag_list


class ViolationDetail(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the Firewall Manager policy that the violation details were requested for.</p>"""
    member_account: "capo_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account that the violation details were requested for.</p>"""
    resource_id: "capo_fms.types.resource_id.ResourceId"
    """<p>The resource ID that the violation details were requested for.</p>"""
    resource_type: "capo_fms.types.resource_type.ResourceType"
    """<p>The resource type that the violation details were requested for.</p>"""
    resource_violations: "capo_fms.types.resource_violations.ResourceViolations"
    """<p>List of violations for the requested resource.</p>"""
    resource_tags: NotRequired["capo_fms.types.tag_list.TagList"]
    """<p>The <code>ResourceTag</code> objects associated with the resource.</p>"""
    resource_description: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Brief description for the requested resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViolationDetail) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["MemberAccount"] = value["member_account"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    import capo_fms.types.resource_violations

    out["ResourceViolations"] = (
        capo_fms.types.resource_violations.serialize_aws_json_1_1(
            value["resource_violations"]
        )
    )
    if "resource_tags" in value:
        import capo_fms.types.tag_list

        out["ResourceTags"] = capo_fms.types.tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    if "resource_description" in value:
        out["ResourceDescription"] = value["resource_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ViolationDetail:
    out: ViolationDetail = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("MemberAccount") is not None:
        out["member_account"] = data["MemberAccount"]
    else:
        out["member_account"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceViolations") is not None:
        import capo_fms.types.resource_violations

        out["resource_violations"] = (
            capo_fms.types.resource_violations.deserialize_aws_json_1_1(
                data["ResourceViolations"]
            )
        )
    else:
        out["resource_violations"] = []
    if data.get("ResourceTags") is not None:
        import capo_fms.types.tag_list

        out["resource_tags"] = capo_fms.types.tag_list.deserialize_aws_json_1_1(
            data["ResourceTags"]
        )
    if data.get("ResourceDescription") is not None:
        out["resource_description"] = data["ResourceDescription"]
    return out
