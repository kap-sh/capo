"""Generated from Smithy shape ``com.amazonaws.omics#CreateReferenceStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.reference_store_arn
    import capo_omics.types.reference_store_description
    import capo_omics.types.reference_store_id
    import capo_omics.types.reference_store_name
    import capo_omics.types.sse_config


class CreateReferenceStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The store's ID.</p>"""
    arn: "capo_omics.types.reference_store_arn.ReferenceStoreArn"
    """<p>The store's ARN.</p>"""
    name: NotRequired["capo_omics.types.reference_store_name.ReferenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "capo_omics.types.reference_store_description.ReferenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>The store's SSE settings.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReferenceStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import capo_omics.types.sse_config

        out["sseConfig"] = capo_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateReferenceStoreResponse:
    out: CreateReferenceStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sseConfig") is not None:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
