"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.concurrency
    import capo_lambda.types.function_code_location
    import capo_lambda.types.function_configuration
    import capo_lambda.types.tags
    import capo_lambda.types.tags_error


class GetFunctionResponse(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_lambda.types.function_configuration.FunctionConfiguration"
    ]
    """<p>The configuration of the function or version.</p>"""
    code: NotRequired["capo_lambda.types.function_code_location.FunctionCodeLocation"]
    """<p>The deployment package of the function or version.</p>"""
    tags: NotRequired["capo_lambda.types.tags.Tags"]
    """<p>The function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/tagging.html">tags</a>. Lambda returns tag data only if you have explicit allow permissions for <a href="https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html">lambda:ListTags</a>.</p>"""
    tags_error: NotRequired["capo_lambda.types.tags_error.TagsError"]
    """<p>An object that contains details about an error related to retrieving tags.</p>"""
    concurrency: NotRequired["capo_lambda.types.concurrency.Concurrency"]
    """<p>The function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html">reserved concurrency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_lambda.types.function_configuration

        out["Configuration"] = capo_lambda.types.function_configuration.serialize_json(
            value["configuration"]
        )
    if "code" in value:
        import capo_lambda.types.function_code_location

        out["Code"] = capo_lambda.types.function_code_location.serialize_json(
            value["code"]
        )
    if "tags" in value:
        import capo_lambda.types.tags

        out["Tags"] = capo_lambda.types.tags.serialize_json(value["tags"])
    if "tags_error" in value:
        import capo_lambda.types.tags_error

        out["TagsError"] = capo_lambda.types.tags_error.serialize_json(
            value["tags_error"]
        )
    if "concurrency" in value:
        import capo_lambda.types.concurrency

        out["Concurrency"] = capo_lambda.types.concurrency.serialize_json(
            value["concurrency"]
        )
    return out


def deserialize_json(data: dict) -> GetFunctionResponse:
    out: GetFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_lambda.types.function_configuration

        out["configuration"] = (
            capo_lambda.types.function_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("Code") is not None:
        import capo_lambda.types.function_code_location

        out["code"] = capo_lambda.types.function_code_location.deserialize_json(
            data["Code"]
        )
    if data.get("Tags") is not None:
        import capo_lambda.types.tags

        out["tags"] = capo_lambda.types.tags.deserialize_json(data["Tags"])
    if data.get("TagsError") is not None:
        import capo_lambda.types.tags_error

        out["tags_error"] = capo_lambda.types.tags_error.deserialize_json(
            data["TagsError"]
        )
    if data.get("Concurrency") is not None:
        import capo_lambda.types.concurrency

        out["concurrency"] = capo_lambda.types.concurrency.deserialize_json(
            data["Concurrency"]
        )
    return out
