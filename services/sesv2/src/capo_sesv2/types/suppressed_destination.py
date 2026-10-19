"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.suppressed_destination_attributes
    import capo_sesv2.types.suppression_list_reason
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.timestamp


class SuppressedDestination(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that is on the suppression list for your account or for a specific tenant.</p>"""
    reason: "capo_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The reason that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    last_update_time: "capo_sesv2.types.timestamp.Timestamp"
    """<p>The date and time when the suppressed destination was last updated, shown in Unix time format.</p>"""
    attributes: NotRequired[
        "capo_sesv2.types.suppressed_destination_attributes.SuppressedDestinationAttributes"
    ]
    """<p>An optional value that can contain additional information about the reasons that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant that the suppressed destination belongs to. This field is present only when the suppressed destination is on a tenant's suppression list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestination) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import capo_sesv2.types.suppression_list_reason

    out["Reason"] = capo_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    import capo_sesv2.types.timestamp

    out["LastUpdateTime"] = capo_sesv2.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    if "attributes" in value:
        import capo_sesv2.types.suppressed_destination_attributes

        out["Attributes"] = (
            capo_sesv2.types.suppressed_destination_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "tenant_name" in value:
        out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> SuppressedDestination:
    out: SuppressedDestination = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        out["email_address"] = ""
    if data.get("Reason") is not None:
        import capo_sesv2.types.suppression_list_reason

        out["reason"] = capo_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_sesv2.types.suppression_list_reason.SuppressionListReason", ""
        )
    if data.get("LastUpdateTime") is not None:
        import capo_sesv2.types.timestamp

        out["last_update_time"] = capo_sesv2.types.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    else:
        import datetime

        out["last_update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Attributes") is not None:
        import capo_sesv2.types.suppressed_destination_attributes

        out["attributes"] = (
            capo_sesv2.types.suppressed_destination_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    return out
