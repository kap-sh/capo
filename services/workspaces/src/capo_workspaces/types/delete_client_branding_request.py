"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteClientBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.client_device_type_list
    import capo_workspaces.types.directory_id


class DeleteClientBrandingRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier of the WorkSpace for which you want to delete client branding.</p>"""
    platforms: "capo_workspaces.types.client_device_type_list.ClientDeviceTypeList"
    """<p>The device type for which you want to delete client branding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClientBrandingRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.client_device_type_list

    out["Platforms"] = (
        capo_workspaces.types.client_device_type_list.serialize_aws_json_1_1(
            value["platforms"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClientBrandingRequest:
    out: DeleteClientBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Platforms") is not None:
        import capo_workspaces.types.client_device_type_list

        out["platforms"] = (
            capo_workspaces.types.client_device_type_list.deserialize_aws_json_1_1(
                data["Platforms"]
            )
        )
    else:
        out["platforms"] = []
    return out
