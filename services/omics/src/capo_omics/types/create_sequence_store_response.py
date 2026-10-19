"""Generated from Smithy shape ``com.amazonaws.omics#CreateSequenceStoreResponse``."""

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


class CreateSequenceStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The store's ID.</p>"""
    arn: "capo_omics.types.sequence_store_arn.SequenceStoreArn"
    """<p>The store's ARN.</p>"""
    name: NotRequired["capo_omics.types.sequence_store_name.SequenceStoreName"]
    """<p>The store's name.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>The store's description.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store. This contains the KMS key ARN that is used to encrypt read set objects.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the store was created.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>An S3 location that is used to store files that have failed a direct upload.</p>"""
    e_tag_algorithm_family: NotRequired[
        "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The algorithm family of the ETag.</p>"""
    status: NotRequired["capo_omics.types.sequence_store_status.SequenceStoreStatus"]
    """<p>The status of the sequence store.</p>"""
    status_message: NotRequired[
        "capo_omics.types.sequence_store_status_message.SequenceStoreStatusMessage"
    ]
    """<p>The status message of the sequence store.</p>"""
    propagated_set_level_tags: NotRequired[
        "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>"""
    s3_access: NotRequired[
        "capo_omics.types.sequence_store_s3_access.SequenceStoreS3Access"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSequenceStoreResponse) -> dict:
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
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "propagated_set_level_tags" in value:
        import capo_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            capo_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "s3_access" in value:
        import capo_omics.types.sequence_store_s3_access

        out["s3Access"] = capo_omics.types.sequence_store_s3_access.serialize_json(
            value["s3_access"]
        )
    return out


def deserialize_json(data: dict) -> CreateSequenceStoreResponse:
    out: CreateSequenceStoreResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("fallbackLocation") is not None:
        out["fallback_location"] = data["fallbackLocation"]
    if data.get("eTagAlgorithmFamily") is not None:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("propagatedSetLevelTags") is not None:
        import capo_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            capo_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if data.get("s3Access") is not None:
        import capo_omics.types.sequence_store_s3_access

        out["s3_access"] = capo_omics.types.sequence_store_s3_access.deserialize_json(
            data["s3Access"]
        )
    return out
