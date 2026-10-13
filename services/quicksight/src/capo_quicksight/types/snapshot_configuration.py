"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.parameters
    import capo_quicksight.types.snapshot_destination_configuration
    import capo_quicksight.types.snapshot_file_group_list


class SnapshotConfiguration(TypedDict, closed=True):
    file_groups: "capo_quicksight.types.snapshot_file_group_list.SnapshotFileGroupList"
    """<p>A list of <code>SnapshotJobResultFileGroup</code> objects that contain information about the snapshot that is generated. This list can hold a maximum of 6 <code>FileGroup</code> configurations.</p>"""
    destination_configuration: NotRequired[
        "capo_quicksight.types.snapshot_destination_configuration.SnapshotDestinationConfiguration"
    ]
    """<p>A structure that contains information on the Amazon S3 bucket that the generated snapshot is stored in.</p>"""
    parameters: NotRequired["capo_quicksight.types.parameters.Parameters"]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.snapshot_file_group_list

    out["FileGroups"] = capo_quicksight.types.snapshot_file_group_list.serialize_json(
        value["file_groups"]
    )
    if "destination_configuration" in value:
        import capo_quicksight.types.snapshot_destination_configuration

        out["DestinationConfiguration"] = (
            capo_quicksight.types.snapshot_destination_configuration.serialize_json(
                value["destination_configuration"]
            )
        )
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["Parameters"] = capo_quicksight.types.parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> SnapshotConfiguration:
    out: SnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FileGroups") is not None:
        import capo_quicksight.types.snapshot_file_group_list

        out["file_groups"] = (
            capo_quicksight.types.snapshot_file_group_list.deserialize_json(
                data["FileGroups"]
            )
        )
    else:
        raise DeserializationError("SnapshotConfiguration.file_groups required")
    if data.get("DestinationConfiguration") is not None:
        import capo_quicksight.types.snapshot_destination_configuration

        out["destination_configuration"] = (
            capo_quicksight.types.snapshot_destination_configuration.deserialize_json(
                data["DestinationConfiguration"]
            )
        )
    if data.get("Parameters") is not None:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.deserialize_json(
            data["Parameters"]
        )
    return out


def redact_sensitive(value: SnapshotConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.redact_sensitive(
            value["parameters"]
        )
    return out
