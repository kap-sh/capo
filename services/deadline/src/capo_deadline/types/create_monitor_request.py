"""Generated from Smithy shape ``com.amazonaws.deadline#CreateMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.identity_center_instance_arn
    import capo_deadline.types.region
    import capo_deadline.types.resource_name
    import capo_deadline.types.subdomain
    import capo_deadline.types.tags


class CreateMonitorRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    identity_center_instance_arn: (
        "capo_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    )
    """<p>The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.</p>"""
    identity_center_region: NotRequired["capo_deadline.types.region.Region"]
    """<p>The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.</p>"""
    subdomain: "capo_deadline.types.subdomain.Subdomain"
    """<p>The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>"""
    role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.</p>"""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """<p>The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "identity_center_region" in value:
        out["identityCenterRegion"] = value["identity_center_region"]
    out["subdomain"] = value["subdomain"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMonitorRequest:
    out: CreateMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("identityCenterInstanceArn") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    else:
        out["identity_center_instance_arn"] = ""
    if data.get("identityCenterRegion") is not None:
        out["identity_center_region"] = data["identityCenterRegion"]
    if data.get("subdomain") is not None:
        out["subdomain"] = data["subdomain"]
    else:
        out["subdomain"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out
