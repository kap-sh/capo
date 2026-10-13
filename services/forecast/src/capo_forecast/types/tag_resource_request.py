"""Generated from Smithy shape ``com.amazonaws.forecast#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. </p>"""
    tags: "capo_forecast.types.tags.Tags"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_forecast.types.tags

    out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.redact_sensitive(value["tags"])
    return out
