"""Generated from Smithy shape ``com.amazonaws.accountaccess#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.date_time


class ApplicationSummary(TypedDict, closed=True):
    application_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>The ARN of the application.</p>"""
    tenant_id: NotRequired["str"]
    """<p>The tenant identifier associated with the application.</p>"""
    created_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the application was created.</p>"""
    updated_at: "capo_account_access.types.date_time.DateTime"
    """<p>The date and time when the application was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
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
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    if data.get("createdAt") is not None:
        import capo_account_access.types.date_time

        out["created_at"] = capo_account_access.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_account_access.types.date_time

        out["updated_at"] = capo_account_access.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
