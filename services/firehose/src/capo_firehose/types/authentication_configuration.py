"""Generated from Smithy shape ``com.amazonaws.firehose#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.connectivity
    import capo_firehose.types.role_arn


class AuthenticationConfiguration(TypedDict, closed=True):
    role_arn: "capo_firehose.types.role_arn.RoleARN"
    """<p>The ARN of the role used to access the Amazon MSK cluster.</p>"""
    connectivity: "capo_firehose.types.connectivity.Connectivity"
    """<p>The type of connectivity used to access the Amazon MSK cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    import capo_firehose.types.connectivity

    out["Connectivity"] = capo_firehose.types.connectivity.serialize_aws_json_1_1(
        value["connectivity"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    if data.get("Connectivity") is not None:
        import capo_firehose.types.connectivity

        out["connectivity"] = capo_firehose.types.connectivity.deserialize_aws_json_1_1(
            data["Connectivity"]
        )
    else:
        import typing

        out["connectivity"] = typing.cast(
            "capo_firehose.types.connectivity.Connectivity", ""
        )
    return out
