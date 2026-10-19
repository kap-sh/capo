"""Generated from Smithy shape ``com.amazonaws.dsql#CreateStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.stream_format
    import capo_dsql.types.stream_ordering
    import capo_dsql.types.tag_map
    import capo_dsql.types.target_definition


class CreateStreamInput(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for which to create the stream.</p>"""
    target_definition: "capo_dsql.types.target_definition.TargetDefinition"
    """<p>The target destination configuration for the stream. Contains Kinesis stream configuration including stream ARN and IAM role ARN.</p>"""
    ordering: "capo_dsql.types.stream_ordering.StreamOrdering"
    """<p>The ordering mode for the stream. Determines how change events are ordered when delivered to the target.</p>"""
    format: "capo_dsql.types.stream_format.StreamFormat"
    """<p>The format of the stream records.</p>"""
    tags: NotRequired["capo_dsql.types.tag_map.TagMap"]
    """<p>A map of key and value pairs to use to tag your stream.</p>"""
    client_token: NotRequired["capo_dsql.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamInput) -> dict:
    out: dict = {}
    import capo_dsql.types.target_definition

    out["targetDefinition"] = capo_dsql.types.target_definition.serialize_json(
        value["target_definition"]
    )
    import capo_dsql.types.stream_ordering

    out["ordering"] = capo_dsql.types.stream_ordering.serialize_json(value["ordering"])
    import capo_dsql.types.stream_format

    out["format"] = capo_dsql.types.stream_format.serialize_json(value["format"])
    if "tags" in value:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateStreamInput:
    out: CreateStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("targetDefinition") is not None:
        import capo_dsql.types.target_definition

        out["target_definition"] = capo_dsql.types.target_definition.deserialize_json(
            data["targetDefinition"]
        )
    else:
        import capo_dsql.types._unknown

        out["target_definition"] = capo_dsql.types._unknown.UnknownUnionMember("")
    if data.get("ordering") is not None:
        import capo_dsql.types.stream_ordering

        out["ordering"] = capo_dsql.types.stream_ordering.deserialize_json(
            data["ordering"]
        )
    else:
        import typing

        out["ordering"] = typing.cast(
            "capo_dsql.types.stream_ordering.StreamOrdering", ""
        )
    if data.get("format") is not None:
        import capo_dsql.types.stream_format

        out["format"] = capo_dsql.types.stream_format.deserialize_json(data["format"])
    else:
        import typing

        out["format"] = typing.cast("capo_dsql.types.stream_format.StreamFormat", "")
    if data.get("tags") is not None:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
