"""Generated from Smithy shape ``com.amazonaws.workmail#CreateOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.directory_id
    import capo_workmail.types.domains
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.kms_key_arn
    import capo_workmail.types.organization_name


class CreateOrganizationRequest(TypedDict, closed=True):
    directory_id: NotRequired["capo_workmail.types.directory_id.DirectoryId"]
    """<p>The AWS Directory Service directory ID.</p>"""
    alias: "capo_workmail.types.organization_name.OrganizationName"
    """<p>The organization alias.</p>"""
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>The idempotency token associated with the request.</p>"""
    domains: NotRequired["capo_workmail.types.domains.Domains"]
    """<p>The email domains to associate with the organization.</p>"""
    kms_key_arn: NotRequired["capo_workmail.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of a customer managed key from AWS KMS.</p>"""
    enable_interoperability: NotRequired["capo_workmail.types.boolean.Boolean"]
    """<p>When <code>true</code>, allows organization interoperability between WorkMail and Microsoft Exchange. If <code>true</code>, you must include a AD Connector directory ID in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    out["Alias"] = value["alias"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "domains" in value:
        import capo_workmail.types.domains

        out["Domains"] = capo_workmail.types.domains.serialize_aws_json_1_1(
            value["domains"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "enable_interoperability" in value:
        out["EnableInteroperability"] = value["enable_interoperability"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationRequest:
    out: CreateOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Domains") is not None:
        import capo_workmail.types.domains

        out["domains"] = capo_workmail.types.domains.deserialize_aws_json_1_1(
            data["Domains"]
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("EnableInteroperability") is not None:
        out["enable_interoperability"] = data["EnableInteroperability"]
    return out
