"""Generated from Smithy shape ``com.amazonaws.billing#BillingPreferenceForKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.preference_key
    import capo_billing.types.preference_value


class BillingPreferenceForKey(TypedDict, closed=True):
    key: "capo_billing.types.preference_key.PreferenceKey"
    """<p>The preference key. Format depends on the feature being updated.</p>"""
    value: "capo_billing.types.preference_value.PreferenceValue"
    """<p>The preference value. Valid values: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPreferenceForKey) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_billing.types.preference_value

    out["value"] = capo_billing.types.preference_value.serialize_aws_json_1_0(
        value["value"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingPreferenceForKey:
    out: BillingPreferenceForKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        import capo_billing.types.preference_value

        out["value"] = capo_billing.types.preference_value.deserialize_aws_json_1_0(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_billing.types.preference_value.PreferenceValue", ""
        )
    return out
