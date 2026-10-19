"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#KeyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.key_filter_key
    import capo_cloudwatchomni.types.key_filter_values


class KeyFilter(TypedDict, closed=True):
    key: "capo_cloudwatchomni.types.key_filter_key.KeyFilterKey"
    """The tag or attribute key to filter on."""
    values: NotRequired["capo_cloudwatchomni.types.key_filter_values.KeyFilterValues"]
    """The values to match for this key, OR'ed together. Each supports exact, negation (!value), and wildcard (*value*, value*, *value) syntax."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "values" in value:
        import capo_cloudwatchomni.types.key_filter_values

        out["values"] = capo_cloudwatchomni.types.key_filter_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> KeyFilter:
    out: KeyFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("values") is not None:
        import capo_cloudwatchomni.types.key_filter_values

        out["values"] = capo_cloudwatchomni.types.key_filter_values.deserialize_cbor(
            data["values"]
        )
    return out
