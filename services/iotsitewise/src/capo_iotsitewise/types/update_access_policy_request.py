"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.identity
    import capo_iotsitewise.types.permission
    import capo_iotsitewise.types.resource


class UpdateAccessPolicyRequest(TypedDict, closed=True):
    access_policy_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    access_policy_identity: "capo_iotsitewise.types.identity.Identity"
    """<p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>"""
    access_policy_resource: "capo_iotsitewise.types.resource.Resource"
    """<p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>"""
    access_policy_permission: "capo_iotsitewise.types.permission.Permission"
    """<p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessPolicyRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.identity

    out["accessPolicyIdentity"] = capo_iotsitewise.types.identity.serialize_json(
        value["access_policy_identity"]
    )
    import capo_iotsitewise.types.resource

    out["accessPolicyResource"] = capo_iotsitewise.types.resource.serialize_json(
        value["access_policy_resource"]
    )
    import capo_iotsitewise.types.permission

    out["accessPolicyPermission"] = capo_iotsitewise.types.permission.serialize_json(
        value["access_policy_permission"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAccessPolicyRequest:
    out: UpdateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("accessPolicyIdentity") is not None:
        import capo_iotsitewise.types.identity

        out["access_policy_identity"] = (
            capo_iotsitewise.types.identity.deserialize_json(
                data["accessPolicyIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccessPolicyRequest.access_policy_identity required"
        )
    if data.get("accessPolicyResource") is not None:
        import capo_iotsitewise.types.resource

        out["access_policy_resource"] = (
            capo_iotsitewise.types.resource.deserialize_json(
                data["accessPolicyResource"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccessPolicyRequest.access_policy_resource required"
        )
    if data.get("accessPolicyPermission") is not None:
        import capo_iotsitewise.types.permission

        out["access_policy_permission"] = (
            capo_iotsitewise.types.permission.deserialize_json(
                data["accessPolicyPermission"]
            )
        )
    else:
        import typing

        out["access_policy_permission"] = typing.cast(
            "capo_iotsitewise.types.permission.Permission", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
