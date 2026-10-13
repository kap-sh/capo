"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketAccessKeysResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.access_key_list


class GetBucketAccessKeysResult(TypedDict, closed=True):
    access_keys: NotRequired["capo_lightsail.types.access_key_list.AccessKeyList"]
    """<p>An object that describes the access keys for the specified bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketAccessKeysResult) -> dict:
    out: dict = {}
    if "access_keys" in value:
        import capo_lightsail.types.access_key_list

        out["accessKeys"] = capo_lightsail.types.access_key_list.serialize_aws_json_1_1(
            value["access_keys"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketAccessKeysResult:
    out: GetBucketAccessKeysResult = {}  # type: ignore[typeddict-item]
    if data.get("accessKeys") is not None:
        import capo_lightsail.types.access_key_list

        out["access_keys"] = (
            capo_lightsail.types.access_key_list.deserialize_aws_json_1_1(
                data["accessKeys"]
            )
        )
    return out


def redact_sensitive(value: GetBucketAccessKeysResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_keys" in value:
        import capo_lightsail.types.access_key_list

        out["access_keys"] = capo_lightsail.types.access_key_list.redact_sensitive(
            value["access_keys"]
        )
    return out
