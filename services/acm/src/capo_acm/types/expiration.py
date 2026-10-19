"""Generated from Smithy shape ``com.amazonaws.acm#Expiration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.time_type


class Expiration(TypedDict, closed=True):
    value: "int"
    """<p>The numeric value of the expiration.</p>"""
    type: "capo_acm.types.time_type.TimeType"
    """<p>The time unit for the expiration value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expiration) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_acm.types.time_type

    out["Type"] = capo_acm.types.time_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Expiration:
    out: Expiration = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("Type") is not None:
        import capo_acm.types.time_type

        out["type"] = capo_acm.types.time_type.deserialize_aws_json_1_1(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_acm.types.time_type.TimeType", "")
    return out
