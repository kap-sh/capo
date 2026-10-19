"""Generated from Smithy shape ``com.amazonaws.forecast#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. </p>"""
    tag_keys: "capo_forecast.types.tag_keys.TagKeys"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_forecast.types.tag_keys

    out["TagKeys"] = capo_forecast.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_forecast.types.tag_keys

        out["tag_keys"] = capo_forecast.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        import capo_forecast.types.tag_keys

        out["tag_keys"] = capo_forecast.types.tag_keys.redact_sensitive(
            value["tag_keys"]
        )
    return out
