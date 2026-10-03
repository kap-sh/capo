"""Generated from Smithy shape ``com.amazonaws.connect#CreateAttachedFileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.file_source_uri
    import capo_connect.types.file_use_case_type
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateAttachedFileRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    file_use_case_type: "capo_connect.types.file_use_case_type.FileUseCaseType"
    """<p>The use case for the file.</p> <important> <p>Only <code>VOICE_RECORDING</code> is supported.</p> </important>"""
    file_source_uri: "capo_connect.types.file_source_uri.FileSourceUri"
    """<p>The S3 URI of the file to be attached. Only S3 source URIs are supported.</p>"""
    associated_resource_arn: "capo_connect.types.arn.ARN"
    """<p>The ARN of the completed voice contact to attach the file to. Only voice contacts with Telephony subtype are supported.</p> <note> <p>This value must be a valid ARN.</p> </note>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttachedFileRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_connect.types.file_use_case_type

    out["FileUseCaseType"] = capo_connect.types.file_use_case_type.serialize_json(
        value["file_use_case_type"]
    )
    out["FileSourceUri"] = value["file_source_uri"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAttachedFileRequest:
    out: CreateAttachedFileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("FileUseCaseType") is not None:
        import capo_connect.types.file_use_case_type

        out["file_use_case_type"] = (
            capo_connect.types.file_use_case_type.deserialize_json(
                data["FileUseCaseType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAttachedFileRequest.file_use_case_type required"
        )
    if data.get("FileSourceUri") is not None:
        out["file_source_uri"] = data["FileSourceUri"]
    else:
        raise DeserializationError("CreateAttachedFileRequest.file_source_uri required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
