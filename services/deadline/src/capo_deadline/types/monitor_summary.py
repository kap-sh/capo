"""Generated from Smithy shape ``com.amazonaws.deadline#MonitorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.identity_center_application_arn
    import capo_deadline.types.identity_center_instance_arn
    import capo_deadline.types.monitor_id
    import capo_deadline.types.region
    import capo_deadline.types.resource_name
    import capo_deadline.types.subdomain
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.url


class MonitorSummary(TypedDict, closed=True):
    monitor_id: "capo_deadline.types.monitor_id.MonitorId"
    """<p>The unique identifier for the monitor.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The name of the monitor that displays on the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    subdomain: "capo_deadline.types.subdomain.Subdomain"
    """<p>The subdomain used for the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    url: "capo_deadline.types.url.Url"
    """<p>The complete URL of the monitor. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name of the IAM role for the monitor. Users of the monitor use this role to access Deadline Cloud resources.</p>"""
    identity_center_instance_arn: (
        "capo_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    )
    """<p>The Amazon Resource Name of the IAM Identity Center instance responsible for authenticating monitor users.</p>"""
    identity_center_region: NotRequired["capo_deadline.types.region.Region"]
    """<p>The Region where IAM Identity Center is enabled.</p>"""
    identity_center_application_arn: "capo_deadline.types.identity_center_application_arn.IdentityCenterApplicationArn"
    """<p>The Amazon Resource Name that the IAM Identity Center assigned to the monitor when it was created.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The UNIX timestamp of the date and time that the monitor was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user name of the person that created the monitor.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The UNIX timestamp of the date and time that the monitor was last updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user name of the person that last updated the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorSummary) -> dict:
    out: dict = {}
    out["monitorId"] = value["monitor_id"]
    out["displayName"] = value["display_name"]
    out["subdomain"] = value["subdomain"]
    out["url"] = value["url"]
    out["roleArn"] = value["role_arn"]
    out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> MonitorSummary:
    out: MonitorSummary = {}  # type: ignore[typeddict-item]
    if data.get("monitorId") is not None:
        out["monitor_id"] = data["monitorId"]
    else:
        out["monitor_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("subdomain") is not None:
        out["subdomain"] = data["subdomain"]
    else:
        out["subdomain"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("identityCenterInstanceArn") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    else:
        out["identity_center_instance_arn"] = ""
    if data.get("identityCenterRegion") is not None:
        out["identity_center_region"] = data["identityCenterRegion"]
    if data.get("identityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    else:
        out["identity_center_application_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    return out
