"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaFunctionRecipeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_dependency_map
    import capo_greengrassv2.types.component_name_string
    import capo_greengrassv2.types.component_platform_list
    import capo_greengrassv2.types.component_version_string
    import capo_greengrassv2.types.lambda_execution_parameters
    import capo_greengrassv2.types.non_empty_string


class LambdaFunctionRecipeSource(TypedDict, closed=True):
    lambda_arn: "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the Lambda function. The ARN must include the version of the function to import. You can't use version aliases like <code>$LATEST</code>.</p>"""
    component_name: NotRequired[
        "capo_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p> <p>Defaults to the name of the Lambda function.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p> <p>Defaults to the version of the Lambda function as a semantic version. For example, if your function version is <code>3</code>, the component version becomes <code>3.0.0</code>.</p>"""
    component_platforms: NotRequired[
        "capo_greengrassv2.types.component_platform_list.ComponentPlatformList"
    ]
    """<p>The platforms that the component version supports.</p>"""
    component_dependencies: NotRequired[
        "capo_greengrassv2.types.component_dependency_map.ComponentDependencyMap"
    ]
    """<p>The component versions on which this Lambda function component depends.</p>"""
    component_lambda_parameters: NotRequired[
        "capo_greengrassv2.types.lambda_execution_parameters.LambdaExecutionParameters"
    ]
    """<p>The system and runtime parameters for the Lambda function as it runs on the Greengrass core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionRecipeSource) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "component_platforms" in value:
        import capo_greengrassv2.types.component_platform_list

        out["componentPlatforms"] = (
            capo_greengrassv2.types.component_platform_list.serialize_json(
                value["component_platforms"]
            )
        )
    if "component_dependencies" in value:
        import capo_greengrassv2.types.component_dependency_map

        out["componentDependencies"] = (
            capo_greengrassv2.types.component_dependency_map.serialize_json(
                value["component_dependencies"]
            )
        )
    if "component_lambda_parameters" in value:
        import capo_greengrassv2.types.lambda_execution_parameters

        out["componentLambdaParameters"] = (
            capo_greengrassv2.types.lambda_execution_parameters.serialize_json(
                value["component_lambda_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> LambdaFunctionRecipeSource:
    out: LambdaFunctionRecipeSource = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        raise DeserializationError("LambdaFunctionRecipeSource.lambda_arn required")
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("componentPlatforms") is not None:
        import capo_greengrassv2.types.component_platform_list

        out["component_platforms"] = (
            capo_greengrassv2.types.component_platform_list.deserialize_json(
                data["componentPlatforms"]
            )
        )
    if data.get("componentDependencies") is not None:
        import capo_greengrassv2.types.component_dependency_map

        out["component_dependencies"] = (
            capo_greengrassv2.types.component_dependency_map.deserialize_json(
                data["componentDependencies"]
            )
        )
    if data.get("componentLambdaParameters") is not None:
        import capo_greengrassv2.types.lambda_execution_parameters

        out["component_lambda_parameters"] = (
            capo_greengrassv2.types.lambda_execution_parameters.deserialize_json(
                data["componentLambdaParameters"]
            )
        )
    return out
