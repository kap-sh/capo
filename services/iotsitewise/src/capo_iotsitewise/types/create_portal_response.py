"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreatePortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.portal_status
    import capo_iotsitewise.types.sso_application_id
    import capo_iotsitewise.types.url


class CreatePortalResponse(TypedDict, closed=True):
    portal_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the created portal.</p>"""
    portal_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the portal, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}</code> </p>"""
    portal_start_url: "capo_iotsitewise.types.url.Url"
    """<p>The URL for the IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the IoT SiteWise console to get a URL that you can use to access the portal.</p>"""
    portal_status: "capo_iotsitewise.types.portal_status.PortalStatus"
    """<p>The status of the portal, which contains a state (<code>CREATING</code> after successfully calling this operation) and any error message.</p>"""
    sso_application_id: "capo_iotsitewise.types.sso_application_id.SSOApplicationId"
    """<p>The associated IAM Identity Center application ID, if the portal uses IAM Identity Center.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalResponse) -> dict:
    out: dict = {}
    out["portalId"] = value["portal_id"]
    out["portalArn"] = value["portal_arn"]
    out["portalStartUrl"] = value["portal_start_url"]
    import capo_iotsitewise.types.portal_status

    out["portalStatus"] = capo_iotsitewise.types.portal_status.serialize_json(
        value["portal_status"]
    )
    out["ssoApplicationId"] = value["sso_application_id"]
    return out


def deserialize_json(data: dict) -> CreatePortalResponse:
    out: CreatePortalResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalId") is not None:
        out["portal_id"] = data["portalId"]
    else:
        raise DeserializationError("CreatePortalResponse.portal_id required")
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("CreatePortalResponse.portal_arn required")
    if data.get("portalStartUrl") is not None:
        out["portal_start_url"] = data["portalStartUrl"]
    else:
        raise DeserializationError("CreatePortalResponse.portal_start_url required")
    if data.get("portalStatus") is not None:
        import capo_iotsitewise.types.portal_status

        out["portal_status"] = capo_iotsitewise.types.portal_status.deserialize_json(
            data["portalStatus"]
        )
    else:
        raise DeserializationError("CreatePortalResponse.portal_status required")
    if data.get("ssoApplicationId") is not None:
        out["sso_application_id"] = data["ssoApplicationId"]
    else:
        raise DeserializationError("CreatePortalResponse.sso_application_id required")
    return out
