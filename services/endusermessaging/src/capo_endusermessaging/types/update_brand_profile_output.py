"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateBrandProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.brand_profile_name
    import capo_endusermessaging.types.status


class UpdateBrandProfileOutput(TypedDict, closed=True):
    brand_profile_id: (
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    )
    """<p>The unique identifier of the brand profile.</p>"""
    brand_profile_arn: (
        "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the brand profile.</p>"""
    brand_profile_name: (
        "capo_endusermessaging.types.brand_profile_name.BrandProfileName"
    )
    """<p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>"""
    status: "capo_endusermessaging.types.status.Status"
    """<p>The current lifecycle status of the brand profile.</p>"""
    deletion_protection_enabled: "bool"
    """<p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time when the resource was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandProfileOutput) -> dict:
    out: dict = {}
    out["brandProfileId"] = value["brand_profile_id"]
    out["brandProfileArn"] = value["brand_profile_arn"]
    out["brandProfileName"] = value["brand_profile_name"]
    import capo_endusermessaging.types.status

    out["status"] = capo_endusermessaging.types.status.serialize_json(value["status"])
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_endusermessaging.types._prelude.timestamp

    out["updatedAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBrandProfileOutput:
    out: UpdateBrandProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileId") is not None:
        out["brand_profile_id"] = data["brandProfileId"]
    else:
        out["brand_profile_id"] = ""
    if data.get("brandProfileArn") is not None:
        out["brand_profile_arn"] = data["brandProfileArn"]
    else:
        out["brand_profile_arn"] = ""
    if data.get("brandProfileName") is not None:
        out["brand_profile_name"] = data["brandProfileName"]
    else:
        out["brand_profile_name"] = ""
    if data.get("status") is not None:
        import capo_endusermessaging.types.status

        out["status"] = capo_endusermessaging.types.status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_endusermessaging.types.status.Status", "")
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        out["deletion_protection_enabled"] = False
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
