"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeValuesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.sensitive_string1_to1000
    import capo_customer_profiles.types.timestamp


class ListObjectTypeAttributeValuesItem(TypedDict, closed=True):
    value: (
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    )
    """<p>The actual value of the object type attribute.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the object type attribute value was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeValuesItem) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeValuesItem:
    out: ListObjectTypeAttributeValuesItem = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ListObjectTypeAttributeValuesItem.value required")
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "ListObjectTypeAttributeValuesItem.last_updated_at required"
        )
    return out


def redact_sensitive(value: ListObjectTypeAttributeValuesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
