"""Generated from Smithy shape ``com.amazonaws.imagebuilder#StartResourceStateUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.resource_state
    import capo_imagebuilder.types.resource_state_update_exclusion_rules
    import capo_imagebuilder.types.resource_state_update_include_resources
    import capo_imagebuilder.types.role_name_or_arn


class StartResourceStateUpdateRequest(TypedDict, closed=True):
    resource_arn: "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image build version to update. The image must be in one of these terminal states: <code>AVAILABLE</code>, <code>DEPRECATED</code>, <code>DISABLED</code>, <code>FAILED</code>, or <code>CANCELLED</code>. Images with <code>FAILED</code> or <code>CANCELLED</code> status can transition only to <code>DELETED</code>.</p>"""
    state: "capo_imagebuilder.types.resource_state.ResourceState"
    """<p>Specifies the lifecycle action to take for this request. For AMI-based images, valid values are <code>AVAILABLE</code>, <code>DEPRECATED</code>, <code>DISABLED</code>, and <code>DELETED</code>. For container-based images, only <code>DELETED</code> is supported.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that's used to update image state. You must provide this property together with <code>includeResources</code>. Neither is valid without the other.</p>"""
    include_resources: NotRequired[
        "capo_imagebuilder.types.resource_state_update_include_resources.ResourceStateUpdateIncludeResources"
    ]
    """<p>Specifies which underlying resources to update, in addition to the Image Builder image resource itself. Snapshots and containers are only valid for the <code>DELETED</code> state. To set an image to <code>DELETED</code>, you must include its underlying resources. To delete only the Image Builder image record, use the <a>DeleteImage</a> operation instead.</p>"""
    exclusion_rules: NotRequired[
        "capo_imagebuilder.types.resource_state_update_exclusion_rules.ResourceStateUpdateExclusionRules"
    ]
    """<p>Rules that Image Builder evaluates against each of the image's AMIs. Matching AMIs and their snapshots are skipped. Exclusion rules only take effect when the request includes AMIs. If the target state is <code>DELETED</code> and any resource was skipped, the Image Builder image resource itself is also retained. For the <code>DEPRECATED</code> and <code>DISABLED</code> target states, Image Builder updates the image resource's state regardless of exclusions.</p>"""
    update_at: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp that indicates when resources are updated by a lifecycle action. This property is valid only when the target status is <code>DEPRECATED</code>, and the value must be a future time. If you don't specify a value, Image Builder begins the state update right away. For a scheduled deprecation, included AMIs get their EC2 deprecation time set immediately, and Image Builder schedules the image resource to transition to <code>DEPRECATED</code> at that time.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceStateUpdateRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_imagebuilder.types.resource_state

    out["state"] = capo_imagebuilder.types.resource_state.serialize_json(value["state"])
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "include_resources" in value:
        import capo_imagebuilder.types.resource_state_update_include_resources

        out["includeResources"] = (
            capo_imagebuilder.types.resource_state_update_include_resources.serialize_json(
                value["include_resources"]
            )
        )
    if "exclusion_rules" in value:
        import capo_imagebuilder.types.resource_state_update_exclusion_rules

        out["exclusionRules"] = (
            capo_imagebuilder.types.resource_state_update_exclusion_rules.serialize_json(
                value["exclusion_rules"]
            )
        )
    if "update_at" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["updateAt"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["update_at"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartResourceStateUpdateRequest:
    out: StartResourceStateUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "StartResourceStateUpdateRequest.resource_arn required"
        )
    if data.get("state") is not None:
        import capo_imagebuilder.types.resource_state

        out["state"] = capo_imagebuilder.types.resource_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("StartResourceStateUpdateRequest.state required")
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("includeResources") is not None:
        import capo_imagebuilder.types.resource_state_update_include_resources

        out["include_resources"] = (
            capo_imagebuilder.types.resource_state_update_include_resources.deserialize_json(
                data["includeResources"]
            )
        )
    if data.get("exclusionRules") is not None:
        import capo_imagebuilder.types.resource_state_update_exclusion_rules

        out["exclusion_rules"] = (
            capo_imagebuilder.types.resource_state_update_exclusion_rules.deserialize_json(
                data["exclusionRules"]
            )
        )
    if data.get("updateAt") is not None:
        import capo_imagebuilder.types.date_time_timestamp

        out["update_at"] = capo_imagebuilder.types.date_time_timestamp.deserialize_json(
            data["updateAt"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "StartResourceStateUpdateRequest.client_token required"
        )
    return out
