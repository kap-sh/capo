"""Generated from Smithy shape ``com.amazonaws.securityir#OptInFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.opt_in_feature_name


class OptInFeature(TypedDict, closed=True):
    feature_name: "capo_security_ir.types.opt_in_feature_name.OptInFeatureName"
    """<p/>"""
    is_enabled: "bool"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptInFeature) -> dict:
    out: dict = {}
    import capo_security_ir.types.opt_in_feature_name

    out["featureName"] = capo_security_ir.types.opt_in_feature_name.serialize_json(
        value["feature_name"]
    )
    out["isEnabled"] = value["is_enabled"]
    return out


def deserialize_json(data: dict) -> OptInFeature:
    out: OptInFeature = {}  # type: ignore[typeddict-item]
    if data.get("featureName") is not None:
        import capo_security_ir.types.opt_in_feature_name

        out["feature_name"] = (
            capo_security_ir.types.opt_in_feature_name.deserialize_json(
                data["featureName"]
            )
        )
    else:
        import typing

        out["feature_name"] = typing.cast(
            "capo_security_ir.types.opt_in_feature_name.OptInFeatureName", ""
        )
    if data.get("isEnabled") is not None:
        out["is_enabled"] = data["isEnabled"]
    else:
        out["is_enabled"] = False
    return out
