"""Generated from Smithy shape ``com.amazonaws.lightsail#DisableAddOnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_type
    import capo_lightsail.types.resource_name


class DisableAddOnRequest(TypedDict, closed=True):
    add_on_type: "capo_lightsail.types.add_on_type.AddOnType"
    """<p>The add-on type to disable.</p>"""
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the source resource for which to disable the add-on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAddOnRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.add_on_type

    out["addOnType"] = capo_lightsail.types.add_on_type.serialize_aws_json_1_1(
        value["add_on_type"]
    )
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAddOnRequest:
    out: DisableAddOnRequest = {}  # type: ignore[typeddict-item]
    if data.get("addOnType") is not None:
        import capo_lightsail.types.add_on_type

        out["add_on_type"] = capo_lightsail.types.add_on_type.deserialize_aws_json_1_1(
            data["addOnType"]
        )
    else:
        import typing

        out["add_on_type"] = typing.cast(
            "capo_lightsail.types.add_on_type.AddOnType", ""
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    return out
