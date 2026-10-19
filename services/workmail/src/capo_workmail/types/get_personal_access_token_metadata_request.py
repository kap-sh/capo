"""Generated from Smithy shape ``com.amazonaws.workmail#GetPersonalAccessTokenMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.organization_id
    import capo_workmail.types.personal_access_token_id


class GetPersonalAccessTokenMetadataRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p> The Organization ID. </p>"""
    personal_access_token_id: (
        "capo_workmail.types.personal_access_token_id.PersonalAccessTokenId"
    )
    """<p> The Personal Access Token ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPersonalAccessTokenMetadataRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["PersonalAccessTokenId"] = value["personal_access_token_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPersonalAccessTokenMetadataRequest:
    out: GetPersonalAccessTokenMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("PersonalAccessTokenId") is not None:
        out["personal_access_token_id"] = data["PersonalAccessTokenId"]
    else:
        out["personal_access_token_id"] = ""
    return out
