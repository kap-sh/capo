"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdateZonalAutoshiftConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.zonal_autoshift_status


class UpdateZonalAutoshiftConfigurationRequest(TypedDict, closed=True):
    resource_identifier: (
        "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The identifier for the resource that you want to update the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>"""
    zonal_autoshift_status: (
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The zonal autoshift status for the resource that you want to update the zonal autoshift configuration for. Choose <code>ENABLED</code> to authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateZonalAutoshiftConfigurationRequest) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateZonalAutoshiftConfigurationRequest:
    out: UpdateZonalAutoshiftConfigurationRequest = {}  # type: ignore[typeddict-item]
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
