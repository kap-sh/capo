"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateSoftwareSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_validation_status


class UpdateSoftwareSetRequest(TypedDict, closed=True):
    id: "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    """<p>The ID of the software set to update.</p>"""
    validation_status: "capo_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus"
    """<p>An option to define if the software set has been validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSoftwareSetRequest) -> dict:
    out: dict = {}
    import capo_workspaces_thin_client.types.software_set_validation_status

    out["validationStatus"] = (
        capo_workspaces_thin_client.types.software_set_validation_status.serialize_json(
            value["validation_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSoftwareSetRequest:
    out: UpdateSoftwareSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("validationStatus") is not None:
        import capo_workspaces_thin_client.types.software_set_validation_status

        out["validation_status"] = (
            capo_workspaces_thin_client.types.software_set_validation_status.deserialize_json(
                data["validationStatus"]
            )
        )
    else:
        import typing

        out["validation_status"] = typing.cast(
            "capo_workspaces_thin_client.types.software_set_validation_status.SoftwareSetValidationStatus",
            "",
        )
    return out
