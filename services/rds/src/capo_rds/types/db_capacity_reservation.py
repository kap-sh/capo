"""Generated from Smithy shape ``com.amazonaws.rds#DBCapacityReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.available_capacity_per_availability_zone_list
    import capo_rds.types.db_capacity_reservation_commitment_info
    import capo_rds.types.db_capacity_reservation_identifier
    import capo_rds.types.db_capacity_reservation_name
    import capo_rds.types.db_capacity_reservation_state
    import capo_rds.types.db_instance_class
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class DBCapacityReservation(TypedDict, closed=True):
    db_capacity_reservation_name: NotRequired[
        "capo_rds.types.db_capacity_reservation_name.DBCapacityReservationName"
    ]
    """<p>The name that you specified for the DB capacity reservation.</p>"""
    db_instance_class: NotRequired["capo_rds.types.db_instance_class.DBInstanceClass"]
    """<p>The DB instance class for the reserved capacity. You specify this value when you create the reservation, and you can't change it afterward.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine for the reserved capacity. You specify this value when you create the reservation, and you can't change it afterward.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model for the reserved capacity. Amazon RDS returns this value only for a reservation that reserves capacity for a specific license model. Amazon RDS doesn't return this value for a reservation whose database engine doesn't support a license model.</p> <p>A DB instance launches into the reservation only when the license model of the DB instance matches this value. For a reservation that holds no license model, Amazon RDS applies no license model check at launch.</p> <p>Valid Values:</p> <ul> <li> <p>RDS for Microsoft SQL Server Enterprise Edition and Standard Edition - <code>license-included | bring-your-own-media</code> </p> </li> <li> <p>RDS for Microsoft SQL Server Developer Edition - <code>bring-your-own-license</code> </p> </li> <li> <p>RDS for Oracle - <code>bring-your-own-license | license-included</code> </p> </li> <li> <p>RDS for Db2 Standard Edition and Advanced Edition - <code>bring-your-own-license | marketplace-license</code> </p> </li> </ul> <p>For RDS for Db2 Standard Edition and Advanced Edition, a reservation created without a license model holds <code>bring-your-own-license</code>.</p>"""
    reserved_capacity_per_availability_zone: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of DB instances that Amazon RDS reserves in each Availability Zone of the reservation. This value matches the <code>CapacityPerAvailabilityZone</code> parameter of the request. The total reserved capacity is this value multiplied by the number of Availability Zones of the reservation.</p>"""
    available_capacity_per_availability_zone_list: NotRequired[
        "capo_rds.types.available_capacity_per_availability_zone_list.AvailableCapacityPerAvailabilityZoneList"
    ]
    """<p>The unused capacity of the reservation, reported for each Availability Zone of the reservation. Each entry names one Availability Zone, and it reports the number of DB instances that remain available in that Availability Zone.</p> <p>Amazon RDS reports available capacity only for a reservation that is in the <code>active</code> state and not past its end date. Otherwise, each entry reports an available capacity of <code>0</code>. A future-dated reservation that hasn't started reports <code>0</code>, and a reservation that Amazon RDS is modifying reports <code>0</code>.</p> <p>A reservation reports the <code>pending</code> state while Amazon RDS modifies it. Therefore, a reservation in the <code>active</code> state that reports no available capacity has no unused capacity.</p>"""
    end_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the reservation expires, in Universal Coordinated Time (UTC). Amazon RDS doesn't return this value if the reservation doesn't expire.</p> <important> <p>A DB instance that uses the reservation keeps running after the reservation expires. It continues on unreserved capacity, and Amazon RDS doesn't stop it or modify it. However, Amazon RDS no longer reserves capacity for the DB instance. Amazon RDS might later move the DB instance to different hardware, for example during hardware maintenance. That move can fail when the Amazon Web Services Region has insufficient capacity for the DB instance class.</p> </important>"""
    create_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the reservation was created, in Universal Coordinated Time (UTC).</p>"""
    start_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when a future-dated reservation starts, in Universal Coordinated Time (UTC). Amazon RDS doesn't return this value for a reservation that started immediately.</p>"""
    commitment_info: NotRequired[
        "capo_rds.types.db_capacity_reservation_commitment_info.DBCapacityReservationCommitmentInfo"
    ]
    """<p>The capacity commitment of the reservation. Amazon RDS returns this object only for a future-dated reservation.</p>"""
    state: NotRequired[
        "capo_rds.types.db_capacity_reservation_state.DBCapacityReservationState"
    ]
    """<p>The current state of the DB capacity reservation. A DB instance can use the reservation in the <code>active</code> state only.</p> <p>Valid Values:</p> <ul> <li> <p> <code>active</code> - Amazon RDS holds the reserved capacity, and a DB instance can use it.</p> </li> <li> <p> <code>pending</code> - The reservation isn't ready to use yet. Amazon RDS is creating the reserved capacity, or it is applying a requested modification.</p> </li> <li> <p> <code>assessing</code> - Amazon RDS is evaluating the request for a future-dated reservation.</p> </li> <li> <p> <code>scheduled</code> - Amazon RDS accepted a future-dated reservation, and the reservation is waiting for its start date.</p> </li> <li> <p> <code>delayed</code> - Amazon RDS couldn't provide the reserved capacity of a future-dated reservation by its start date.</p> </li> <li> <p> <code>unsupported</code> - Amazon RDS can't fulfill the future-dated reservation as requested.</p> </li> <li> <p> <code>expired</code> - The reservation passed its end date. Amazon RDS releases the reserved capacity.</p> </li> <li> <p> <code>cancelled</code> - You cancelled the reservation, and Amazon RDS released the reserved capacity.</p> </li> <li> <p> <code>failed</code> - Amazon RDS couldn't reserve the capacity.</p> </li> </ul> <p>The values <code>assessing</code>, <code>scheduled</code>, <code>delayed</code>, and <code>unsupported</code> apply to a future-dated reservation only.</p>"""
    db_capacity_reservation_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the DB capacity reservation.</p>"""
    db_capacity_reservation_identifier: NotRequired[
        "capo_rds.types.db_capacity_reservation_identifier.DBCapacityReservationIdentifier"
    ]
    """<p>The unique identifier of the DB capacity reservation. The identifier has the prefix <code>dbcr-</code>. Every other DB capacity reservation operation takes this identifier.</p>"""
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>The tags associated with the DB capacity reservation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBCapacityReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_capacity_reservation_name" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationName",
                str(value["db_capacity_reservation_name"]),
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "reserved_capacity_per_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedCapacityPerAvailabilityZone",
                str(value["reserved_capacity_per_availability_zone"]),
            )
        )
    if "available_capacity_per_availability_zone_list" in value:
        import capo_rds.types.available_capacity_per_availability_zone_list

        capo_rds.types.available_capacity_per_availability_zone_list.serialize_query(
            value["available_capacity_per_availability_zone_list"],
            pairs,
            f"{key_prefix}AvailableCapacityPerAvailabilityZoneList",
        )
    if "end_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "create_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "start_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "commitment_info" in value:
        import capo_rds.types.db_capacity_reservation_commitment_info

        capo_rds.types.db_capacity_reservation_commitment_info.serialize_query(
            value["commitment_info"], pairs, f"{key_prefix}CommitmentInfo"
        )
    if "state" in value:
        import capo_rds.types.db_capacity_reservation_state

        capo_rds.types.db_capacity_reservation_state.serialize_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "db_capacity_reservation_arn" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationArn",
                str(value["db_capacity_reservation_arn"]),
            )
        )
    if "db_capacity_reservation_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBCapacityReservationIdentifier",
                str(value["db_capacity_reservation_identifier"]),
            )
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> DBCapacityReservation:
    out: DBCapacityReservation = {}  # type: ignore[typeddict-item]
    child_db_capacity_reservation_name = el.find("DBCapacityReservationName")
    if child_db_capacity_reservation_name is not None:
        out["db_capacity_reservation_name"] = str(
            child_db_capacity_reservation_name.text or ""
        )
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_reserved_capacity_per_availability_zone = el.find(
        "ReservedCapacityPerAvailabilityZone"
    )
    if child_reserved_capacity_per_availability_zone is not None:
        out["reserved_capacity_per_availability_zone"] = int(
            child_reserved_capacity_per_availability_zone.text or ""
        )
    child_available_capacity_per_availability_zone_list = el.find(
        "AvailableCapacityPerAvailabilityZoneList"
    )
    if child_available_capacity_per_availability_zone_list is not None:
        import capo_rds.types.available_capacity_per_availability_zone_list

        out["available_capacity_per_availability_zone_list"] = (
            capo_rds.types.available_capacity_per_availability_zone_list.deserialize_query(
                child_available_capacity_per_availability_zone_list
            )
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_rds.types.t_stamp

        out["end_date"] = capo_rds.types.t_stamp.deserialize_query(child_end_date)
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import capo_rds.types.t_stamp

        out["create_date"] = capo_rds.types.t_stamp.deserialize_query(child_create_date)
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_rds.types.t_stamp

        out["start_date"] = capo_rds.types.t_stamp.deserialize_query(child_start_date)
    child_commitment_info = el.find("CommitmentInfo")
    if child_commitment_info is not None:
        import capo_rds.types.db_capacity_reservation_commitment_info

        out["commitment_info"] = (
            capo_rds.types.db_capacity_reservation_commitment_info.deserialize_query(
                child_commitment_info
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_rds.types.db_capacity_reservation_state

        out["state"] = capo_rds.types.db_capacity_reservation_state.deserialize_query(
            child_state
        )
    child_db_capacity_reservation_arn = el.find("DBCapacityReservationArn")
    if child_db_capacity_reservation_arn is not None:
        out["db_capacity_reservation_arn"] = str(
            child_db_capacity_reservation_arn.text or ""
        )
    child_db_capacity_reservation_identifier = el.find(
        "DBCapacityReservationIdentifier"
    )
    if child_db_capacity_reservation_identifier is not None:
        out["db_capacity_reservation_identifier"] = str(
            child_db_capacity_reservation_identifier.text or ""
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out
