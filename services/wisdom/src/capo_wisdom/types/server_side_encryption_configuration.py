"""Generated from Smithy shape ``com.amazonaws.wisdom#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.non_empty_string


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The customer managed key used for encryption. For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>. For information about valid ID values, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id">Key identifiers (KeyId)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
