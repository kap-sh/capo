"""Generated from Smithy shape ``com.amazonaws.eks#CreateFargateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.fargate_profile_selectors
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_map


class CreateFargateProfileRequest(TypedDict, closed=True):
    fargate_profile_name: "capo_eks.types.string.String"
    """<p>The name of the Fargate profile.</p>"""
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    pod_execution_role_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the <code>Pod</code> execution role to use for a <code>Pod</code> that matches the selectors in the Fargate profile. The <code>Pod</code> execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html"> <code>Pod</code> execution role</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    subnets: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The IDs of subnets to launch a <code>Pod</code> into. A <code>Pod</code> running on Fargate isn't assigned a public IP address, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.</p>"""
    selectors: NotRequired[
        "capo_eks.types.fargate_profile_selectors.FargateProfileSelectors"
    ]
    """<p>The selectors to match for a <code>Pod</code> to use this Fargate profile. Each selector must have an associated Kubernetes <code>namespace</code>. Optionally, you can also specify <code>labels</code> for a <code>namespace</code>. You may specify up to five selectors in a Fargate profile.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFargateProfileRequest) -> dict:
    out: dict = {}
    out["fargateProfileName"] = value["fargate_profile_name"]
    out["podExecutionRoleArn"] = value["pod_execution_role_arn"]
    if "subnets" in value:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.serialize_json(value["subnets"])
    if "selectors" in value:
        import capo_eks.types.fargate_profile_selectors

        out["selectors"] = capo_eks.types.fargate_profile_selectors.serialize_json(
            value["selectors"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFargateProfileRequest:
    out: CreateFargateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("fargateProfileName") is not None:
        out["fargate_profile_name"] = data["fargateProfileName"]
    else:
        raise DeserializationError(
            "CreateFargateProfileRequest.fargate_profile_name required"
        )
    if data.get("podExecutionRoleArn") is not None:
        out["pod_execution_role_arn"] = data["podExecutionRoleArn"]
    else:
        raise DeserializationError(
            "CreateFargateProfileRequest.pod_execution_role_arn required"
        )
    if data.get("subnets") is not None:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.deserialize_json(data["subnets"])
    if data.get("selectors") is not None:
        import capo_eks.types.fargate_profile_selectors

        out["selectors"] = capo_eks.types.fargate_profile_selectors.deserialize_json(
            data["selectors"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    return out
