"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class DescribeResourceRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization for which the resource is described.</p>"""
    resource_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the resource to be described.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceRequest:
    out: DescribeResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
