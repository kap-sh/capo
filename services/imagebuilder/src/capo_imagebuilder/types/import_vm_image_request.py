"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportVmImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number


class ImportVmImageRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the base image that is created by the import process. Image Builder generates the image ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If an image with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the import creates a new build version for it.</p>"""
    semantic_version: "capo_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version to attach to the base image that was created during the import process. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description for the base image that is created by the import process.</p>"""
    platform: "capo_imagebuilder.types.platform.Platform"
    """<p>The operating system platform for the imported VM.</p>"""
    os_version: NotRequired["capo_imagebuilder.types.os_version.OsVersion"]
    """<p>The operating system version for the imported VM.</p>"""
    vm_import_task_id: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The <code>importTaskId</code> (API) or <code>ImportTaskId</code> (CLI) from the Amazon EC2 VM import process. The import task doesn't need to be complete when you call ImportVmImage - Image Builder monitors the task and finishes creating the image when the task completes.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The CloudWatch Logs log group where Image Builder sends the import logs. For ImportVmImage, the log group name must be within the <code>/aws/imagebuilder/</code> namespace.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the import resources.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportVmImageRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_imagebuilder.types.platform

    out["platform"] = capo_imagebuilder.types.platform.serialize_json(value["platform"])
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    out["vmImportTaskId"] = value["vm_import_task_id"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportVmImageRequest:
    out: ImportVmImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportVmImageRequest.name required")
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportVmImageRequest.semantic_version required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("ImportVmImageRequest.platform required")
    if data.get("osVersion") is not None:
        out["os_version"] = data["osVersion"]
    if data.get("vmImportTaskId") is not None:
        out["vm_import_task_id"] = data["vmImportTaskId"]
    else:
        raise DeserializationError("ImportVmImageRequest.vm_import_task_id required")
    if data.get("loggingConfiguration") is not None:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ImportVmImageRequest.client_token required")
    return out
