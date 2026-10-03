"""Generated from Smithy shape ``com.amazonaws.lambda#PutRuntimeManagementConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.update_runtime_on


class PutRuntimeManagementConfigRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>"""
    update_runtime_on: "capo_lambda.types.update_runtime_on.UpdateRuntimeOn"
    """<p>Specify the runtime update mode.</p> <ul> <li> <p> <b>Auto (default)</b> - Automatically update to the most recent and secure runtime version using a <a href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase">Two-phase runtime version rollout</a>. This is the best choice for most customers to ensure they always benefit from runtime updates.</p> </li> <li> <p> <b>Function update</b> - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.</p> </li> <li> <p> <b>Manual</b> - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback">Roll back a runtime version</a>.</p> </li> </ul>"""
    runtime_version_arn: NotRequired[
        "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime version you want the function to use.</p> <note> <p>This is only required if you're using the <b>Manual</b> runtime update mode.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRuntimeManagementConfigRequest) -> dict:
    out: dict = {}
    import capo_lambda.types.update_runtime_on

    out["UpdateRuntimeOn"] = capo_lambda.types.update_runtime_on.serialize_json(
        value["update_runtime_on"]
    )
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    return out


def deserialize_json(data: dict) -> PutRuntimeManagementConfigRequest:
    out: PutRuntimeManagementConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateRuntimeOn") is not None:
        import capo_lambda.types.update_runtime_on

        out["update_runtime_on"] = capo_lambda.types.update_runtime_on.deserialize_json(
            data["UpdateRuntimeOn"]
        )
    else:
        raise DeserializationError(
            "PutRuntimeManagementConfigRequest.update_runtime_on required"
        )
    if data.get("RuntimeVersionArn") is not None:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    return out
