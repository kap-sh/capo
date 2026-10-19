"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Threshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.operator
    import capo_customer_profiles.types.string1_to255


class Threshold(TypedDict, closed=True):
    value: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The value of the threshold.</p>"""
    operator: "capo_customer_profiles.types.operator.Operator"
    """<p>The operator of the threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threshold) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_customer_profiles.types.operator

    out["Operator"] = capo_customer_profiles.types.operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> Threshold:
    out: Threshold = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("Operator") is not None:
        import capo_customer_profiles.types.operator

        out["operator"] = capo_customer_profiles.types.operator.deserialize_json(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_customer_profiles.types.operator.Operator", ""
        )
    return out
