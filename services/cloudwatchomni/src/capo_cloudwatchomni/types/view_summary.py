"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.view_type


class ViewSummary(TypedDict, closed=True):
    name: "str"
    """The name of the view."""
    type: "capo_cloudwatchomni.types.view_type.ViewType"
    """The ownership category of the view."""
    description: NotRequired["str"]
    """The description of the view."""
    created_at: "datetime.datetime"
    """The timestamp when the view was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the view was last updated."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViewSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cloudwatchomni.types.view_type

    out["type"] = capo_cloudwatchomni.types.view_type.serialize_cbor(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    return out


def deserialize_cbor(data: dict) -> ViewSummary:
    out: ViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_cloudwatchomni.types.view_type

        out["type"] = capo_cloudwatchomni.types.view_type.deserialize_cbor(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_cloudwatchomni.types.view_type.ViewType", "")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
