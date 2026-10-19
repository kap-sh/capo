"""Generated from Smithy shape ``com.amazonaws.arczonalshift#UpdatePracticeRunConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.practice_run_configuration
    import capo_arc_zonal_shift.types.resource_arn
    import capo_arc_zonal_shift.types.resource_name
    import capo_arc_zonal_shift.types.zonal_autoshift_status


class UpdatePracticeRunConfigurationResponse(TypedDict, closed=True):
    arn: "capo_arc_zonal_shift.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you updated the practice run for.</p>"""
    name: "capo_arc_zonal_shift.types.resource_name.ResourceName"
    """<p>The name of the resource that you updated the practice run for. </p>"""
    zonal_autoshift_status: (
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    )
    """<p>The zonal autoshift status for the resource that you updated the practice run for.</p>"""
    practice_run_configuration: (
        "capo_arc_zonal_shift.types.practice_run_configuration.PracticeRunConfiguration"
    )
    """<p>The practice run configuration that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePracticeRunConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_arc_zonal_shift.types.zonal_autoshift_status

    out["zonalAutoshiftStatus"] = (
        capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
            value["zonal_autoshift_status"]
        )
    )
    import capo_arc_zonal_shift.types.practice_run_configuration

    out["practiceRunConfiguration"] = (
        capo_arc_zonal_shift.types.practice_run_configuration.serialize_json(
            value["practice_run_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePracticeRunConfigurationResponse:
    out: UpdatePracticeRunConfigurationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("practiceRunConfiguration") is not None:
        import capo_arc_zonal_shift.types.practice_run_configuration

        out["practice_run_configuration"] = (
            capo_arc_zonal_shift.types.practice_run_configuration.deserialize_json(
                data["practiceRunConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePracticeRunConfigurationResponse.practice_run_configuration required"
        )
    return out
