"""Generated from Smithy shape ``com.amazonaws.rds#DBCapacityReservationCommitmentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.t_stamp


class DBCapacityReservationCommitmentInfo(TypedDict, closed=True):
    committed_capacity_per_availability_zone: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of DB instances that Amazon RDS holds in each Availability Zone of the reservation for the length of the commitment.</p>"""
    commitment_end_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the commitment ends, in Universal Coordinated Time (UTC). This date reports the capacity commitment that Amazon RDS granted.</p> <p>Amazon RDS can grant a shorter capacity commitment than you request in <code>CommitmentDuration</code>. Therefore, this date can fall earlier than <code>StartDate</code> plus <code>CommitmentDuration</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBCapacityReservationCommitmentInfo,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "committed_capacity_per_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}CommittedCapacityPerAvailabilityZone",
                str(value["committed_capacity_per_availability_zone"]),
            )
        )
    if "commitment_end_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["commitment_end_date"], pairs, f"{key_prefix}CommitmentEndDate"
        )


def deserialize_query(el: Element) -> DBCapacityReservationCommitmentInfo:
    out: DBCapacityReservationCommitmentInfo = {}  # type: ignore[typeddict-item]
    child_committed_capacity_per_availability_zone = el.find(
        "CommittedCapacityPerAvailabilityZone"
    )
    if child_committed_capacity_per_availability_zone is not None:
        out["committed_capacity_per_availability_zone"] = int(
            child_committed_capacity_per_availability_zone.text or ""
        )
    child_commitment_end_date = el.find("CommitmentEndDate")
    if child_commitment_end_date is not None:
        import capo_rds.types.t_stamp

        out["commitment_end_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_commitment_end_date
        )
    return out
