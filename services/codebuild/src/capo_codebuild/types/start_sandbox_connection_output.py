"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.ssm_session


class StartSandboxConnectionOutput(TypedDict, closed=True):
    ssm_session: NotRequired["capo_codebuild.types.ssm_session.SSMSession"]
    """<p>Information about the Session Manager session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxConnectionOutput) -> dict:
    out: dict = {}
    if "ssm_session" in value:
        import capo_codebuild.types.ssm_session

        out["ssmSession"] = capo_codebuild.types.ssm_session.serialize_aws_json_1_1(
            value["ssm_session"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxConnectionOutput:
    out: StartSandboxConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ssmSession") is not None:
        import capo_codebuild.types.ssm_session

        out["ssm_session"] = capo_codebuild.types.ssm_session.deserialize_aws_json_1_1(
            data["ssmSession"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartSandboxConnectionOutput) -> dict:
    out: dict = {}
    if "ssm_session" in value:
        import capo_codebuild.types.ssm_session

        out["ssmSession"] = capo_codebuild.types.ssm_session.serialize_cbor(
            value["ssm_session"]
        )
    return out


def deserialize_cbor(data: dict) -> StartSandboxConnectionOutput:
    out: StartSandboxConnectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ssmSession") is not None:
        import capo_codebuild.types.ssm_session

        out["ssm_session"] = capo_codebuild.types.ssm_session.deserialize_cbor(
            data["ssmSession"]
        )
    return out
