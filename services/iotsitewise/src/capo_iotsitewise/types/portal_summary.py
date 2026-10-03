"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.iam_arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.portal_status
    import capo_iotsitewise.types.portal_type
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.url


class PortalSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the portal.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the portal.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The portal's description.</p>"""
    start_url: "capo_iotsitewise.types.url.Url"
    """<p>The URL for the IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the IoT SiteWise console to get a URL that you can use to access the portal.</p>"""
    creation_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the portal was created, in Unix epoch time.</p>"""
    last_update_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the portal was last updated, in Unix epoch time.</p>"""
    role_arn: NotRequired["capo_iotsitewise.types.iam_arn.IamArn"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    status: "capo_iotsitewise.types.portal_status.PortalStatus"
    portal_type: NotRequired["capo_iotsitewise.types.portal_type.PortalType"]
    """<p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["startUrl"] = value["start_url"]
    if "creation_date" in value:
        import capo_iotsitewise.types.timestamp

        out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import capo_iotsitewise.types.timestamp

        out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["last_update_date"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    import capo_iotsitewise.types.portal_status

    out["status"] = capo_iotsitewise.types.portal_status.serialize_json(value["status"])
    if "portal_type" in value:
        import capo_iotsitewise.types.portal_type

        out["portalType"] = capo_iotsitewise.types.portal_type.serialize_json(
            value["portal_type"]
        )
    return out


def deserialize_json(data: dict) -> PortalSummary:
    out: PortalSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PortalSummary.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PortalSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("startUrl") is not None:
        out["start_url"] = data["startUrl"]
    else:
        raise DeserializationError("PortalSummary.start_url required")
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("status") is not None:
        import capo_iotsitewise.types.portal_status

        out["status"] = capo_iotsitewise.types.portal_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("PortalSummary.status required")
    if data.get("portalType") is not None:
        import capo_iotsitewise.types.portal_type

        out["portal_type"] = capo_iotsitewise.types.portal_type.deserialize_json(
            data["portalType"]
        )
    return out
