"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementPackSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.management_type
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_name
    import capo_securityagent.types.security_requirement_pack_status


class SecurityRequirementPackSummary(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack.</p>"""
    name: "capo_securityagent.types.security_requirement_pack_name.SecurityRequirementPackName"
    """<p>The name of the security requirement pack.</p>"""
    description: NotRequired["str"]
    """<p>A description of the security requirement pack.</p>"""
    vendor_name: NotRequired["str"]
    """<p>The vendor name for AWS managed packs.</p>"""
    management_type: "capo_securityagent.types.management_type.ManagementType"
    """<p>The management type of the pack.</p>"""
    status: "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
    """<p>The status of the security requirement pack.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the security requirement pack was created, in UTC format.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the security requirement pack was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementPackSummary) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "vendor_name" in value:
        out["vendorName"] = value["vendor_name"]
    import capo_securityagent.types.management_type

    out["managementType"] = capo_securityagent.types.management_type.serialize_json(
        value["management_type"]
    )
    import capo_securityagent.types.security_requirement_pack_status

    out["status"] = (
        capo_securityagent.types.security_requirement_pack_status.serialize_json(
            value["status"]
        )
    )
    import capo_securityagent._protocol.serialize

    out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_securityagent._protocol.serialize

    out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> SecurityRequirementPackSummary:
    out: SecurityRequirementPackSummary = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        out["pack_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("vendorName") is not None:
        out["vendor_name"] = data["vendorName"]
    if data.get("managementType") is not None:
        import capo_securityagent.types.management_type

        out["management_type"] = (
            capo_securityagent.types.management_type.deserialize_json(
                data["managementType"]
            )
        )
    else:
        import typing

        out["management_type"] = typing.cast(
            "capo_securityagent.types.management_type.ManagementType", ""
        )
    if data.get("status") is not None:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
