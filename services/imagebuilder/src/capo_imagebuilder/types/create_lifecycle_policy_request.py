"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.lifecycle_policy_details
    import capo_imagebuilder.types.lifecycle_policy_resource_selection
    import capo_imagebuilder.types.lifecycle_policy_resource_type
    import capo_imagebuilder.types.lifecycle_policy_status
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map


class CreateLifecyclePolicyRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the lifecycle policy to create. Policy names must be unique to your account in each Amazon Web Services Region. Image Builder generates the policy ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. You can't change the name after creation.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Optional description for the lifecycle policy.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>Indicates whether the lifecycle policy resource is enabled. If you don't specify a status, it defaults to <code>ENABLED</code>. Only enabled policies run on their schedule.</p>"""
    execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions. You must have permission to pass the role, and the role's trust policy must allow the Image Builder service principal to assume it.</p>"""
    resource_type: "capo_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    """<p>The type of Image Builder resource that the lifecycle policy applies to. The resource type determines the allowed rule actions: policies for AMI-based Image Builder images support <code>DELETE</code>, <code>DEPRECATE</code>, and <code>DISABLE</code>, and policies for container-based Image Builder images support only <code>DELETE</code>. You can't change the resource type after creation.</p>"""
    policy_details: (
        "capo_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails"
    )
    """<p>Configuration details for the lifecycle policy rules. A policy can contain at most one rule per action type: one <code>DELETE</code>, one <code>DEPRECATE</code>, and one <code>DISABLE</code>.</p>"""
    resource_selection: "capo_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection"
    """<p>Selection criteria for the resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags to apply to the lifecycle policy resource.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateLifecyclePolicyRequest:
    out: CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.name required")
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
            "CreateLifecyclePolicyRequest.execution_role required"
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
            "CreateLifecyclePolicyRequest.resource_type required"
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
            "CreateLifecyclePolicyRequest.policy_details required"
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
            "CreateLifecyclePolicyRequest.resource_selection required"
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.client_token required")
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
