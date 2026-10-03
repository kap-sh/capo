"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_policy_arn
    import capo_imagebuilder.types.lifecycle_policy_details
    import capo_imagebuilder.types.lifecycle_policy_resource_selection
    import capo_imagebuilder.types.lifecycle_policy_resource_type
    import capo_imagebuilder.types.lifecycle_policy_status
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.role_name_or_arn


class UpdateLifecyclePolicyRequest(TypedDict, closed=True):
    lifecycle_policy_arn: (
        "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy resource.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Optional description for the lifecycle policy. Because the update replaces the entire configuration, omitting this property removes any existing description.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>Indicates whether the lifecycle policy resource is enabled. Defaults to <code>ENABLED</code> when omitted, so updating a disabled policy without setting this property re-enables it.</p>"""
    execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.</p>"""
    resource_type: "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    """<p>The type of image resource that the lifecycle policy applies to. The value must match the policy's existing resource type. You can't change the resource type of an existing lifecycle policy.</p>"""
    policy_details: (
        "capo_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails"
    )
    """<p>The configuration details for a lifecycle policy resource.</p>"""
    resource_selection: "capo_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection"
    """<p>Selection criteria for resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = capo_imagebuilder.types.lifecycle_policy_status.serialize_json(
            value["status"]
        )
    out["executionRole"] = value["execution_role"]
    import capo_imagebuilder.types.lifecycle_policy_resource_type

    out["resourceType"] = (
        capo_imagebuilder.types.lifecycle_policy_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_imagebuilder.types.lifecycle_policy_details

    out["policyDetails"] = (
        capo_imagebuilder.types.lifecycle_policy_details.serialize_json(
            value["policy_details"]
        )
    )
    import capo_imagebuilder.types.lifecycle_policy_resource_selection

    out["resourceSelection"] = (
        capo_imagebuilder.types.lifecycle_policy_resource_selection.serialize_json(
            value["resource_selection"]
        )
    )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateLifecyclePolicyRequest:
    out: UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("lifecyclePolicyArn") is not None:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.lifecycle_policy_arn required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_policy_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.execution_role required"
        )
    if data.get("resourceType") is not None:
        import capo_imagebuilder.types.lifecycle_policy_resource_type

        out["resource_type"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.resource_type required"
        )
    if data.get("policyDetails") is not None:
        import capo_imagebuilder.types.lifecycle_policy_details

        out["policy_details"] = (
            capo_imagebuilder.types.lifecycle_policy_details.deserialize_json(
                data["policyDetails"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.policy_details required"
        )
    if data.get("resourceSelection") is not None:
        import capo_imagebuilder.types.lifecycle_policy_resource_selection

        out["resource_selection"] = (
            capo_imagebuilder.types.lifecycle_policy_resource_selection.deserialize_json(
                data["resourceSelection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.resource_selection required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateLifecyclePolicyRequest.client_token required")
    return out
