"""Generated from Smithy shape ``com.amazonaws.omics#UpdateSequenceStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.fallback_location
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.sequence_store_arn
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name
    import capo_omics.types.sequence_store_s3_access
    import capo_omics.types.sequence_store_status
    import capo_omics.types.sequence_store_status_message
    import capo_omics.types.sse_config


class UpdateSequenceStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The ID of the sequence store.</p>"""
    arn: "capo_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The ARN of the sequence store.</p>"""
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The name of the sequence store.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>Description of the sequence store.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    creation_time: "datetime.datetime"
    """<p>The time when the store was created.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The last-updated time of the Sequence Store.</p>"""
    propagated_set_level_tags: NotRequired[
        "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>"""
    status: NotRequired["capo_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>The status of the sequence store.</p>"""
    status_message: NotRequired[
        "capo_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>"""
    s3_access: NotRequired[
        "capo_omics.types.sequence_store_s3_access.SequenceStoreS3Access"
    ]
    e_tag_algorithm_family: NotRequired[
        "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The ETag algorithm family to use on ingested read sets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSequenceStoreResponse) -> dict:
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
    if "update_time" in value:
        import capo_omics._protocol.serialize

        out["updateTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["update_time"]
        )
    if "propagated_set_level_tags" in value:
        import capo_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            capo_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "s3_access" in value:
        import capo_omics.types.sequence_store_s3_access

        out["s3Access"] = capo_omics.types.sequence_store_s3_access.serialize_json(
            value["s3_access"]
        )
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    return out


def deserialize_json(data: dict) -> UpdateSequenceStoreResponse:
    out: UpdateSequenceStoreResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    if data.get("propagatedSetLevelTags") is not None:
        import capo_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            capo_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("fallbackLocation") is not None:
        out["fallback_location"] = data["fallbackLocation"]
    if data.get("s3Access") is not None:
        import capo_omics.types.sequence_store_s3_access

        out["s3_access"] = capo_omics.types.sequence_store_s3_access.deserialize_json(
            data["s3Access"]
        )
    if data.get("eTagAlgorithmFamily") is not None:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    return out
