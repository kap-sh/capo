"""Generated from Smithy shape ``com.amazonaws.deadline#Attachments``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.job_attachments_file_system
    import capo_deadline.types.manifest_properties_list


class Attachments(TypedDict, closed=True):
    manifests: "capo_deadline.types.manifest_properties_list.ManifestPropertiesList"
    """<p>The manifest properties for the attachments.</p>"""
    file_system: (
        "capo_deadline.types.job_attachments_file_system.JobAttachmentsFileSystem"
    )
    """<p>The file system location for the attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attachments) -> dict:
    out: dict = {}
    import capo_deadline.types.manifest_properties_list

    out["manifests"] = capo_deadline.types.manifest_properties_list.serialize_json(
        value["manifests"]
    )
    import capo_deadline.types.job_attachments_file_system

    out["fileSystem"] = capo_deadline.types.job_attachments_file_system.serialize_json(
        value.get("file_system", "COPIED")
    )
    return out


def deserialize_json(data: dict) -> Attachments:
    out: Attachments = {}  # type: ignore[typeddict-item]
    if data.get("manifests") is not None:
        import capo_deadline.types.manifest_properties_list

        out["manifests"] = (
            capo_deadline.types.manifest_properties_list.deserialize_json(
                data["manifests"]
            )
        )
    else:
        raise DeserializationError("Attachments.manifests required")
    if data.get("fileSystem") is not None:
        import capo_deadline.types.job_attachments_file_system

        out["file_system"] = (
            capo_deadline.types.job_attachments_file_system.deserialize_json(
                data["fileSystem"]
            )
        )
    else:
        out["file_system"] = "COPIED"
    return out


def redact_sensitive(value: Attachments) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "manifests" in value:
        import capo_deadline.types.manifest_properties_list

        out["manifests"] = (
            capo_deadline.types.manifest_properties_list.redact_sensitive(
                value["manifests"]
            )
        )
    return out
