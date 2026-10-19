"""Generated from Smithy shape ``com.amazonaws.codecommit#GetFolderOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_list
    import capo_codecommit.types.folder_list
    import capo_codecommit.types.object_id
    import capo_codecommit.types.path
    import capo_codecommit.types.sub_module_list
    import capo_codecommit.types.symbolic_link_list


class GetFolderOutput(TypedDict, closed=True):
    commit_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The full commit ID used as a reference for the returned version of the folder content.</p>"""
    folder_path: "capo_codecommit.types.path.Path"
    """<p>The fully qualified path of the folder whose contents are returned.</p>"""
    tree_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the folder.</p>"""
    sub_folders: NotRequired["capo_codecommit.types.folder_list.FolderList"]
    """<p>The list of folders that exist under the specified folder, if any.</p>"""
    files: NotRequired["capo_codecommit.types.file_list.FileList"]
    """<p>The list of files in the specified folder, if any.</p>"""
    symbolic_links: NotRequired[
        "capo_codecommit.types.symbolic_link_list.SymbolicLinkList"
    ]
    """<p>The list of symbolic links to other files and folders in the specified folder, if any.</p>"""
    sub_modules: NotRequired["capo_codecommit.types.sub_module_list.SubModuleList"]
    """<p>The list of submodules in the specified folder, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFolderOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["folderPath"] = value["folder_path"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    if "sub_folders" in value:
        import capo_codecommit.types.folder_list

        out["subFolders"] = capo_codecommit.types.folder_list.serialize_aws_json_1_1(
            value["sub_folders"]
        )
    if "files" in value:
        import capo_codecommit.types.file_list

        out["files"] = capo_codecommit.types.file_list.serialize_aws_json_1_1(
            value["files"]
        )
    if "symbolic_links" in value:
        import capo_codecommit.types.symbolic_link_list

        out["symbolicLinks"] = (
            capo_codecommit.types.symbolic_link_list.serialize_aws_json_1_1(
                value["symbolic_links"]
            )
        )
    if "sub_modules" in value:
        import capo_codecommit.types.sub_module_list

        out["subModules"] = (
            capo_codecommit.types.sub_module_list.serialize_aws_json_1_1(
                value["sub_modules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFolderOutput:
    out: GetFolderOutput = {}  # type: ignore[typeddict-item]
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    else:
        out["commit_id"] = ""
    if data.get("folderPath") is not None:
        out["folder_path"] = data["folderPath"]
    else:
        out["folder_path"] = ""
    if data.get("treeId") is not None:
        out["tree_id"] = data["treeId"]
    if data.get("subFolders") is not None:
        import capo_codecommit.types.folder_list

        out["sub_folders"] = capo_codecommit.types.folder_list.deserialize_aws_json_1_1(
            data["subFolders"]
        )
    if data.get("files") is not None:
        import capo_codecommit.types.file_list

        out["files"] = capo_codecommit.types.file_list.deserialize_aws_json_1_1(
            data["files"]
        )
    if data.get("symbolicLinks") is not None:
        import capo_codecommit.types.symbolic_link_list

        out["symbolic_links"] = (
            capo_codecommit.types.symbolic_link_list.deserialize_aws_json_1_1(
                data["symbolicLinks"]
            )
        )
    if data.get("subModules") is not None:
        import capo_codecommit.types.sub_module_list

        out["sub_modules"] = (
            capo_codecommit.types.sub_module_list.deserialize_aws_json_1_1(
                data["subModules"]
            )
        )
    return out
