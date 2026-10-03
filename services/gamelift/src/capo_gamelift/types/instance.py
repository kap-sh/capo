"""Generated from Smithy shape ``com.amazonaws.gamelift#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.dns_name
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.fleet_arn
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.instance_id
    import capo_gamelift.types.instance_status
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.operating_system
    import capo_gamelift.types.timestamp


class Instance(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that the instance belongs to.</p>"""
    fleet_arn: NotRequired["capo_gamelift.types.fleet_arn.FleetArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the instance.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>IP address that is assigned to the instance.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name.DnsName"]
    """<p>The DNS identifier assigned to the instance that is running the game session. Values have the following format:</p> <ul> <li> <p>TLS-enabled fleets: <code><unique identifier>.<region identifier>.amazongamelift.com</code>.</p> </li> <li> <p>Non-TLS-enabled fleets: <code>ec2-<unique identifier>.compute.amazonaws.com</code>. (See <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#concepts-public-addresses">Amazon EC2 Instance IP Addressing</a>.)</p> </li> </ul> <p>When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.</p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>Operating system that is running on this EC2 instance. </p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    type: NotRequired["capo_gamelift.types.ec2_instance_type.EC2InstanceType"]
    """<p>EC2 instance type that defines the computing resources of this instance. </p>"""
    status: NotRequired["capo_gamelift.types.instance_status.InstanceStatus"]
    """<p>Current status of the instance. Possible statuses include the following:</p> <ul> <li> <p> <b>PENDING</b> -- The instance is in the process of being created and launching server processes as defined in the fleet's run-time configuration. </p> </li> <li> <p> <b>ACTIVE</b> -- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift Servers that it is ready to host a game session. The instance is now considered ready to host game sessions. </p> </li> <li> <p> <b>TERMINATING</b> -- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem.</p> </li> </ul>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location of the instance, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "operating_system" in value:
        import capo_gamelift.types.operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["Type"] = capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_gamelift.types.instance_status

        out["Status"] = capo_gamelift.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("FleetArn") is not None:
        out["fleet_arn"] = data["FleetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.operating_system

        out["operating_system"] = (
            capo_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("Type") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["type"] = capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Status") is not None:
        import capo_gamelift.types.instance_status

        out["status"] = capo_gamelift.types.instance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
