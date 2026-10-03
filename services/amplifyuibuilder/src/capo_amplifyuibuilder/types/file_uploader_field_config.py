"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FileUploaderFieldConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.storage_access_level
    import capo_amplifyuibuilder.types.str_values


class FileUploaderFieldConfig(TypedDict, closed=True):
    access_level: "capo_amplifyuibuilder.types.storage_access_level.StorageAccessLevel"
    """<p>The access level to assign to the uploaded files in the Amazon S3 bucket where they are stored. The valid values for this property are <code>private</code>, <code>protected</code>, or <code>public</code>. For detailed information about the permissions associated with each access level, see <a href="https://docs.amplify.aws/lib/storage/configureaccess/q/platform/js/">File access levels</a> in the <i>Amplify documentation</i>.</p>"""
    accepted_file_types: "capo_amplifyuibuilder.types.str_values.StrValues"
    """<p>The file types that are allowed to be uploaded by the file uploader. Provide this information in an array of strings specifying the valid file extensions.</p>"""
    show_thumbnails: NotRequired["bool"]
    """<p>Specifies whether to display or hide the image preview after selecting a file for upload. The default value is <code>true</code> to display the image preview.</p>"""
    is_resumable: NotRequired["bool"]
    """<p>Allows the file upload operation to be paused and resumed. The default value is <code>false</code>.</p> <p>When <code>isResumable</code> is set to <code>true</code>, the file uploader uses a multipart upload to break the files into chunks before upload. The progress of the upload isn't continuous, because the file uploader uploads a chunk at a time.</p>"""
    max_file_count: NotRequired["int"]
    """<p>Specifies the maximum number of files that can be selected to upload. The default value is an unlimited number of files.</p>"""
    max_size: NotRequired["int"]
    """<p>The maximum file size in bytes that the file uploader will accept. The default value is an unlimited file size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileUploaderFieldConfig) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.storage_access_level

    out["accessLevel"] = (
        capo_amplifyuibuilder.types.storage_access_level.serialize_json(
            value["access_level"]
        )
    )
    import capo_amplifyuibuilder.types.str_values

    out["acceptedFileTypes"] = capo_amplifyuibuilder.types.str_values.serialize_json(
        value["accepted_file_types"]
    )
    if "show_thumbnails" in value:
        out["showThumbnails"] = value["show_thumbnails"]
    if "is_resumable" in value:
        out["isResumable"] = value["is_resumable"]
    if "max_file_count" in value:
        out["maxFileCount"] = value["max_file_count"]
    if "max_size" in value:
        out["maxSize"] = value["max_size"]
    return out


def deserialize_json(data: dict) -> FileUploaderFieldConfig:
    out: FileUploaderFieldConfig = {}  # type: ignore[typeddict-item]
    if data.get("accessLevel") is not None:
        import capo_amplifyuibuilder.types.storage_access_level

        out["access_level"] = (
            capo_amplifyuibuilder.types.storage_access_level.deserialize_json(
                data["accessLevel"]
            )
        )
    else:
        raise DeserializationError("FileUploaderFieldConfig.access_level required")
    if data.get("acceptedFileTypes") is not None:
        import capo_amplifyuibuilder.types.str_values

        out["accepted_file_types"] = (
            capo_amplifyuibuilder.types.str_values.deserialize_json(
                data["acceptedFileTypes"]
            )
        )
    else:
        raise DeserializationError(
            "FileUploaderFieldConfig.accepted_file_types required"
        )
    if data.get("showThumbnails") is not None:
        out["show_thumbnails"] = data["showThumbnails"]
    if data.get("isResumable") is not None:
        out["is_resumable"] = data["isResumable"]
    if data.get("maxFileCount") is not None:
        out["max_file_count"] = data["maxFileCount"]
    if data.get("maxSize") is not None:
        out["max_size"] = data["maxSize"]
    return out
