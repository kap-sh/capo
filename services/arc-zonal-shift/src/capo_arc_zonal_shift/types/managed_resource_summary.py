"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ManagedResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.applied_weights
    import capo_arc_zonal_shift.types.autoshifts_in_resource
    import capo_arc_zonal_shift.types.availability_zones
    import capo_arc_zonal_shift.types.resource_arn
    import capo_arc_zonal_shift.types.resource_name
    import capo_arc_zonal_shift.types.zonal_autoshift_status
    import capo_arc_zonal_shift.types.zonal_shifts_in_resource


class ManagedResourceSummary(TypedDict, closed=True):
    arn: NotRequired["capo_arc_zonal_shift.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the managed resource.</p>"""
    name: NotRequired["capo_arc_zonal_shift.types.resource_name.ResourceName"]
    """<p>The name of the managed resource.</p>"""
    availability_zones: (
        "capo_arc_zonal_shift.types.availability_zones.AvailabilityZones"
    )
    """<p>The Availability Zones that a resource is deployed in.</p>"""
    applied_weights: NotRequired[
        "capo_arc_zonal_shift.types.applied_weights.AppliedWeights"
    ]
    """<p>A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.</p>"""
    zonal_shifts: NotRequired[
        "capo_arc_zonal_shift.types.zonal_shifts_in_resource.ZonalShiftsInResource"
    ]
    """<p>An array of the zonal shifts for a resource.</p>"""
    autoshifts: NotRequired[
        "capo_arc_zonal_shift.types.autoshifts_in_resource.AutoshiftsInResource"
    ]
    """<p>An array of the autoshifts that have been completed for a resource.</p>"""
    zonal_autoshift_status: NotRequired[
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    ]
    """<p>The status of autoshift for a resource. When you configure zonal autoshift for a resource, you can set the value of the status to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    practice_run_status: NotRequired[
        "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    ]
    """<p>This status tracks whether a practice run configuration exists for a resource. When you configure a practice run for a resource so that a practice run configuration exists, ARC sets this value to <code>ENABLED</code>. If a you have not configured a practice run for the resource, or delete a practice run configuration, ARC sets the value to <code>DISABLED</code>.</p> <p>ARC updates this status; you can't set a practice run status to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedResourceSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_arc_zonal_shift.types.availability_zones

    out["availabilityZones"] = (
        capo_arc_zonal_shift.types.availability_zones.serialize_json(
            value["availability_zones"]
        )
    )
    if "applied_weights" in value:
        import capo_arc_zonal_shift.types.applied_weights

        out["appliedWeights"] = (
            capo_arc_zonal_shift.types.applied_weights.serialize_json(
                value["applied_weights"]
            )
        )
    if "zonal_shifts" in value:
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
    if "zonal_autoshift_status" in value:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["zonalAutoshiftStatus"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
                value["zonal_autoshift_status"]
            )
        )
    if "practice_run_status" in value:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["practiceRunStatus"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
                value["practice_run_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedResourceSummary:
    out: ManagedResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("availabilityZones") is not None:
        import capo_arc_zonal_shift.types.availability_zones

        out["availability_zones"] = (
            capo_arc_zonal_shift.types.availability_zones.deserialize_json(
                data["availabilityZones"]
            )
        )
    else:
        out["availability_zones"] = []
    if data.get("appliedWeights") is not None:
        import capo_arc_zonal_shift.types.applied_weights

        out["applied_weights"] = (
            capo_arc_zonal_shift.types.applied_weights.deserialize_json(
                data["appliedWeights"]
            )
        )
    if data.get("zonalShifts") is not None:
        import capo_arc_zonal_shift.types.zonal_shifts_in_resource

        out["zonal_shifts"] = (
            capo_arc_zonal_shift.types.zonal_shifts_in_resource.deserialize_json(
                data["zonalShifts"]
            )
        )
    if data.get("autoshifts") is not None:
        import capo_arc_zonal_shift.types.autoshifts_in_resource

        out["autoshifts"] = (
            capo_arc_zonal_shift.types.autoshifts_in_resource.deserialize_json(
                data["autoshifts"]
            )
        )
    if data.get("zonalAutoshiftStatus") is not None:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["zonal_autoshift_status"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["zonalAutoshiftStatus"]
            )
        )
    if data.get("practiceRunStatus") is not None:
        import capo_arc_zonal_shift.types.zonal_autoshift_status

        out["practice_run_status"] = (
            capo_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["practiceRunStatus"]
            )
        )
    return out
