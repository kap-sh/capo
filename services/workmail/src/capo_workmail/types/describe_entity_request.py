"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.organization_id


class DescribeEntityRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the entity exists.</p>"""
    email: "capo_workmail.types.email_address.EmailAddress"
    """<p>The email under which the entity exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityRequest:
    out: DescribeEntityRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        out["email"] = ""
    return out
