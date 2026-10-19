"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateZonalAutoshiftConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.zonal_autoshift_status


class UpdateZonalAutoshiftConfigurationResponse(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you updated the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    zonal_autoshift_status: (
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The updated zonal autoshift status for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateZonalAutoshiftConfigurationResponse) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    import capo_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateZonalAutoshiftConfigurationResponse:
    out: UpdateZonalAutoshiftConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("zonalAutoshiftStatus") is not None:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["zonal_autoshift_status"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["zonalAutoshiftStatus"]
            )
        )
    else:
        import typing

        out["zonal_autoshift_status"] = typing.cast(
            "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus", ""
        )
    return out
