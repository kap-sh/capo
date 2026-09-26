"""Generated from Smithy shape ``com.amazonaws.accountaccess#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.date_time
    import capo_account_access.types.error_details
    import capo_account_access.types.identity_source_details
    import capo_account_access.types.status
    import capo_account_access.types.tags_map


class GetApplicationResponse(TypedDict, closed=True):
    identity_source: (
        "capo_account_access.types.identity_source_details.IdentitySourceDetails"
    )
    """<p>The identity source details for the application, including the IAM Identity Center instance configuration.</p>"""
    status: "capo_account_access.types.status.Status"
    """<p>The current status of the application.</p>"""
    tenant_id: NotRequired["str"]
    """<p>The tenant identifier associated with the application.</p>"""
    created_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the application was created.</p>"""
    updated_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the application was last updated.</p>"""
    tags: NotRequired["capo_account_access.types.tags_map.TagsMap"]
    """<p>The tags associated with the application.</p>"""
    error: NotRequired["capo_account_access.types.error_details.ErrorDetails"]
    """<p>The error details if the application is in a failed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    import capo_account_access.types.identity_source_details

    out["identitySource"] = (
        capo_account_access.types.identity_source_details.serialize_json(
            value["identity_source"]
        )
    )
    import capo_account_access.types.status

    out["status"] = capo_account_access.types.status.serialize_json(value["status"])
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    import capo_account_access.types.date_time

    out["createdAt"] = capo_account_access.types.date_time.serialize_json(
        value["created_at"]
    )
    import capo_account_access.types.date_time

    out["updatedAt"] = capo_account_access.types.date_time.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import capo_account_access.types.tags_map

        out["tags"] = capo_account_access.types.tags_map.serialize_json(value["tags"])
    if "error" in value:
        import capo_account_access.types.error_details

        out["error"] = capo_account_access.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("identitySource") is not None:
        import capo_account_access.types.identity_source_details

        out["identity_source"] = (
            capo_account_access.types.identity_source_details.deserialize_json(
                data["identitySource"]
            )
        )
    else:
        raise DeserializationError("GetApplicationResponse.identity_source required")
    if data.get("status") is not None:
        import capo_account_access.types.status

        out["status"] = capo_account_access.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetApplicationResponse.status required")
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    if data.get("createdAt") is not None:
        import capo_account_access.types.date_time

        out["created_at"] = capo_account_access.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetApplicationResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_account_access.types.date_time

        out["updated_at"] = capo_account_access.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetApplicationResponse.updated_at required")
    if data.get("tags") is not None:
        import capo_account_access.types.tags_map

        out["tags"] = capo_account_access.types.tags_map.deserialize_json(data["tags"])
    if data.get("error") is not None:
        import capo_account_access.types.error_details

        out["error"] = capo_account_access.types.error_details.deserialize_json(
            data["error"]
        )
    return out
