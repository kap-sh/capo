"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.organization_id


class DeleteOrganizationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>The idempotency token associated with the request.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    delete_directory: "capo_workmail.types.boolean.Boolean"
    """<p>If true, deletes the AWS Directory Service directory associated with the organization.</p>"""
    force_delete: NotRequired["capo_workmail.types.boolean.Boolean"]
    """<p>Deletes a WorkMail organization even if the organization has enabled users.</p>"""
    delete_identity_center_application: NotRequired[
        "capo_workmail.types.boolean.Boolean"
    ]
    """<p>Deletes IAM Identity Center application for WorkMail. This action does not affect authentication settings for any organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DeleteDirectory"] = value["delete_directory"]
    if "force_delete" in value:
        out["ForceDelete"] = value["force_delete"]
    if "delete_identity_center_application" in value:
        out["DeleteIdentityCenterApplication"] = value[
            "delete_identity_center_application"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationRequest:
    out: DeleteOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("DeleteOrganizationRequest.organization_id required")
    if data.get("DeleteDirectory") is not None:
        out["delete_directory"] = data["DeleteDirectory"]
    else:
        raise DeserializationError(
            "DeleteOrganizationRequest.delete_directory required"
        )
    if data.get("ForceDelete") is not None:
        out["force_delete"] = data["ForceDelete"]
    if data.get("DeleteIdentityCenterApplication") is not None:
        out["delete_identity_center_application"] = data[
            "DeleteIdentityCenterApplication"
        ]
    return out
