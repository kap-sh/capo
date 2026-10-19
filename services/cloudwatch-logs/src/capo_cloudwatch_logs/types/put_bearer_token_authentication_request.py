"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutBearerTokenAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.bearer_token_authentication_enabled
    import capo_cloudwatch_logs.types.log_group_identifier


class PutBearerTokenAuthenticationRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    r"""<p>The name or ARN of the log group.</p> <p>Type: String</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512.</p> <p>Pattern: <code>[\.\-_/#A-Za-z0-9]+</code> </p> <p>Required: Yes</p>"""
    bearer_token_authentication_enabled: "capo_cloudwatch_logs.types.bearer_token_authentication_enabled.BearerTokenAuthenticationEnabled"
    """<p>Whether to enable bearer token authentication.</p> <p>Type: Boolean</p> <p>Required: Yes</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutBearerTokenAuthenticationRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    out["bearerTokenAuthenticationEnabled"] = value[
        "bearer_token_authentication_enabled"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutBearerTokenAuthenticationRequest:
    out: PutBearerTokenAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        out["log_group_identifier"] = ""
    if data.get("bearerTokenAuthenticationEnabled") is not None:
        out["bearer_token_authentication_enabled"] = data[
            "bearerTokenAuthenticationEnabled"
        ]
    else:
        out["bearer_token_authentication_enabled"] = False
    return out
