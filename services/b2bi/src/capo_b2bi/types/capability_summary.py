"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.capability_type
    import capo_b2bi.types.created_date
    import capo_b2bi.types.modified_date


class CapabilitySummary(TypedDict, closed=True):
    capability_id: "capo_b2bi.types.capability_id.CapabilityId"
    """<p>Returns a system-assigned unique identifier for the capability.</p>"""
    name: "capo_b2bi.types.capability_name.CapabilityName"
    """<p>The display name of the capability.</p>"""
    type: "capo_b2bi.types.capability_type.CapabilityType"
    """<p>Returns the type of the capability. Currently, only <code>edi</code> is supported.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the capability.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp that identifies the most recent date and time that the capability was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilitySummary) -> dict:
    out: dict = {}
    out["capabilityId"] = value["capability_id"]
    out["name"] = value["name"]
    import capo_b2bi.types.capability_type

    out["type"] = capo_b2bi.types.capability_type.serialize_aws_json_1_0(value["type"])
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapabilitySummary:
    out: CapabilitySummary = {}  # type: ignore[typeddict-item]
    if data.get("capabilityId") is not None:
        out["capability_id"] = data["capabilityId"]
    else:
        out["capability_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_b2bi.types.capability_type

        out["type"] = capo_b2bi.types.capability_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_b2bi.types.capability_type.CapabilityType", "")
    if data.get("createdAt") is not None:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
