"""Generated from Smithy shape ``com.amazonaws.mgn#StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.fsx_ontap_configuration
    import capo_mgn.types.storage_type


class StorageConfiguration(TypedDict, closed=True):
    storage_type: "capo_mgn.types.storage_type.StorageType"
    """<p>Storage configuration storage type.</p>"""
    fsx_ontap_configuration: NotRequired[
        "capo_mgn.types.fsx_ontap_configuration.FsxOntapConfiguration"
    ]
    """<p>Storage configuration FSx ONTAP configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfiguration) -> dict:
    out: dict = {}
    out["storageType"] = value["storage_type"]
    if "fsx_ontap_configuration" in value:
        import capo_mgn.types.fsx_ontap_configuration

        out["fsxOntapConfiguration"] = (
            capo_mgn.types.fsx_ontap_configuration.serialize_json(
                value["fsx_ontap_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    else:
        out["storage_type"] = ""
    if data.get("fsxOntapConfiguration") is not None:
        import capo_mgn.types.fsx_ontap_configuration

        out["fsx_ontap_configuration"] = (
            capo_mgn.types.fsx_ontap_configuration.deserialize_json(
                data["fsxOntapConfiguration"]
            )
        )
    return out
