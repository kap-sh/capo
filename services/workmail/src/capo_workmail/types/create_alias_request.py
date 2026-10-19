"""Generated from Smithy shape ``com.amazonaws.workmail#CreateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_identifier


class CreateAliasRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization under which the member (user or group) exists.</p>"""
    entity_id: "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    """<p>The member (user or group) to which this alias is added.</p>"""
    alias: "capo_workmail.types.email_address.EmailAddress"
    """<p>The alias to add to the member set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["Alias"] = value["alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasRequest:
    out: CreateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    return out
