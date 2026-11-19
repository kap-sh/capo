"""Generated from Smithy shape ``com.amazonaws.fms#WebACLHasOutOfScopeResourcesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_arn_list


class WebACLHasOutOfScopeResourcesViolation(TypedDict, closed=True):
    web_acl_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the web ACL. </p>"""
    out_of_scope_resource_list: NotRequired[
        "capo_fms.types.resource_arn_list.ResourceArnList"
    ]
    """<p>An array of Amazon Resource Name (ARN) for the resources that are out of scope of the policy and are associated with the web ACL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLHasOutOfScopeResourcesViolation) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    if "out_of_scope_resource_list" in value:
        import capo_fms.types.resource_arn_list

        out["OutOfScopeResourceList"] = (
            capo_fms.types.resource_arn_list.serialize_aws_json_1_1(
                value["out_of_scope_resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLHasOutOfScopeResourcesViolation:
    out: WebACLHasOutOfScopeResourcesViolation = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    if data.get("OutOfScopeResourceList") is not None:
        import capo_fms.types.resource_arn_list

        out["out_of_scope_resource_list"] = (
            capo_fms.types.resource_arn_list.deserialize_aws_json_1_1(
                data["OutOfScopeResourceList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebACLHasOutOfScopeResourcesViolation) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    if "out_of_scope_resource_list" in value:
        import capo_fms.types.resource_arn_list

        out["OutOfScopeResourceList"] = capo_fms.types.resource_arn_list.serialize_cbor(
            value["out_of_scope_resource_list"]
        )
    return out


def deserialize_cbor(data: dict) -> WebACLHasOutOfScopeResourcesViolation:
    out: WebACLHasOutOfScopeResourcesViolation = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    if data.get("OutOfScopeResourceList") is not None:
        import capo_fms.types.resource_arn_list

        out["out_of_scope_resource_list"] = (
            capo_fms.types.resource_arn_list.deserialize_cbor(
                data["OutOfScopeResourceList"]
            )
        )
    return out
