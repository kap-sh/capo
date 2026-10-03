"""Generated from Smithy shape ``com.amazonaws.lambda#PublishVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.description
    import capo_lambda.types.function_name
    import capo_lambda.types.function_version_latest_published
    import capo_lambda.types.string


class PublishVersionRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    code_sha256: NotRequired["capo_lambda.types.string.String"]
    """<p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>A description for the version to override the description in the function configuration.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>"""
    publish_to: NotRequired[
        "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
    ]
    """<p>Specifies where to publish the function version or configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishVersionRequest) -> dict:
    out: dict = {}
    if "code_sha256" in value:
        out["CodeSha256"] = value["code_sha256"]
    if "description" in value:
        out["Description"] = value["description"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "publish_to" in value:
        import capo_lambda.types.function_version_latest_published

        out["PublishTo"] = (
            capo_lambda.types.function_version_latest_published.serialize_json(
                value["publish_to"]
            )
        )
    return out


def deserialize_json(data: dict) -> PublishVersionRequest:
    out: PublishVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CodeSha256") is not None:
        out["code_sha256"] = data["CodeSha256"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("PublishTo") is not None:
        import capo_lambda.types.function_version_latest_published

        out["publish_to"] = (
            capo_lambda.types.function_version_latest_published.deserialize_json(
                data["PublishTo"]
            )
        )
    return out
