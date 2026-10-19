"""Generated from Smithy shape ``com.amazonaws.workmail#PutInboundDmarcSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean_object
    import capo_workmail.types.organization_id


class PutInboundDmarcSettingsRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The ID of the organization that you are applying the DMARC policy to.</p>"""
    enforced: "capo_workmail.types.boolean_object.BooleanObject"
    """<p>Enforces or suspends a policy after it's applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInboundDmarcSettingsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Enforced"] = value["enforced"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInboundDmarcSettingsRequest:
    out: PutInboundDmarcSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Enforced") is not None:
        out["enforced"] = data["Enforced"]
    else:
        out["enforced"] = False
    return out
