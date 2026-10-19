"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.timestamp


class ListObjectTypeAttributeItem(TypedDict, closed=True):
    attribute_name: "capo_customer_profiles.types.name.name"
    """<p>Name of the attribute.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>When the attribute was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeItem) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeItem:
    out: ListObjectTypeAttributeItem = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
