"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.message_body


class GetArchiveMessageContentResponse(TypedDict, closed=True):
    body: NotRequired["capo_mailmanager.types.message_body.MessageBody"]
    """<p>The textual body content of the email message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageContentResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_mailmanager.types.message_body

        out["Body"] = capo_mailmanager.types.message_body.serialize_aws_json_1_0(
            value["body"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageContentResponse:
    out: GetArchiveMessageContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_mailmanager.types.message_body

        out["body"] = capo_mailmanager.types.message_body.deserialize_aws_json_1_0(
            data["Body"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetArchiveMessageContentResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_mailmanager.types.message_body

        out["Body"] = capo_mailmanager.types.message_body.serialize_cbor(value["body"])
    return out


def deserialize_cbor(data: dict) -> GetArchiveMessageContentResponse:
    out: GetArchiveMessageContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_mailmanager.types.message_body

        out["body"] = capo_mailmanager.types.message_body.deserialize_cbor(data["Body"])
    return out
