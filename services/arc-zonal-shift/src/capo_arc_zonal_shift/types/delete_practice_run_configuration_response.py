"""Generated from Smithy shape ``com.amazonaws.arczonalshift#DeletePracticeRunConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.resource_arn
    import capo_arc_zonal_shift.types.resource_name
    import capo_arc_zonal_shift.types.zonal_autoshift_status


class DeletePracticeRunConfigurationResponse(TypedDict, closed=True):
    arn: "capo_arc_zonal_shift.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you deleted the practice run for.</p>"""
    name: "capo_arc_zonal_shift.types.resource_name.ResourceName"
    """<p>The name of the resource that you deleted the practice run for. </p>"""
    zonal_autoshift_status: (
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The status of zonal autoshift for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePracticeRunConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeletePracticeRunConfigurationResponse:
    out: DeletePracticeRunConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
