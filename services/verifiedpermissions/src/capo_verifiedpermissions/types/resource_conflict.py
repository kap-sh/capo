"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceConflict``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.resource_type


class ResourceConflict(TypedDict, closed=True):
    resource_id: "str"
    """<p>The unique identifier of the resource involved in a conflict.</p>"""
    resource_type: "capo_verifiedpermissions.types.resource_type.ResourceType"
    """<p>The type of the resource involved in a conflict.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceConflict) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    import capo_verifiedpermissions.types.resource_type

    out["resourceType"] = (
        capo_verifiedpermissions.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceConflict:
    out: ResourceConflict = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceType") is not None:
        import capo_verifiedpermissions.types.resource_type

        out["resource_type"] = (
            capo_verifiedpermissions.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_verifiedpermissions.types.resource_type.ResourceType", ""
        )
    return out
