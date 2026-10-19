"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceAuth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.source_auth_type
    import capo_codebuild.types.string


class SourceAuth(TypedDict, closed=True):
    type: "capo_codebuild.types.source_auth_type.SourceAuthType"
    """<p>The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.</p>"""
    resource: NotRequired["capo_codebuild.types.string.String"]
    """<p>The resource value that applies to the specified authorization type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAuth) -> dict:
    out: dict = {}
    import capo_codebuild.types.source_auth_type

    out["type"] = capo_codebuild.types.source_auth_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAuth:
    out: SourceAuth = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.source_auth_type

        out["type"] = capo_codebuild.types.source_auth_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codebuild.types.source_auth_type.SourceAuthType", ""
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    return out
