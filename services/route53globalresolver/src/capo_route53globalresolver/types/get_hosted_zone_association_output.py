"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetHostedZoneAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.hosted_zone_association_status
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.hosted_zone_name
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class GetHostedZoneAssociationOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the private hosted zone association.</p>"""
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the DNS view the private hosted zone is associated to.</p>"""
    hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>ID of the hosted zone associated to the DNS view.</p>"""
    hosted_zone_name: "capo_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    """<p>Name of the domain associated with the private hosted zone.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the private hosted zone association.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the private hosted zone association was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the private hosted zone association was updated.</p>"""
    status: "capo_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>The operational status of the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHostedZoneAssociationOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["resourceArn"] = value["resource_arn"]
    out["hostedZoneId"] = value["hosted_zone_id"]
    out["hostedZoneName"] = value["hosted_zone_name"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.hosted_zone_association_status

    out["status"] = (
        capo_route53globalresolver.types.hosted_zone_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetHostedZoneAssociationOutput:
    out: GetHostedZoneAssociationOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("hostedZoneId") is not None:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        out["hosted_zone_id"] = ""
    if data.get("hostedZoneName") is not None:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        out["hosted_zone_name"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            capo_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus",
            "",
        )
    return out
