"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceCredentialsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.auth_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.server_type
    import capo_codebuild.types.string


class SourceCredentialsInfo(TypedDict, closed=True):
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the token. </p>"""
    server_type: NotRequired["capo_codebuild.types.server_type.ServerType"]
    """<p> The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, GITLAB, GITLAB_SELF_MANAGED, or BITBUCKET. </p>"""
    auth_type: NotRequired["capo_codebuild.types.auth_type.AuthType"]
    """<p> The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH, PERSONAL_ACCESS_TOKEN, CODECONNECTIONS, or SECRETS_MANAGER. </p>"""
    resource: NotRequired["capo_codebuild.types.string.String"]
    """<p>The connection ARN if your authType is CODECONNECTIONS or SECRETS_MANAGER.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceCredentialsInfo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "server_type" in value:
        import capo_codebuild.types.server_type

        out["serverType"] = capo_codebuild.types.server_type.serialize_aws_json_1_1(
            value["server_type"]
        )
    if "auth_type" in value:
        import capo_codebuild.types.auth_type

        out["authType"] = capo_codebuild.types.auth_type.serialize_aws_json_1_1(
            value["auth_type"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceCredentialsInfo:
    out: SourceCredentialsInfo = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("serverType") is not None:
        import capo_codebuild.types.server_type

        out["server_type"] = capo_codebuild.types.server_type.deserialize_aws_json_1_1(
            data["serverType"]
        )
    if data.get("authType") is not None:
        import capo_codebuild.types.auth_type

        out["auth_type"] = capo_codebuild.types.auth_type.deserialize_aws_json_1_1(
            data["authType"]
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceCredentialsInfo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "server_type" in value:
        import capo_codebuild.types.server_type

        out["serverType"] = capo_codebuild.types.server_type.serialize_cbor(
            value["server_type"]
        )
    if "auth_type" in value:
        import capo_codebuild.types.auth_type

        out["authType"] = capo_codebuild.types.auth_type.serialize_cbor(
            value["auth_type"]
        )
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_cbor(data: dict) -> SourceCredentialsInfo:
    out: SourceCredentialsInfo = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("serverType") is not None:
        import capo_codebuild.types.server_type

        out["server_type"] = capo_codebuild.types.server_type.deserialize_cbor(
            data["serverType"]
        )
    if data.get("authType") is not None:
        import capo_codebuild.types.auth_type

        out["auth_type"] = capo_codebuild.types.auth_type.deserialize_cbor(
            data["authType"]
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    return out
