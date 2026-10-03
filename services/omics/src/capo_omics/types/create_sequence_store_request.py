"""Generated from Smithy shape ``com.amazonaws.omics#CreateSequenceStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.client_token
    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.fallback_location
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.s3_access_config
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_name
    import capo_omics.types.sse_config
    import capo_omics.types.tag_map


class CreateSequenceStoreRequest(TypedDict, closed=True):
    name: "capo_omics.types.sequence_store_name.SequenceStoreName"
    """<p>A name for the store.</p>"""
    description: NotRequired[
        "capo_omics.types.sequence_store_description.SequenceStoreDescription"
    ]
    """<p>A description for the store.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the store. You can configure up to 50 tags.</p>"""
    client_token: NotRequired["capo_omics.types.client_token.ClientToken"]
    """<p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>"""
    fallback_location: NotRequired[
        "capo_omics.types.fallback_location.FallbackLocation"
    ]
    """<p>An S3 location that is used to store files that have failed a direct upload. You can add or change the <code>fallbackLocation</code> after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.</p>"""
    e_tag_algorithm_family: NotRequired[
        "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
    ]
    """<p>The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see <a href="https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html">ETags and data provenance</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""
    propagated_set_level_tags: NotRequired[
        "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
    ]
    """<p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.</p>"""
    s3_access_config: NotRequired["capo_omics.types.s3_access_config.S3AccessConfig"]
    """<p>S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSequenceStoreRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sse_config" in value:
        import capo_omics.types.sse_config

        out["sseConfig"] = capo_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "fallback_location" in value:
        out["fallbackLocation"] = value["fallback_location"]
    if "e_tag_algorithm_family" in value:
        out["eTagAlgorithmFamily"] = value["e_tag_algorithm_family"]
    if "propagated_set_level_tags" in value:
        import capo_omics.types.propagated_set_level_tags

        out["propagatedSetLevelTags"] = (
            capo_omics.types.propagated_set_level_tags.serialize_json(
                value["propagated_set_level_tags"]
            )
        )
    if "s3_access_config" in value:
        import capo_omics.types.s3_access_config

        out["s3AccessConfig"] = capo_omics.types.s3_access_config.serialize_json(
            value["s3_access_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateSequenceStoreRequest:
    out: CreateSequenceStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSequenceStoreRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sseConfig") is not None:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("fallbackLocation") is not None:
        out["fallback_location"] = data["fallbackLocation"]
    if data.get("eTagAlgorithmFamily") is not None:
        out["e_tag_algorithm_family"] = data["eTagAlgorithmFamily"]
    if data.get("propagatedSetLevelTags") is not None:
        import capo_omics.types.propagated_set_level_tags

        out["propagated_set_level_tags"] = (
            capo_omics.types.propagated_set_level_tags.deserialize_json(
                data["propagatedSetLevelTags"]
            )
        )
    if data.get("s3AccessConfig") is not None:
        import capo_omics.types.s3_access_config

        out["s3_access_config"] = capo_omics.types.s3_access_config.deserialize_json(
            data["s3AccessConfig"]
        )
    return out
