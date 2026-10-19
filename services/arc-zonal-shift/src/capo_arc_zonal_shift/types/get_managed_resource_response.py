"""Generated from Smithy shape ``com.amazonaws.arczonalshift#GetManagedResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.applied_weights
    import capo_arc_zonal_shift.types.autoshifts_in_resource
    import capo_arc_zonal_shift.types.practice_run_configuration
    import capo_arc_zonal_shift.types.resource_arn
    import capo_arc_zonal_shift.types.resource_name
    import capo_arc_zonal_shift.types.zonal_autoshift_status
    import capo_arc_zonal_shift.types.zonal_shifts_in_resource


class GetManagedResourceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_arc_zonal_shift.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the resource.</p>"""
    name: NotRequired["capo_arc_zonal_shift.types.resource_name.ResourceName"]
    """<p>The name of the resource.</p>"""
    applied_weights: "capo_arc_zonal_shift.types.applied_weights.AppliedWeights"
    """<p>A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.</p>"""
    zonal_shifts: (
        "capo_arc_zonal_shift.types.zonal_shifts_in_resource.ZonalShiftsInResource"
    )
    """<p>The zonal shifts that are currently active for a resource. </p>"""
    autoshifts: NotRequired[
        "capo_arc_zonal_shift.types.autoshifts_in_resource.AutoshiftsInResource"
    ]
    """<p>An array of the autoshifts that are active for the resource.</p>"""
    practice_run_configuration: NotRequired[
        "capo_arc_zonal_shift.types.practice_run_configuration.PracticeRunConfiguration"
    ]
    """<p>The practice run configuration for zonal autoshift that's associated with the resource.</p>"""
    zonal_autoshift_status: NotRequired[
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    ]
    """<p>The status for zonal autoshift for a resource. When the autoshift status is <code>ENABLED</code>, Amazon Web Services shifts traffic for a resource away from an Availability Zone, on your behalf, when Amazon Web Services determines that there's an issue in the Availability Zone that could potentially affect customers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedResourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_arc_zonal_shift.types.applied_weights

    out["appliedWeights"] = capo_arc_zonal_shift.types.applied_weights.serialize_json(
        value["applied_weights"]
    )
    import capo_arc_zonal_shift.types.zonal_shifts_in_resource

    out["zonalShifts"] = (
        capo_arc_zonal_shift.types.zonal_shifts_in_resource.serialize_json(
            value["zonal_shifts"]
        )
    )
    if "autoshifts" in value:
        import capo_arc_zonal_shift.types.autoshifts_in_resource

        out["autoshifts"] = (
            capo_arc_zonal_shift.types.autoshifts_in_resource.serialize_json(
                value["autoshifts"]
            )
        )
    if "practice_run_configuration" in value:
        import capo_arc_zonal_shift.types.practice_run_configuration

        out["practiceRunConfiguration"] = (
            capo_arc_zonal_shift.types.practice_run_configuration.serialize_json(
                value["practice_run_configuration"]
            )
        )
    if "zonal_autoshift_status" in value:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["zonalAutoshiftStatus"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
                value["zonal_autoshift_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedResourceResponse:
    out: GetManagedResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("appliedWeights") is not None:
        import capo_arc_zonal_shift.types.applied_weights

        out["applied_weights"] = (
            capo_arc_zonal_shift.types.applied_weights.deserialize_json(
                data["appliedWeights"]
            )
        )
    else:
        out["applied_weights"] = {}
    if data.get("zonalShifts") is not None:
        import capo_arc_zonal_shift.types.zonal_shifts_in_resource

        out["zonal_shifts"] = (
            capo_arc_zonal_shift.types.zonal_shifts_in_resource.deserialize_json(
                data["zonalShifts"]
            )
        )
    else:
        out["zonal_shifts"] = []
    if data.get("autoshifts") is not None:
        import capo_arc_zonal_shift.types.autoshifts_in_resource

        out["autoshifts"] = (
            capo_arc_zonal_shift.types.autoshifts_in_resource.deserialize_json(
                data["autoshifts"]
            )
        )
    if data.get("practiceRunConfiguration") is not None:
        import capo_arc_zonal_shift.types.practice_run_configuration

        out["practice_run_configuration"] = (
            capo_arc_zonal_shift.types.practice_run_configuration.deserialize_json(
                data["practiceRunConfiguration"]
            )
        )
    if data.get("zonalAutoshiftStatus") is not None:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["zonal_autoshift_status"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["zonalAutoshiftStatus"]
            )
        )
    return out
