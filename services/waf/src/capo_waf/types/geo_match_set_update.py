"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_action
    import capo_waf.types.geo_match_constraint


class GeoMatchSetUpdate(TypedDict, closed=True):
    action: "capo_waf.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a country with <a>UpdateGeoMatchSet</a>.</p>"""
    geo_match_constraint: "capo_waf.types.geo_match_constraint.GeoMatchConstraint"
    """<p>The country from which web requests originate that you want AWS WAF to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSetUpdate) -> dict:
    out: dict = {}
    import capo_waf.types.change_action

    out["Action"] = capo_waf.types.change_action.serialize_aws_json_1_1(value["action"])
    import capo_waf.types.geo_match_constraint

    out["GeoMatchConstraint"] = (
        capo_waf.types.geo_match_constraint.serialize_aws_json_1_1(
            value["geo_match_constraint"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GeoMatchSetUpdate:
    out: GeoMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf.types.change_action

        out["action"] = capo_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_waf.types.change_action.ChangeAction", "")
    if data.get("GeoMatchConstraint") is not None:
        import capo_waf.types.geo_match_constraint

        out["geo_match_constraint"] = (
            capo_waf.types.geo_match_constraint.deserialize_aws_json_1_1(
                data["GeoMatchConstraint"]
            )
        )
    else:
        raise DeserializationError("GeoMatchSetUpdate.geo_match_constraint required")
    return out
