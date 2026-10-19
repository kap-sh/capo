"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.compute_type
    import capo_workspaces.types.root_storage
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.user_storage
    import capo_workspaces.types.workspace_bundle_description
    import capo_workspaces.types.workspace_bundle_name
    import capo_workspaces.types.workspace_image_id


class CreateWorkspaceBundleRequest(TypedDict, closed=True):
    bundle_name: "capo_workspaces.types.workspace_bundle_name.WorkspaceBundleName"
    """<p>The name of the bundle.</p>"""
    bundle_description: (
        "capo_workspaces.types.workspace_bundle_description.WorkspaceBundleDescription"
    )
    """<p>The description of the bundle.</p>"""
    image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image that is used to create the bundle.</p>"""
    compute_type: "capo_workspaces.types.compute_type.ComputeType"
    user_storage: "capo_workspaces.types.user_storage.UserStorage"
    root_storage: NotRequired["capo_workspaces.types.root_storage.RootStorage"]
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the bundle.</p> <note> <p>To add tags at the same time when you're creating the bundle, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceBundleRequest) -> dict:
    out: dict = {}
    out["BundleName"] = value["bundle_name"]
    out["BundleDescription"] = value["bundle_description"]
    out["ImageId"] = value["image_id"]
    import capo_workspaces.types.compute_type

    out["ComputeType"] = capo_workspaces.types.compute_type.serialize_aws_json_1_1(
        value["compute_type"]
    )
    import capo_workspaces.types.user_storage

    out["UserStorage"] = capo_workspaces.types.user_storage.serialize_aws_json_1_1(
        value["user_storage"]
    )
    if "root_storage" in value:
        import capo_workspaces.types.root_storage

        out["RootStorage"] = capo_workspaces.types.root_storage.serialize_aws_json_1_1(
            value["root_storage"]
        )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceBundleRequest:
    out: CreateWorkspaceBundleRequest = {}  # type: ignore[typeddict-item]
    if data.get("BundleName") is not None:
        out["bundle_name"] = data["BundleName"]
    else:
        out["bundle_name"] = ""
    if data.get("BundleDescription") is not None:
        out["bundle_description"] = data["BundleDescription"]
    else:
        out["bundle_description"] = ""
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    else:
        out["image_id"] = ""
    if data.get("ComputeType") is not None:
        import capo_workspaces.types.compute_type

        out["compute_type"] = (
            capo_workspaces.types.compute_type.deserialize_aws_json_1_1(
                data["ComputeType"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.compute_type required")
    if data.get("UserStorage") is not None:
        import capo_workspaces.types.user_storage

        out["user_storage"] = (
            capo_workspaces.types.user_storage.deserialize_aws_json_1_1(
                data["UserStorage"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.user_storage required")
    if data.get("RootStorage") is not None:
        import capo_workspaces.types.root_storage

        out["root_storage"] = (
            capo_workspaces.types.root_storage.deserialize_aws_json_1_1(
                data["RootStorage"]
            )
        )
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
