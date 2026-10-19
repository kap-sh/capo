"""Generated from Smithy shape ``com.amazonaws.mediastore#GetCorsPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.cors_policy


class GetCorsPolicyOutput(TypedDict, closed=True):
    cors_policy: "capo_mediastore.types.cors_policy.CorsPolicy"
    """<p>The CORS policy assigned to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCorsPolicyOutput) -> dict:
    out: dict = {}
    import capo_mediastore.types.cors_policy

    out["CorsPolicy"] = capo_mediastore.types.cors_policy.serialize_aws_json_1_1(
        value["cors_policy"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCorsPolicyOutput:
    out: GetCorsPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("CorsPolicy") is not None:
        import capo_mediastore.types.cors_policy

        out["cors_policy"] = capo_mediastore.types.cors_policy.deserialize_aws_json_1_1(
            data["CorsPolicy"]
        )
    else:
        out["cors_policy"] = []
    return out
