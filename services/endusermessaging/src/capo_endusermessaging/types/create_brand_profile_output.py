"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CreateBrandProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.brand_profile_name
    import capo_endusermessaging.types.status


class CreateBrandProfileOutput(TypedDict, closed=True):
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
    attributes_created: "int"
    """<p>The number of default attributes that were created for the brand profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandProfileOutput) -> dict:
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
    out["attributesCreated"] = value["attributes_created"]
    return out


def deserialize_json(data: dict) -> CreateBrandProfileOutput:
    out: CreateBrandProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("brandProfileId") is not None:
        out["brand_profile_id"] = data["brandProfileId"]
    else:
        raise DeserializationError("CreateBrandProfileOutput.brand_profile_id required")
    if data.get("brandProfileArn") is not None:
        out["brand_profile_arn"] = data["brandProfileArn"]
    else:
        raise DeserializationError(
            "CreateBrandProfileOutput.brand_profile_arn required"
        )
    if data.get("brandProfileName") is not None:
        out["brand_profile_name"] = data["brandProfileName"]
    else:
        raise DeserializationError(
            "CreateBrandProfileOutput.brand_profile_name required"
        )
    if data.get("status") is not None:
        import capo_endusermessaging.types.status

        out["status"] = capo_endusermessaging.types.status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateBrandProfileOutput.status required")
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        raise DeserializationError(
            "CreateBrandProfileOutput.deletion_protection_enabled required"
        )
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateBrandProfileOutput.created_at required")
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateBrandProfileOutput.updated_at required")
    if data.get("attributesCreated") is not None:
        out["attributes_created"] = data["attributesCreated"]
    else:
        raise DeserializationError(
            "CreateBrandProfileOutput.attributes_created required"
        )
    return out
