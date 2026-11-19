"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunEffectivePolicyValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.disaster_recovery_source
    import capo_resiliencehubv2.types.slo_source
    import capo_resiliencehubv2.types.target_source


class TestRunEffectivePolicyValues(TypedDict, closed=True):
    availability_slo: NotRequired["capo_resiliencehubv2.types.slo_source.SloSource"]
    """<p>The effective availability SLO value for the test run.</p>"""
    multi_az_rto: NotRequired["capo_resiliencehubv2.types.target_source.TargetSource"]
    """<p>The effective multi-AZ RTO value for the test run, in minutes.</p>"""
    multi_az_rpo: NotRequired["capo_resiliencehubv2.types.target_source.TargetSource"]
    """<p>The effective multi-AZ RPO value for the test run, in minutes.</p>"""
    multi_az_dr_approach: NotRequired[
        "capo_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-Availability Zone (AZ) disaster recovery approach for the test run.</p>"""
    multi_region_rto: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RTO value for the test run, in minutes.</p>"""
    multi_region_rpo: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective multi-Region RPO value for the test run, in minutes.</p>"""
    multi_region_dr_approach: NotRequired[
        "capo_resiliencehubv2.types.disaster_recovery_source.DisasterRecoverySource"
    ]
    """<p>The effective multi-Region disaster recovery approach for the test run.</p>"""
    data_recovery_time_between_backups: NotRequired[
        "capo_resiliencehubv2.types.target_source.TargetSource"
    ]
    """<p>The effective data recovery time between backups value for the test run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunEffectivePolicyValues) -> dict:
    out: dict = {}
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.slo_source

        out["availabilitySlo"] = capo_resiliencehubv2.types.slo_source.serialize_json(
            value["availability_slo"]
        )
    if "multi_az_rto" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiAzRto"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rto"]
        )
    if "multi_az_rpo" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiAzRpo"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_az_rpo"]
        )
    if "multi_az_dr_approach" in value:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multiAzDrApproach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_az_dr_approach"]
            )
        )
    if "multi_region_rto" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiRegionRto"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_region_rto"]
        )
    if "multi_region_rpo" in value:
        import capo_resiliencehubv2.types.target_source

        out["multiRegionRpo"] = capo_resiliencehubv2.types.target_source.serialize_json(
            value["multi_region_rpo"]
        )
    if "multi_region_dr_approach" in value:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multiRegionDrApproach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.serialize_json(
                value["multi_region_dr_approach"]
            )
        )
    if "data_recovery_time_between_backups" in value:
        import capo_resiliencehubv2.types.target_source

        out["dataRecoveryTimeBetweenBackups"] = (
            capo_resiliencehubv2.types.target_source.serialize_json(
                value["data_recovery_time_between_backups"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRunEffectivePolicyValues:
    out: TestRunEffectivePolicyValues = {}  # type: ignore[typeddict-item]
    if data.get("availabilitySlo") is not None:
        import capo_resiliencehubv2.types.slo_source

        out["availability_slo"] = (
            capo_resiliencehubv2.types.slo_source.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if data.get("multiAzRto") is not None:
        import capo_resiliencehubv2.types.target_source

        out["multi_az_rto"] = capo_resiliencehubv2.types.target_source.deserialize_json(
            data["multiAzRto"]
        )
    if data.get("multiAzRpo") is not None:
        import capo_resiliencehubv2.types.target_source

        out["multi_az_rpo"] = capo_resiliencehubv2.types.target_source.deserialize_json(
            data["multiAzRpo"]
        )
    if data.get("multiAzDrApproach") is not None:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multi_az_dr_approach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiAzDrApproach"]
            )
        )
    if data.get("multiRegionRto") is not None:
        import capo_resiliencehubv2.types.target_source

        out["multi_region_rto"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRto"]
            )
        )
    if data.get("multiRegionRpo") is not None:
        import capo_resiliencehubv2.types.target_source

        out["multi_region_rpo"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["multiRegionRpo"]
            )
        )
    if data.get("multiRegionDrApproach") is not None:
        import capo_resiliencehubv2.types.disaster_recovery_source

        out["multi_region_dr_approach"] = (
            capo_resiliencehubv2.types.disaster_recovery_source.deserialize_json(
                data["multiRegionDrApproach"]
            )
        )
    if data.get("dataRecoveryTimeBetweenBackups") is not None:
        import capo_resiliencehubv2.types.target_source

        out["data_recovery_time_between_backups"] = (
            capo_resiliencehubv2.types.target_source.deserialize_json(
                data["dataRecoveryTimeBetweenBackups"]
            )
        )
    return out
