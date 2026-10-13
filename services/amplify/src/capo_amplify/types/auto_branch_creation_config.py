"""Generated from Smithy shape ``com.amazonaws.amplify#AutoBranchCreationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.basic_auth_credentials
    import capo_amplify.types.build_spec
    import capo_amplify.types.enable_auto_build
    import capo_amplify.types.enable_basic_auth
    import capo_amplify.types.enable_performance_mode
    import capo_amplify.types.enable_pull_request_preview
    import capo_amplify.types.environment_variables
    import capo_amplify.types.framework
    import capo_amplify.types.pull_request_environment_name
    import capo_amplify.types.stage


class AutoBranchCreationConfig(TypedDict, closed=True):
    stage: NotRequired["capo_amplify.types.stage.Stage"]
    """<p>Describes the current stage for the autocreated branch. </p>"""
    framework: NotRequired["capo_amplify.types.framework.Framework"]
    """<p>The framework for the autocreated branch. </p>"""
    enable_auto_build: NotRequired[
        "capo_amplify.types.enable_auto_build.EnableAutoBuild"
    ]
    """<p>Enables auto building for the autocreated branch. </p>"""
    environment_variables: NotRequired[
        "capo_amplify.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables for the autocreated branch. </p>"""
    basic_auth_credentials: NotRequired[
        "capo_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The basic authorization credentials for the autocreated branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    enable_basic_auth: NotRequired[
        "capo_amplify.types.enable_basic_auth.EnableBasicAuth"
    ]
    """<p>Enables basic authorization for the autocreated branch. </p>"""
    enable_performance_mode: NotRequired[
        "capo_amplify.types.enable_performance_mode.EnablePerformanceMode"
    ]
    """<p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>"""
    build_spec: NotRequired["capo_amplify.types.build_spec.BuildSpec"]
    """<p>The build specification (build spec) for the autocreated branch. </p>"""
    enable_pull_request_preview: NotRequired[
        "capo_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
    ]
    """<p>Enables pull request previews for the autocreated branch. </p>"""
    pull_request_environment_name: NotRequired[
        "capo_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
    ]
    """<p>The Amplify environment name for the pull request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoBranchCreationConfig) -> dict:
    out: dict = {}
    if "stage" in value:
        import capo_amplify.types.stage

        out["stage"] = capo_amplify.types.stage.serialize_json(value["stage"])
    if "framework" in value:
        out["framework"] = value["framework"]
    if "enable_auto_build" in value:
        out["enableAutoBuild"] = value["enable_auto_build"]
    if "environment_variables" in value:
        import capo_amplify.types.environment_variables

        out["environmentVariables"] = (
            capo_amplify.types.environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "enable_basic_auth" in value:
        out["enableBasicAuth"] = value["enable_basic_auth"]
    if "enable_performance_mode" in value:
        out["enablePerformanceMode"] = value["enable_performance_mode"]
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    if "enable_pull_request_preview" in value:
        out["enablePullRequestPreview"] = value["enable_pull_request_preview"]
    if "pull_request_environment_name" in value:
        out["pullRequestEnvironmentName"] = value["pull_request_environment_name"]
    return out


def deserialize_json(data: dict) -> AutoBranchCreationConfig:
    out: AutoBranchCreationConfig = {}  # type: ignore[typeddict-item]
    if data.get("stage") is not None:
        import capo_amplify.types.stage

        out["stage"] = capo_amplify.types.stage.deserialize_json(data["stage"])
    if data.get("framework") is not None:
        out["framework"] = data["framework"]
    if data.get("enableAutoBuild") is not None:
        out["enable_auto_build"] = data["enableAutoBuild"]
    if data.get("environmentVariables") is not None:
        import capo_amplify.types.environment_variables

        out["environment_variables"] = (
            capo_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("basicAuthCredentials") is not None:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if data.get("enableBasicAuth") is not None:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    if data.get("enablePerformanceMode") is not None:
        out["enable_performance_mode"] = data["enablePerformanceMode"]
    if data.get("buildSpec") is not None:
        out["build_spec"] = data["buildSpec"]
    if data.get("enablePullRequestPreview") is not None:
        out["enable_pull_request_preview"] = data["enablePullRequestPreview"]
    if data.get("pullRequestEnvironmentName") is not None:
        out["pull_request_environment_name"] = data["pullRequestEnvironmentName"]
    return out


def redact_sensitive(value: AutoBranchCreationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "basic_auth_credentials" in value:
        out["basic_auth_credentials"] = "*** Sensitive Data Redacted ***"
    if "build_spec" in value:
        out["build_spec"] = "*** Sensitive Data Redacted ***"
    return out
