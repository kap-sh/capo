"""Generated from Smithy shape ``com.amazonaws.dataexchange#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.map_of__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_dataexchange.types.__string.__string"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>"""
    tags: "capo_dataexchange.types.map_of__string.MapOf__string"
    """<p>A label that consists of a customer-defined key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_dataexchange.types.map_of__string

    out["tags"] = capo_dataexchange.types.map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
