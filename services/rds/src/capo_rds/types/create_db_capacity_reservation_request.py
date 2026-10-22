"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zones
    import capo_rds.types.db_capacity_reservation_name
    import capo_rds.types.db_instance_class
    import capo_rds.types.integer_optional
    import capo_rds.types.long_optional
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list


class CreateDBCapacityReservationRequest(TypedDict, closed=True):
    db_capacity_reservation_name: NotRequired[
        "capo_rds.types.db_capacity_reservation_name.DBCapacityReservationName"
    ]
    """<p>The name of the DB capacity reservation. This name must be unique for your Amazon Web Services account in the Amazon Web Services Region.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 lowercase letters, digits, or hyphens.</p> </li> <li> <p>First character must be a lowercase letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Can't contain more than 16 groups of characters separated by hyphens.</p> </li> <li> <p>Can't begin with <code>dbcr-</code>.</p> </li> </ul>"""
    db_instance_class: NotRequired["capo_rds.types.db_instance_class.DBInstanceClass"]
    """<p>The compute and memory capacity to reserve, for example <code>db.m5.large</code>. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB instance classes</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must be a DB instance class that the specified <code>Engine</code> supports.</p> </li> <li> <p>For RDS for Oracle with <code>LicenseModel</code> set to <code>license-included</code>, some DB instance classes aren't supported. Either choose a supported DB instance class, or set <code>LicenseModel</code> to <code>bring-your-own-license</code>.</p> </li> </ul>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to reserve capacity for.</p> <p>Valid Values: <code>aurora-mysql</code> | <code>aurora-postgresql</code> | <code>mysql</code> | <code>postgres</code> | <code>mariadb</code> | <code>oracle-ee</code> | <code>oracle-ee-cdb</code> | <code>oracle-se2</code> | <code>oracle-se2-cdb</code> | <code>sqlserver-ee</code> | <code>sqlserver-se</code> | <code>sqlserver-web</code> | <code>sqlserver-ex</code> | <code>sqlserver-dev-ee</code> | <code>sqlserver-dev-se</code> | <code>db2-ae</code> | <code>db2-ce</code> | <code>db2-se</code> </p> <note> <p>The Developer Edition engines <code>sqlserver-dev-ee</code> and <code>sqlserver-dev-se</code> support no Multi-AZ DB instance and no read replica. Therefore, a reservation for either engine serves Single-AZ DB instances only.</p> </note>"""
    capacity_per_availability_zone: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of DB instances to reserve in each Availability Zone that you list in <code>AvailabilityZones</code>. Amazon RDS reserves this number of DB instances in every listed Availability Zone.</p> <p>A Single-AZ DB instance uses one unit of reserved capacity, in one Availability Zone. A Multi-AZ DB instance is one DB instance, and it uses one unit of reserved capacity in each of two Availability Zones. Therefore, a Multi-AZ DB instance uses two units in total. A read replica uses one unit of reserved capacity, in the same way as any other DB instance.</p> <p>Amazon RDS reserves capacity in each Availability Zone separately. Reserved capacity in one Availability Zone can't serve a DB instance in another Availability Zone. A request for a DB instance fails when the Availability Zone of the DB instance has no available capacity.</p> <p>Therefore, set this value to the number of DB instances that you want to run at the same time in one Availability Zone. Don't set it to the number that you want in total.</p> <p>This value multiplied by the number of Availability Zones counts against the DB instances quota for your Amazon Web Services account in the Amazon Web Services Region. Your existing DB instances, and the unused capacity of your other reservations, count against the same quota.</p> <p>To find the value of the DB instances quota, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html">Quotas and constraints for Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Minimum 1.</p> </li> </ul>"""
    availability_zones: NotRequired[
        "capo_rds.types.availability_zones.AvailabilityZones"
    ]
    """<p>A list of Availability Zones for the reservation.</p> <p>You can't change the Availability Zones of a reservation after you create it. Reserved capacity in an Availability Zone that no DB instance uses stays unused.</p> <p>Constraints:</p> <ul> <li> <p>Must specify one or more Availability Zones.</p> </li> <li> <p>Each Availability Zone can appear only once.</p> </li> <li> <p>Each Availability Zone must be in the Amazon Web Services Region of the request.</p> </li> <li> <p>Each Availability Zone must have capacity for the requested DB instance class.</p> </li> <li> <p>Must include two or more Availability Zones to use the reservation for a Multi-AZ DB instance.</p> </li> <li> <p>A DB instance can use reserved capacity only in an Availability Zone that its DB subnet group covers.</p> </li> </ul> <p>Example: <code>us-east-1a</code> </p>"""
    end_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the reservation expires, in Universal Coordinated Time (UTC). If you don't specify a value, the reservation doesn't expire.</p> <p>To change the expiration of an existing reservation, use <code>ModifyDBCapacityReservation</code>. That operation takes <code>EndDateType</code> along with <code>EndDate</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be a date and time in the future.</p> </li> <li> <p>For a future-dated reservation, must be at or after <code>StartDate</code> plus <code>CommitmentDuration</code>. For example, a reservation that starts on 2026-12-01 with a 30-day commitment can't expire before 2026-12-31. To reserve capacity for one calendar month, set <code>CommitmentDuration</code> to 30 days or fewer, not to the length of the month.</p> </li> </ul> <p>Example: <code>2026-12-31T23:59:59Z</code> </p>"""
    start_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the reservation starts, in Universal Coordinated Time (UTC). Specify this parameter to create a future-dated reservation. If you don't specify a value, the reservation starts immediately.</p> <p>A reservation that starts later always carries a capacity commitment. Therefore, a request that specifies <code>StartDate</code> must also meet every constraint of a future-dated reservation, including the minimum reserved capacity in each Availability Zone.</p> <p>Constraints:</p> <ul> <li> <p>Must be from 5 to 120 days in the future.</p> </li> <li> <p>You must also specify <code>CommitmentDuration</code>.</p> </li> </ul> <p>Example: <code>2026-12-01T00:00:00Z</code> </p>"""
    commitment_duration: NotRequired["capo_rds.types.long_optional.LongOptional"]
    """<p>The length of the capacity commitment that you request for a future-dated reservation, in seconds. Amazon RDS measures this length from <code>StartDate</code>.</p> <note> <p>Amazon RDS can grant a shorter capacity commitment than you request. Therefore, read <code>CommitmentEndDate</code> in <code>CommitmentInfo</code> for the commitment that Amazon RDS granted.</p> </note> <p>The commitment doesn't end the reservation. Specify <code>EndDate</code> to set an expiration date. You can't cancel a reservation in the <code>active</code> state during the commitment.</p> <p>Constraints:</p> <ul> <li> <p>Minimum 1209600, which is 14 days. For a <code>db.x</code> DB instance class, such as <code>db.x2g.xlarge</code>, the minimum is 7257600, which is 84 days.</p> </li> <li> <p>Must be less than 315576000, which is 10 years.</p> </li> <li> <p>You must also specify <code>StartDate</code>.</p> </li> </ul> <p>Example: <code>2592000</code> </p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model to reserve capacity for. Specify this parameter only for RDS for Microsoft SQL Server Enterprise Edition, Standard Edition, and Developer Edition, for RDS for Oracle, or for RDS for Db2 Standard Edition and Advanced Edition. Amazon RDS rejects the request for any other engine. This includes Amazon Aurora, the Web and Express editions of RDS for Microsoft SQL Server, and RDS for Db2 Community Edition.</p> <p>Valid Values:</p> <ul> <li> <p>RDS for Microsoft SQL Server Enterprise Edition and Standard Edition - <code>license-included | bring-your-own-media</code> </p> </li> <li> <p>RDS for Microsoft SQL Server Developer Edition - <code>bring-your-own-license</code> </p> </li> <li> <p>RDS for Oracle - <code>bring-your-own-license | license-included</code> </p> </li> <li> <p>RDS for Db2 Standard Edition and Advanced Edition - <code>bring-your-own-license | marketplace-license</code> </p> </li> </ul> <p>A DB instance launches into the reservation only when the license model of the DB instance matches the license model of the reservation. For a reservation that holds no license model, Amazon RDS applies no license model check at launch.</p> <p>For RDS for Microsoft SQL Server Enterprise Edition and Standard Edition, if you don't specify a value, Amazon RDS uses <code>license-included</code>.</p> <p>For RDS for Microsoft SQL Server Developer Edition, if you don't specify a value, Amazon RDS uses <code>bring-your-own-license</code>. That is the only license model that these engines accept, and Amazon RDS rejects any other value.</p> <p>For RDS for Oracle, if you don't specify a value, Amazon RDS uses the only orderable license model for the DB instance class. If more than one license model is orderable, you must specify one.</p> <p>For RDS for Db2 Standard Edition and Advanced Edition, if you don't specify a value, Amazon RDS uses <code>bring-your-own-license</code>. To reserve capacity for Db2 DB instances that you license through Amazon Web Services Marketplace, specify <code>marketplace-license</code>.</p> <note> <p>For RDS for Oracle, the license models that you can reserve depend on the engine and the DB instance class. RDS for Oracle Enterprise Edition doesn't support <code>license-included</code>.</p> </note>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB capacity reservation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
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
    if "capacity_per_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityPerAvailabilityZone",
                str(value["capacity_per_availability_zone"]),
            )
        )
    if "availability_zones" in value:
        import capo_rds.types.availability_zones

        capo_rds.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "end_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "start_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "commitment_duration" in value:
        pairs.append(
            (f"{key_prefix}CommitmentDuration", str(value["commitment_duration"]))
        )
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBCapacityReservationRequest:
    out: CreateDBCapacityReservationRequest = {}  # type: ignore[typeddict-item]
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
    child_capacity_per_availability_zone = el.find("CapacityPerAvailabilityZone")
    if child_capacity_per_availability_zone is not None:
        out["capacity_per_availability_zone"] = int(
            child_capacity_per_availability_zone.text or ""
        )
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_rds.types.availability_zones

        out["availability_zones"] = capo_rds.types.availability_zones.deserialize_query(
            child_availability_zones
        )
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_rds.types.t_stamp

        out["end_date"] = capo_rds.types.t_stamp.deserialize_query(child_end_date)
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_rds.types.t_stamp

        out["start_date"] = capo_rds.types.t_stamp.deserialize_query(child_start_date)
    child_commitment_duration = el.find("CommitmentDuration")
    if child_commitment_duration is not None:
        out["commitment_duration"] = int(child_commitment_duration.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out
