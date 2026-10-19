"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.geo_match_constraint_type
    import capo_waf.types.geo_match_constraint_value


class GeoMatchConstraint(TypedDict, closed=True):
    type: "capo_waf.types.geo_match_constraint_type.GeoMatchConstraintType"
    """<p>The type of geographical area you want AWS WAF to search for. Currently <code>Country</code> is the only valid value.</p>"""
    value: "capo_waf.types.geo_match_constraint_value.GeoMatchConstraintValue"
    """<p>The country that you want AWS WAF to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchConstraint) -> dict:
    out: dict = {}
    import capo_waf.types.geo_match_constraint_type

    out["Type"] = capo_waf.types.geo_match_constraint_type.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_waf.types.geo_match_constraint_value

    out["Value"] = capo_waf.types.geo_match_constraint_value.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchConstraint:
    out: GeoMatchConstraint = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_waf.types.geo_match_constraint_type

        out["type"] = capo_waf.types.geo_match_constraint_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_waf.types.geo_match_constraint_type.GeoMatchConstraintType", ""
        )
    if data.get("Value") is not None:
        import capo_waf.types.geo_match_constraint_value

        out["value"] = (
            capo_waf.types.geo_match_constraint_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_waf.types.geo_match_constraint_value.GeoMatchConstraintValue", ""
        )
    return out
