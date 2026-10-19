"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.fallback_location
    import capo_omics.types.sequence_store_arn
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name
    import capo_omics.types.sequence_store_status
    import capo_omics.types.sequence_store_status_message
    import capo_omics.types.sse_config


class SequenceStoreDetail(TypedDict, closed=True):
    arn: "capo_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The store's ARN.</p>"""
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>The store's server-side encryption (SSE) settings.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p> An S3 location that is used to store files that have failed a direct upload. </p>"""
    e_tag_algorithm_family: NotRequired[
        "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The algorithm family of the ETag.</p>"""
    status: NotRequired["capo_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>Status of the sequence store.</p>"""
    status_message: NotRequired[
        "capo_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The last-updated time of the Sequence Store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreDetail) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
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
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "update_time" in value:
        import capo_omics._protocol.serialize

        out["updateTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["update_time"]
        )
    return out


def deserialize_json(data: dict) -> SequenceStoreDetail:
    out: SequenceStoreDetail = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
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
    if data.get("fallbackLocation") is not None:
        out["fallback_location"] = data["fallbackLocation"]
    if data.get("eTagAlgorithmFamily") is not None:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    return out
