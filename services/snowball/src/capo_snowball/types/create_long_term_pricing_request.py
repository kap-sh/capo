"""Generated from Smithy shape ``com.amazonaws.snowball#CreateLongTermPricingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.java_boolean
    import capo_snowball.types.long_term_pricing_type
    import capo_snowball.types.snowball_type


class CreateLongTermPricingRequest(TypedDict, closed=True):
    long_term_pricing_type: (
        "capo_snowball.types.long_term_pricing_type.LongTermPricingType"
    )
    """<p>The type of long-term pricing option you want for the device, either 1-year or 3-year long-term pricing.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "capo_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>Specifies whether the current long-term pricing type for the device should be renewed.</p>"""
    snowball_type: "capo_snowball.types.snowball_type.SnowballType"
    """<p>The type of Snow Family devices to use for the long-term pricing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLongTermPricingRequest) -> dict:
    out: dict = {}
    import capo_snowball.types.long_term_pricing_type

    out["LongTermPricingType"] = (
        capo_snowball.types.long_term_pricing_type.serialize_aws_json_1_1(
            value["long_term_pricing_type"]
        )
    )
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    import capo_snowball.types.snowball_type

    out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
        value["snowball_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLongTermPricingRequest:
    out: CreateLongTermPricingRequest = {}  # type: ignore[typeddict-item]
    if data.get("LongTermPricingType") is not None:
        import capo_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            capo_snowball.types.long_term_pricing_type.deserialize_aws_json_1_1(
                data["LongTermPricingType"]
            )
        )
    else:
        import typing

        out["long_term_pricing_type"] = typing.cast(
            "capo_snowball.types.long_term_pricing_type.LongTermPricingType", ""
        )
    if data.get("IsLongTermPricingAutoRenew") is not None:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    else:
        import typing

        out["snowball_type"] = typing.cast(
            "capo_snowball.types.snowball_type.SnowballType", ""
        )
    return out
