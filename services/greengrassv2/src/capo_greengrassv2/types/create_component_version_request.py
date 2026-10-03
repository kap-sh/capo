"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CreateComponentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.client_token_string
    import capo_greengrassv2.types.lambda_function_recipe_source
    import capo_greengrassv2.types.recipe_blob
    import capo_greengrassv2.types.tag_map


class CreateComponentVersionRequest(TypedDict, closed=True):
    inline_recipe: NotRequired["capo_greengrassv2.types.recipe_blob.RecipeBlob"]
    """<p>The recipe to use to create the component. The recipe defines the component's metadata, parameters, dependencies, lifecycle, artifacts, and platform compatibility.</p> <p>You must specify either <code>inlineRecipe</code> or <code>lambdaFunction</code>.</p>"""
    lambda_function: NotRequired[
        "capo_greengrassv2.types.lambda_function_recipe_source.LambdaFunctionRecipeSource"
    ]
    """<p>The parameters to create a component from a Lambda function.</p> <p>You must specify either <code>inlineRecipe</code> or <code>lambdaFunction</code>.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""
    client_token: NotRequired[
        "capo_greengrassv2.types.client_token_string.ClientTokenString"
    ]
    """<p>A unique, case-sensitive identifier that you can provide to ensure that the request is idempotent. Idempotency means that the request is successfully processed only once, even if you send the request multiple times. When a request succeeds, and you specify the same client token for subsequent successful requests, the IoT Greengrass V2 service returns the successful response that it caches from the previous request. IoT Greengrass V2 caches successful responses for idempotent requests for up to 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComponentVersionRequest) -> dict:
    out: dict = {}
    if "inline_recipe" in value:
        import capo_greengrassv2.types.recipe_blob

        out["inlineRecipe"] = capo_greengrassv2.types.recipe_blob.serialize_json(
            value["inline_recipe"]
        )
    if "lambda_function" in value:
        import capo_greengrassv2.types.lambda_function_recipe_source

        out["lambdaFunction"] = (
            capo_greengrassv2.types.lambda_function_recipe_source.serialize_json(
                value["lambda_function"]
            )
        )
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateComponentVersionRequest:
    out: CreateComponentVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("inlineRecipe") is not None:
        import capo_greengrassv2.types.recipe_blob

        out["inline_recipe"] = capo_greengrassv2.types.recipe_blob.deserialize_json(
            data["inlineRecipe"]
        )
    if data.get("lambdaFunction") is not None:
        import capo_greengrassv2.types.lambda_function_recipe_source

        out["lambda_function"] = (
            capo_greengrassv2.types.lambda_function_recipe_source.deserialize_json(
                data["lambdaFunction"]
            )
        )
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
