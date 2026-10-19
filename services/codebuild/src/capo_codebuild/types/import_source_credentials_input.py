"""Generated from Smithy shape ``com.amazonaws.codebuild#ImportSourceCredentialsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.auth_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.sensitive_non_empty_string
    import capo_codebuild.types.server_type
    import capo_codebuild.types.wrapper_boolean


class ImportSourceCredentialsInput(TypedDict, closed=True):
    username: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The Bitbucket username when the <code>authType</code> is BASIC_AUTH. This parameter is not valid for other types of source providers or connections. </p>"""
    token: "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p> For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is either the access token or the app password. For the <code>authType</code> CODECONNECTIONS, this is the <code>connectionArn</code>. For the <code>authType</code> SECRETS_MANAGER, this is the <code>secretArn</code>.</p>"""
    server_type: "capo_codebuild.types.server_type.ServerType"
    """<p> The source provider used for this project. </p>"""
    auth_type: "capo_codebuild.types.auth_type.AuthType"
    """<p> The type of authentication used to connect to a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the CodeBuild console.</p>"""
    should_overwrite: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p> Set to <code>false</code> to prevent overwriting the repository source credentials. Set to <code>true</code> to overwrite the repository source credentials. The default value is <code>true</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSourceCredentialsInput) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    out["token"] = value["token"]
    import capo_codebuild.types.server_type

    out["serverType"] = capo_codebuild.types.server_type.serialize_aws_json_1_1(
        value["server_type"]
    )
    import capo_codebuild.types.auth_type

    out["authType"] = capo_codebuild.types.auth_type.serialize_aws_json_1_1(
        value["auth_type"]
    )
    if "should_overwrite" in value:
        out["shouldOverwrite"] = value["should_overwrite"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSourceCredentialsInput:
    out: ImportSourceCredentialsInput = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        out["token"] = ""
    if data.get("serverType") is not None:
        import capo_codebuild.types.server_type

        out["server_type"] = capo_codebuild.types.server_type.deserialize_aws_json_1_1(
            data["serverType"]
        )
    else:
        import typing

        out["server_type"] = typing.cast(
            "capo_codebuild.types.server_type.ServerType", ""
        )
    if data.get("authType") is not None:
        import capo_codebuild.types.auth_type

        out["auth_type"] = capo_codebuild.types.auth_type.deserialize_aws_json_1_1(
            data["authType"]
        )
    else:
        import typing

        out["auth_type"] = typing.cast("capo_codebuild.types.auth_type.AuthType", "")
    if data.get("shouldOverwrite") is not None:
        out["should_overwrite"] = data["shouldOverwrite"]
    return out


def redact_sensitive(value: ImportSourceCredentialsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
