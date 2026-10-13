"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketAccessKeyResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.access_key
    import capo_lightsail.types.operation_list


class CreateBucketAccessKeyResult(TypedDict, closed=True):
    access_key: NotRequired["capo_lightsail.types.access_key.AccessKey"]
    """<p>An object that describes the access key that is created.</p>"""
    operations: NotRequired["capo_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketAccessKeyResult) -> dict:
    out: dict = {}
    if "access_key" in value:
        import capo_lightsail.types.access_key

        out["accessKey"] = capo_lightsail.types.access_key.serialize_aws_json_1_1(
            value["access_key"]
        )
    if "operations" in value:
        import capo_lightsail.types.operation_list

        out["operations"] = capo_lightsail.types.operation_list.serialize_aws_json_1_1(
            value["operations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketAccessKeyResult:
    out: CreateBucketAccessKeyResult = {}  # type: ignore[typeddict-item]
    if data.get("accessKey") is not None:
        import capo_lightsail.types.access_key

        out["access_key"] = capo_lightsail.types.access_key.deserialize_aws_json_1_1(
            data["accessKey"]
        )
    if data.get("operations") is not None:
        import capo_lightsail.types.operation_list

        out["operations"] = (
            capo_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out


def redact_sensitive(value: CreateBucketAccessKeyResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_key" in value:
        import capo_lightsail.types.access_key

        out["access_key"] = capo_lightsail.types.access_key.redact_sensitive(
            value["access_key"]
        )
    return out
