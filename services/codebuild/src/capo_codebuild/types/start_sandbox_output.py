"""Generated from Smithy shape ``com.amazonaws.codebuild#StartSandboxOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox


class StartSandboxOutput(TypedDict, closed=True):
    sandbox: NotRequired["capo_codebuild.types.sandbox.Sandbox"]
    """<p>Information about the requested sandbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSandboxOutput) -> dict:
    out: dict = {}
    if "sandbox" in value:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.serialize_aws_json_1_1(
            value["sandbox"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSandboxOutput:
    out: StartSandboxOutput = {}  # type: ignore[typeddict-item]
    if data.get("sandbox") is not None:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.deserialize_aws_json_1_1(
            data["sandbox"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartSandboxOutput) -> dict:
    out: dict = {}
    if "sandbox" in value:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.serialize_cbor(value["sandbox"])
    return out


def deserialize_cbor(data: dict) -> StartSandboxOutput:
    out: StartSandboxOutput = {}  # type: ignore[typeddict-item]
    if data.get("sandbox") is not None:
        import capo_codebuild.types.sandbox

        out["sandbox"] = capo_codebuild.types.sandbox.deserialize_cbor(data["sandbox"])
    return out
