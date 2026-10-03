"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectFileSystemLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.file_system_type
    import capo_codebuild.types.string


class ProjectFileSystemLocation(TypedDict, closed=True):
    type: NotRequired["capo_codebuild.types.file_system_type.FileSystemType"]
    """<p> The type of the file system. The one supported type is <code>EFS</code>. </p>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>A string that specifies the location of the file system created by Amazon EFS. Its format is <code>efs-dns-name:/directory-path</code>. You can find the DNS name of file system when you view it in the Amazon EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is <code>fs-abcd1234.efs.us-west-2.amazonaws.com</code>, and its mount directory is <code>my-efs-mount-directory</code>, then the <code>location</code> is <code>fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory</code>. </p> <p>The directory path in the format <code>efs-dns-name:/directory-path</code> is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system. </p>"""
    mount_point: NotRequired["capo_codebuild.types.string.String"]
    """<p>The location in the container where you mount the file system. </p>"""
    identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p>The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the <code>identifier</code> in all capital letters to <code>CODEBUILD_</code>. For example, if you specify <code>my_efs</code> for <code>identifier</code>, a new environment variable is create named <code>CODEBUILD_MY_EFS</code>. </p> <p> The <code>identifier</code> is used to mount your file system. </p>"""
    mount_options: NotRequired["capo_codebuild.types.string.String"]
    """<p> The mount options for a file system created by Amazon EFS. The default mount options used by CodeBuild are <code>nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2</code>. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html">Recommended NFS Mount Options</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectFileSystemLocation) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codebuild.types.file_system_type

        out["type"] = capo_codebuild.types.file_system_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "mount_point" in value:
        out["mountPoint"] = value["mount_point"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "mount_options" in value:
        out["mountOptions"] = value["mount_options"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectFileSystemLocation:
    out: ProjectFileSystemLocation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.file_system_type

        out["type"] = capo_codebuild.types.file_system_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("mountPoint") is not None:
        out["mount_point"] = data["mountPoint"]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("mountOptions") is not None:
        out["mount_options"] = data["mountOptions"]
    return out
