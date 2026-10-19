"""Generated from Smithy shape ``com.amazonaws.appsync#AuthorizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.authorization_type
    import capo_appsync.types.aws_iam_config


class AuthorizationConfig(TypedDict, closed=True):
    authorization_type: "capo_appsync.types.authorization_type.AuthorizationType"
    """<p>The authorization type that the HTTP endpoint requires.</p> <ul> <li> <p> <b>AWS_IAM</b>: The authorization type is Signature Version 4 (SigV4).</p> </li> </ul>"""
    aws_iam_config: NotRequired["capo_appsync.types.aws_iam_config.AwsIamConfig"]
    """<p>The Identity and Access Management (IAM) settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.authorization_type

    out["authorizationType"] = capo_appsync.types.authorization_type.serialize_json(
        value["authorization_type"]
    )
    if "aws_iam_config" in value:
        import capo_appsync.types.aws_iam_config

        out["awsIamConfig"] = capo_appsync.types.aws_iam_config.serialize_json(
            value["aws_iam_config"]
        )
    return out


def deserialize_json(data: dict) -> AuthorizationConfig:
    out: AuthorizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("authorizationType") is not None:
        import capo_appsync.types.authorization_type

        out["authorization_type"] = (
            capo_appsync.types.authorization_type.deserialize_json(
                data["authorizationType"]
            )
        )
    else:
        import typing

        out["authorization_type"] = typing.cast(
            "capo_appsync.types.authorization_type.AuthorizationType", ""
        )
    if data.get("awsIamConfig") is not None:
        import capo_appsync.types.aws_iam_config

        out["aws_iam_config"] = capo_appsync.types.aws_iam_config.deserialize_json(
            data["awsIamConfig"]
        )
    return out
